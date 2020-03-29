import json
import shutil
from langdetect import detect
from pathlib import Path


def main():
    # Setup output folder
    input_folder = Path.cwd().parent.parent / 'corpus' / 'pubmed' / 'json'
    output_folder = Path.cwd().parent.parent / 'corpus' / 'pubmed' / 'raw'
    if Path.exists(output_folder):
        shutil.rmtree(output_folder)
    Path.mkdir(output_folder)

    # Get JSON files
    counter = 0
    for file in input_folder.iterdir():
        with open(file) as f:
            # Get data
            data = json.load(f)
            title = data['title']

            # Get english paragraphs
            abstract = data['abstract']
            abstract_paragraphs = get_eng_paragraphs(abstract)

            methods = data['methods'] if 'methods' in data else ''
            methods_paragraphs = get_eng_paragraphs(methods)

            results = data['results'] if 'results' in data else ''
            results_paragraphs = get_eng_paragraphs(results)

            conclusions = data['conclusions'] if 'conclusions' in data else ''
            conclusions_paragraphs = get_eng_paragraphs(conclusions)

            # Write only english paragraphs
            if abstract_paragraphs or methods_paragraphs or conclusions_paragraphs or results_paragraphs:
                with open(output_folder / (file.stem + ".txt"), "a") as file_object:
                    # Title
                    file_object.write('TITLE:\n')
                    file_object.write(title)
                    file_object.write('\n\n')

                    write_paragraphs(abstract_paragraphs, 'ABSTRACT', file_object)
                    write_paragraphs(methods_paragraphs, 'METHODS', file_object)
                    write_paragraphs(results_paragraphs, 'RESULTS', file_object)
                    write_paragraphs(conclusions_paragraphs, 'CONCLUSIONS', file_object)

                counter += 1
                print(counter)


def write_paragraphs(paragraphs, section, file_object):
    if paragraphs:
        file_object.write(section + ':\n')
        for paragraph in paragraphs:
            file_object.write(paragraph)
            file_object.write('\n')
        file_object.write('\n\n')


def get_eng_paragraphs(text):
    # Get english paragraphs
    paragraphs_eng = []
    if text:
        paragraphs = text.split('\n', 1)
        for paragraph in paragraphs:
            if detect(paragraph) == 'en':
                paragraphs_eng.append(paragraph)
    return paragraphs_eng


if __name__ == "__main__":
    main()
