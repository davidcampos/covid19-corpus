from pathlib import Path
import json
import requests
import urllib3
import multiprocessing as mp
from timeit import default_timer as timer
from datetime import timedelta
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import re

input_folder = Path(sys.argv[1])
output_folder = Path(sys.argv[2])


def main():
    start = timer()

    input_files = []
    for file in input_folder.glob('*.json'):
        input_files.append(file)

    output_files_names = []
    for file in output_folder.glob('*.json'):
        output_files_names.append(file.name)

    annotate_files = []
    for file in input_files:
        if file.name not in output_files_names:
            annotate_files.append(file)

    threads = 6
    if len(annotate_files) < threads:
        threads = len(annotate_files)

    pool = mp.Pool(threads)
    pool.map(annotate_file, [file for file in annotate_files])
    pool.close()

    end = timer()
    print(timedelta(seconds=end - start))


def annotate_file(file):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    print(file.name)
    with open(file) as f:
        data = json.load(f)

        title = data['metadata']['title']
        data['metadata']['annotations'] = annotate(title)

        abstract = data['abstract']
        for entry in abstract:
            entry['annotations'] = annotate(entry['text'])

        body_text = data['body_text']
        for entry in body_text:
            entry['annotations'] = annotate(entry['text'])

        bib_entries = data['bib_entries']
        for entry in bib_entries:
            bib_entry = bib_entries[entry]
            bib_entry['annotations'] = annotate(bib_entry['title'])

        ref_entries = data['ref_entries']
        for entry in ref_entries:
            ref_entry = ref_entries[entry]
            ref_entry['annotations'] = annotate(ref_entry['text'])

        back_matter = data['back_matter']
        for entry in back_matter:
            entry['annotations'] = annotate(entry['text'])

        # Write article to JSON
        with open(output_folder / file.name, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False)


def annotate(text):
    data = {
        "groups": {
            "COMP": True,
            "PATH": True,
            "DISO": True,
            "PROC": True,
            "FUNC": True,
            "PRGE": True,
            "ENZY": True,
            "CHED": True,
            "MRNA": True,
            "SPEC": True,
            "ANAT": True
        },
        "text": text,
        "crlf": False,
        "fromFile": False,
        "echo": True,
    }
    url = 'https://localhost:8010/annotate/default/annotate?tool=neji&email=david.marques.campos@gmail.com'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }

    entity_pattern = re.compile("(.+)\|(.*?:.*?:.*?:.+?;*)\|([0-9]+)")

    try:
        response = requests_retry_session().post(url, json=data, headers=headers, verify=False, timeout=30)
        content = response.json()
        annotations = []
        for entity in content['entities']:
            entity_match = re.match(entity_pattern, entity)
            name = entity_match.group(1)
            ids = entity_match.group(2).split(';')
            start = entity_match.group(3)

            if not start.isdigit():
                print("damm")

            annotations.append({
                "start": start,
                "text": name,
                "ids": ids
            })
        return annotations
    except requests.exceptions.RequestException as e:
        print("ERROR on text: ", text)
        return []


def requests_retry_session(
        retries=5,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
):
    session = session or requests.Session()
    # session.headers
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


if __name__ == "__main__":
    main()
