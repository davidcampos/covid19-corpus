from pathlib import Path
import sys
import json

input_folder = Path(sys.argv[1])


def main():
    articles = 0
    occurrences = {
        "PRGE": 0,
        "SPEC": 0,
        "ANAT": 0,
        "CHED": 0,
        "COMP": 0,
        "DISO": 0,
        "ENZY": 0,
        "FUNC": 0,
        "MRNA": 0,
        "PATH": 0,
        "PROC": 0
    }
    unique = {
        "PRGE": [],
        "SPEC": [],
        "ANAT": [],
        "CHED": [],
        "COMP": [],
        "DISO": [],
        "ENZY": [],
        "FUNC": [],
        "MRNA": [],
        "PATH": [],
        "PROC": []
    }
    names = {
        "DISO": "Disorder",
        "SPEC": "Species",
        "CHED": "Chemical or Drug",
        "PRGE": "Gene and Protein",
        "ENZY": "Enzyme",
        "ANAT": "Anatomy",
        "PROC": "Biological Process",
        "FUNC": "Molecular Function",
        "COMP": "Cellular Component",
        "PATH": "Pathway",
        "MRNA": "microRNA"
    }

    for file in input_folder.rglob('*.json'):
        articles += 1
        print(articles)
        with open(file) as f:
            data = json.load(f)
            
            count_annotations(data['metadata']['annotations'], occurrences, unique)

            abstract = data['abstract']
            for entry in abstract:
                count_annotations(entry['annotations'], occurrences, unique)

            body_text = data['body_text']
            for entry in body_text:
                count_annotations(entry['annotations'], occurrences, unique)

            bib_entries = data['bib_entries']
            for entry in bib_entries:
                bib_entry = bib_entries[entry]
                count_annotations(bib_entry['annotations'], occurrences, unique)

            ref_entries = data['ref_entries']
            for entry in ref_entries:
                ref_entry = ref_entries[entry]
                count_annotations(ref_entry['annotations'], occurrences, unique)

            back_matter = data['back_matter']
            for entry in back_matter:
                count_annotations(entry['annotations'], occurrences, unique)

    print('# Articles: ', articles)
    print('# Per entity:')
    total_occurrences = 0
    total_unique = 0
    for group in names:
        print('| ', names[group], ' | ', occurrences[group], ' | ', len(unique[group]), ' |')
        total_occurrences += occurrences[group]
        total_unique += len(unique[group])

    print('# Total Occurrences: ', total_occurrences)
    print('# Total Unique: ', total_unique)


def count_annotations(annotations, occurrences, unique):
    for annotation in annotations:
        for group in get_unique_groups(annotation['ids']):
            occurrences[group] += 1
        for identifier in annotation['ids']:
            group = identifier.split(":")[3].strip()
            if identifier not in unique[group]:
                unique[group].append(identifier)


def get_unique_groups(ids):
    unique_groups = []
    for identifier in ids:
        group = identifier.split(":")[3].strip()
        if group not in unique_groups:
            unique_groups.append(group)
    return unique_groups


if __name__ == "__main__":
    main()
