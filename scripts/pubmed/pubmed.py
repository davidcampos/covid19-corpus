import datetime
import json
import shutil
from pymed import PubMed
from pathlib import Path


def date_converter(o):
    if isinstance(o, datetime.date):
        return o.__str__()


def main():
    # Setup output folder
    output_folder = Path.cwd().parent.parent / 'corpus' / 'pubmed' / 'json'
    if Path.exists(output_folder):
        shutil.rmtree(output_folder)
    Path.mkdir(output_folder)

    # Create a PubMed object that GraphQL can use to query
    pubmed = PubMed(tool="DavidCampos", email="david.marques.campos@gmail.com")

    # Create a GraphQL query in plain text
    query = "(\"2000\"[Date - Publication] : \"3000\"[Date - Publication]) AND " \
            "((COVID-19) OR (Coronavirus) OR (Corona virus) OR (2019-nCoV) OR " \
            "(SARS-CoV) OR (MERS-CoV) OR (Severe Acute Respiratory Syndrome) OR " \
            "(Middle East Respiratory Syndrome) OR " \
            "(2019 novel coronavirus disease[MeSH Terms]) OR (2019 novel coronavirus infection[MeSH Terms]) OR " \
            "(2019-nCoV disease[MeSH Terms]) OR (2019-nCoV infection[MeSH Terms]) OR " \
            "(coronavirus disease 2019[MeSH Terms]) OR (coronavirus disease-19[MeSH Terms]))"

    # Execute the query against the API
    results = pubmed.query(query, max_results=1000000)

    # Loop over the retrieved articles
    counter = 0
    for article in results:
        # Discard if abstract empty
        if article.abstract is None or article.abstract == "":
            continue

        # Get PubmedID
        pubmed_id = article.pubmed_id
        if '\n' in pubmed_id:
            rest = pubmed_id.split('\n', 1)
            pubmed_id = rest[0]
        article.pubmed_id = pubmed_id

        # Get article as dict
        article_dict = article.toDict()

        # Write article to JSON
        with open(output_folder / (pubmed_id + ".json"), 'w') as outfile:
            json.dump(article_dict, outfile, default=date_converter)
        counter += 1
        print(counter)


if __name__ == "__main__":
    main()
