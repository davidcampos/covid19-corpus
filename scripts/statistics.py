from pathlib import Path
import re


def main():
    input_folder = Path.cwd().parent / 'corpus' / 'pubmed' / 'annotations'
    abstracts = 0
    entities = {
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
    id_pattern = re.compile("N[0-9]+\tReference T[0-9]+ (.*?)\t")
    entity_pattern = re.compile("T[0-9]+\t(.+?) [0-9]+ [0-9]+")

    for file in input_folder.iterdir():
        abstracts += 1
        with open(file) as fp:
            for line in fp.readlines():
                if entity_match := re.match(entity_pattern, line):
                    group = entity_match.group(1).strip()
                    entities[group] += 1
                elif id_match := re.match(id_pattern, line):
                    identifier = id_match.group(1).strip()
                    group = identifier.split(":")[3].strip()
                    if identifier not in unique[group]:
                        unique[group].append(identifier)

    print('# Abstracts: ', abstracts)

    print('# Occurrences per entity:')
    total_occurrences = 0
    for group in entities:
        print('   ', group, ': ', entities[group])
        total_occurrences += entities[group]
    print('# Total Occurrences: ', total_occurrences)

    print('# Unique entities:')
    total_unique = 0
    for group in unique:
        print('   ', group, ': ', len(unique[group]))
        total_unique += len(unique[group])
    print('# Total Unique: ', total_unique)


if __name__ == "__main__":
    main()
