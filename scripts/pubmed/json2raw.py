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
            abstract = data['abstract']

            # Get english paragraphs
            paragraphs = abstract.split('\n', 1)
            paragraphs_eng = []
            for paragraph in paragraphs:
                if detect(paragraph) == 'en':
                    paragraphs_eng.append(paragraph)

            # Write only english paragraphs
            if paragraphs_eng:
                with open(output_folder / (file.stem + ".txt"), "a") as file_object:
                    file_object.write('TITLE:\n')
                    file_object.write(title)
                    file_object.write('\n\n')
                    file_object.write('ABSTRACT:\n')
                    for paragraph in paragraphs_eng:
                        file_object.write(paragraph)
                        file_object.write('\n')
                counter += 1
                print(counter)


if __name__ == "__main__":
    main()
