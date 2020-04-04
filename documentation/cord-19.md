# CORD-19
Technical details regarding the annottion of the [**CORD-19**](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) corpus of full-text articles.

## Structure
Corpus file `corpus/cord-19_YYYYMMDD.zip` contains the following folders:
- **custom_license**: includes [PMC](https://www.ncbi.nlm.nih.gov/pmc/)  and Elsevier content;
- **noncomm_use_subset**: includes PMC content;
- **comm_use_subset**: includes PMC content;
- **biorxiv_medrxiv**: pre-prints that are not peer reviewed.

On each folder you can find one file per article, with the CORD-19 unique hash on its name.

## JSON format
The input JSON format was extended to include annotations with the following structure:

```json
"annotations": [
    {
        "start": "30",
        "text": "COVID-19",
        "ids": [
            "DOID:0080600::DISO",
            ...
        ]
    },
    ...
]
```

Each annotation has the following properties:
- **start**: start character of the annotation
- **text**: text of the annotation
- **ids**: identifiers that refer to entity type, resource and unique ID.

## Annotation
From the provided JSON files, all entries with textual content were processed and annotated, namely:

```python
title = data['metadata']['title']

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
```

The steps below show how to create a Neji server with an annotation REST API in order to annotate the corpus:

### Create server using Neji CLI:
```bash
./scripts/cord-19/server/create.sh
cp tools/neji-2.0.2/target/neji-server.zip tools/neji-server.zip
unzip tools/neji-server.zip -d tools
```

### Build Docker image:
```bash
cp scripts/cord-19/server/Dockerfile tools/neji-server/Dockerfile
cd tools/neji-server/
docker build -t neji-server .
```

### Run server on Docker container:
```bash
./scripts/cord-19/server/run.sh
```

### Annotate corpus:
```bash
./scripts/cord-19/annotate.sh
```

## Example
Find below an example of the provided JSON files, with input data provided by CORD-19 and with added annotations:

```json
{
    "paper_id": "2b34a2b59b93b191b3566d1952d4b5f794ba5e3e",
    "metadata": {
        "title": "Estimating Spot Prevalence of COVID-19 from Daily Death Data in Italy",
        "authors": [
            {
                "first": "Ali",
                "middle": [],
                "last": "Raheem",
                "suffix": "",
                "affiliation": {
                    "laboratory": "",
                    "institution": "South London and Maudsley NHS Foundation Trust",
                    "location": {}
                },
                "email": ""
            }
        ],
        "annotations": [
            {
                "start": "11",
                "text": "Spot",
                "ids": [
                    "NCBI:59837:T001:SPEC"
                ]
            },
            {
                "start": "30",
                "text": "COVID-19",
                "ids": [
                    "DOID:0080600::DISO"
                ]
            },
            {
                "start": "50",
                "text": "Death",
                "ids": [
                    "GO:0016265::PROC"
                ]
            }
        ]
    },
    "abstract": [],
    "body_text": [
        {
            "text": "COVID-19 has now been declared a pandemic by the World Health Organisation. Caused by a betacoronvirus virus SARS-CoV2 which is related to the SARS and MERS virus.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Introduction",
            "annotations": [
                {
                    "start": "0",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "62",
                    "text": "Organisation",
                    "ids": [
                        "UMLS:C0029237:T039:PROC"
                    ]
                },
                {
                    "start": "103",
                    "text": "virus",
                    "ids": [
                        "NCBI:10239:T001:SPEC"
                    ]
                },
                {
                    "start": "109",
                    "text": "SARS",
                    "ids": [
                        "UMLS:C1175175:T047:DISO"
                    ]
                },
                {
                    "start": "143",
                    "text": "SARS",
                    "ids": [
                        "UMLS:C1175175:T047:DISO"
                    ]
                },
                {
                    "start": "157",
                    "text": "virus",
                    "ids": [
                        "NCBI:10239:T001:SPEC"
                    ]
                }
            ]
        },
        {
            "text": "1 This disease appears to have a mortality rate of approximated 1-15%. However there have been a wide variety in reported proportion of cases that are asymptomatic or only show mild non-specific symptoms. Making it difficult to estimate the prevalence of COVID-19 without widespread testing which has not yet been implemented in any country. Previously authors have used this to estimate the mortality of COVID-19 (1) . Accurately estimating the prevalence of COVID-19 will allow organisations to make better informed decisions to control COVID-19.",
            "cite_spans": [
                {
                    "start": 414,
                    "end": 417,
                    "text": "(1)",
                    "ref_id": "BIBREF0"
                }
            ],
            "ref_spans": [],
            "section": "Introduction",
            "annotations": [
                {
                    "start": "255",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "405",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "460",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "539",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                }
            ]
        },
        {
            "text": "We used a linear retrospective model to estimate past point prevalence using daily number of report deaths. This model required us to calculate a nominal time to death from infection. We based this value on data available from the World Health Organisation. The WHO report time from onset of symptoms to death of about 2 weeks (4). Additionally, the mean incubation period has been reported to be 6.4 days (2) . We estimate that deaths on a given day should correlate with infections 3 weeks prior and use this with daily reported deaths to estimate the spot prevalence in the past. We obtained data on daily deaths and past cases from the European Centre for Disease Prevention and Control (3) cross referenced for accuracy with data from the World Health Organisation (4).",
            "cite_spans": [
                {
                    "start": 406,
                    "end": 409,
                    "text": "(2)",
                    "ref_id": "BIBREF1"
                }
            ],
            "ref_spans": [],
            "section": "Methods",
            "annotations": [
                {
                    "start": "100",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "162",
                    "text": "death",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "173",
                    "text": "infection",
                    "ids": [
                        "UMLS:C0021311:T047:DISO",
                        "UMLS:C0009450:T047:DISO"
                    ]
                },
                {
                    "start": "244",
                    "text": "Organisation",
                    "ids": [
                        "UMLS:C0029237:T039:PROC"
                    ]
                },
                {
                    "start": "304",
                    "text": "death",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "429",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "473",
                    "text": "infections",
                    "ids": [
                        "UMLS:C0021311:T047:DISO",
                        "UMLS:C0851162:T047:DISO"
                    ]
                },
                {
                    "start": "531",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "554",
                    "text": "spot",
                    "ids": [
                        "NCBI:59837:T001:SPEC"
                    ]
                },
                {
                    "start": "609",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "757",
                    "text": "Organisation",
                    "ids": [
                        "UMLS:C0029237:T039:PROC"
                    ]
                }
            ]
        },
        {
            "text": "Data processing was carried out with R, the Juptyer notebook and Tidyverse software suites on a Debian 9.0 Stretch using the latest Jupyter/r-notebook docker image (jupyter/r-notebook:15a66513da30) (5) (6).",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Methods",
            "annotations": []
        },
        {
            "text": "Using a case mortality of 7% was used based on the recent estimates.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Methods",
            "annotations": []
        },
        {
            "text": "Deaths d M ortality 2 All rights reserved. No reuse allowed without permission.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "P revalence d\u221221 =",
            "annotations": [
                {
                    "start": "0",
                    "text": "Deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                }
            ]
        },
        {
            "text": "author/funder, who has granted medRxiv a license to display the preprint in perpetuity.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "P revalence d\u221221 =",
            "annotations": []
        },
        {
            "text": "The copyright holder for this preprint (which was not peer-reviewed) is the . https://doi.org/10.1101/2020.03.17.20037697 doi: medRxiv preprint Where d is time in days. Using a mortality of 7%",
            "cite_spans": [],
            "ref_spans": [],
            "section": "P revalence d\u221221 =",
            "annotations": []
        },
        {
            "text": "The following data was generated using the reported number of deaths per day and new confirmed cases. From this a cumulative cases and cumulative deaths data was calculated and used to calculate the point prevalence according to the formula described above.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "P revalence d\u221221 =",
            "annotations": [
                {
                    "start": "62",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "146",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                }
            ]
        },
        {
            "text": "Using data up to the 16 th of March 2020 we can estimate the point prevalence 21 days into the past (the 24 th of February 2020). This value is subject to the inevitable jitter in deaths per day due to COVID-19, it therefore should be used to guide a trend line before interpretation. Figure 1 summaries the results graphically, the full results can be reviewed in the supplementary materials section in Table 1 . On the 24th of February when our prediction data ends there were 132 cases confirmed by Italian authorities but our model predicts there were near 26000 cases in reality.",
            "cite_spans": [],
            "ref_spans": [
                {
                    "start": 285,
                    "end": 293,
                    "text": "Figure 1",
                    "ref_id": "FIGREF2"
                },
                {
                    "start": 404,
                    "end": 411,
                    "text": "Table 1",
                    "ref_id": "TABREF2"
                }
            ],
            "section": "P revalence d\u221221 =",
            "annotations": [
                {
                    "start": "180",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "202",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                }
            ]
        },
        {
            "text": "Our model predicts that in this period there was undetected transmission resulting in a rise in cases from 28 to 18000. With a doubling period of about 2.5 days.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Italy initially confirmed 3 cases in",
            "annotations": []
        },
        {
            "text": "3 All rights reserved. No reuse allowed without permission.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Italy initially confirmed 3 cases in",
            "annotations": []
        },
        {
            "text": "author/funder, who has granted medRxiv a license to display the preprint in perpetuity.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Italy initially confirmed 3 cases in",
            "annotations": []
        },
        {
            "text": "The copyright holder for this preprint (which was not peer-reviewed) is the . https://doi.org/10.1101/2020.03.17.20037697 doi: medRxiv preprint",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Italy initially confirmed 3 cases in",
            "annotations": []
        },
        {
            "text": "The large disparity with estimated prevalence being much higher than confirmed cases indicates that either an increasing majority of cases are not detected. There seems to have been a period of several weeks where COVID-19 was transmitted in the Italian population undetected. Only a minority of cases appear to be confirmed at any point in time.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Discussion",
            "annotations": [
                {
                    "start": "214",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "227",
                    "text": "transmitted",
                    "ids": [
                        "UMLS:C0242781:T046:DISO"
                    ]
                }
            ]
        },
        {
            "text": "In this paper we present evidence that the currently confirmed cases of COVID-19 are a dramatic underestimate of the true point prevalence in Italy and a method to estimate point prevalence from daily deaths of COVID-19. Increasing the mortality would reduce the estimated prevalence but this alone could not make the estimates agree with the confirmed cases in order of magnitude. This methodology would be applicable to many other conditions and relies only on accurate estimate of deaths due to the condition which can easily be confirmed post-mortem and case mortality. Without incubation date or data on disease progression an accurate estimate can still be produced but will not provide temporal information but could be used to estimate the time from infection to death.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Conclusion",
            "annotations": [
                {
                    "start": "72",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "201",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "211",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "362",
                    "text": "order",
                    "ids": [
                        "NCBI::T001:SPEC"
                    ]
                },
                {
                    "start": "484",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "502",
                    "text": "condition",
                    "ids": [
                        "UMLS:C0012634:T047:DISO"
                    ]
                },
                {
                    "start": "609",
                    "text": "disease progression",
                    "ids": [
                        "UMLS:C0242656:T046:DISO"
                    ]
                },
                {
                    "start": "758",
                    "text": "infection",
                    "ids": [
                        "UMLS:C0021311:T047:DISO",
                        "UMLS:C0009450:T047:DISO"
                    ]
                },
                {
                    "start": "771",
                    "text": "death",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                }
            ]
        },
        {
            "text": "This model used the spot daily reported deaths which may lag the true date of death due to delays in confirming and then reporting causes of death if COVID-19 was not diagnoses ante mortem. Our estimate of point prevalence varies proportionally to the error in deaths. Deaths due to infection not reported will cause an underestimate in prevalence. Estimating true mortality rates is difficult, and our estimate varies with 4 All rights reserved. No reuse allowed without permission. author/funder, who has granted medRxiv a license to display the preprint in perpetuity.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Limitations",
            "annotations": [
                {
                    "start": "20",
                    "text": "spot",
                    "ids": [
                        "NCBI:59837:T001:SPEC"
                    ]
                },
                {
                    "start": "40",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "78",
                    "text": "death",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "141",
                    "text": "death",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "150",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "261",
                    "text": "deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "269",
                    "text": "Deaths",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "283",
                    "text": "infection",
                    "ids": [
                        "UMLS:C0021311:T047:DISO",
                        "UMLS:C0009450:T047:DISO"
                    ]
                }
            ]
        },
        {
            "text": "The copyright holder for this preprint (which was not peer-reviewed) is the . https://doi.org/10.1101/2020.03.17.20037697 doi: medRxiv preprint the reciprocal of the error in the mortality rate. Underestimating mortality will lead to increase in predicted spot prevalence. This is an evolving pandemic and due to the long incubation and time to death periods only a short period of point prevalence's can be estimated. accessed 17-March-2020].",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Limitations",
            "annotations": [
                {
                    "start": "256",
                    "text": "spot",
                    "ids": [
                        "NCBI:59837:T001:SPEC"
                    ]
                },
                {
                    "start": "345",
                    "text": "death",
                    "ids": [
                        "GO:0016265::PROC"
                    ]
                },
                {
                    "start": "351",
                    "text": "periods",
                    "ids": [
                        "GO:0042703::PROC"
                    ]
                }
            ]
        },
        {
            "text": "5 All rights reserved. No reuse allowed without permission.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "European",
            "annotations": []
        },
        {
            "text": "author/funder, who has granted medRxiv a license to display the preprint in perpetuity.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "European",
            "annotations": []
        },
        {
            "text": "The copyright holder for this preprint (which was not peer-reviewed) is the ",
            "cite_spans": [],
            "ref_spans": [],
            "section": "European",
            "annotations": []
        },
        {
            "text": "I would like to thank the healthcare workers around the globe for their tireless efforts fighting COVID-19. author/funder, who has granted medRxiv a license to display the preprint in perpetuity.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Acknowledgements",
            "annotations": [
                {
                    "start": "56",
                    "text": "globe",
                    "ids": [
                        "UMLS:C1280202:T023:ANAT",
                        "UMLS:C0015392:T023:ANAT"
                    ]
                },
                {
                    "start": "98",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                }
            ]
        },
        {
            "text": "The copyright holder for this preprint (which was not peer-reviewed) is the . https://doi.org/10.1101/2020.03.17.20037697 doi: medRxiv preprint author/funder, who has granted medRxiv a license to display the preprint in perpetuity.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Supplementary materials",
            "annotations": []
        },
        {
            "text": "The copyright holder for this preprint (which was not peer-reviewed) is the . https://doi.org/10.1101/2020.03.17.20037697 doi: medRxiv preprint author/funder, who has granted medRxiv a license to display the preprint in perpetuity.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Supplementary materials",
            "annotations": []
        },
        {
            "text": "The copyright holder for this preprint (which was not peer-reviewed) is the . https://doi.org/10.1101/2020.03.17.20037697 doi: medRxiv preprint",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Supplementary materials",
            "annotations": []
        }
    ],
    "bib_entries": {
        "BIBREF0": {
            "ref_id": "b0",
            "title": "The Lancet Infectious Diseases",
            "authors": [
                {
                    "first": "D",
                    "middle": [],
                    "last": "Baud",
                    "suffix": ""
                }
            ],
            "year": 2020,
            "venue": "",
            "volume": "",
            "issn": "",
            "pages": "",
            "other_ids": {},
            "annotations": [
                {
                    "start": "11",
                    "text": "Infectious Diseases",
                    "ids": [
                        "UMLS:C0009450:T047:DISO"
                    ]
                }
            ]
        },
        "BIBREF1": {
            "ref_id": "b1",
            "title": "Coronavirus disease 2019 (COVID-19) Situation Report -56",
            "authors": [],
            "year": 2020,
            "venue": "",
            "volume": "",
            "issn": "",
            "pages": "",
            "other_ids": {},
            "annotations": [
                {
                    "start": "0",
                    "text": "Coronavirus disease 2019",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                },
                {
                    "start": "0",
                    "text": "Coronavirus",
                    "ids": [
                        "NCBI:693996:T001:SPEC",
                        "NCBI:694013:T001:SPEC",
                        "NCBI:694002:T001:SPEC"
                    ]
                },
                {
                    "start": "26",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                }
            ]
        },
        "BIBREF2": {
            "ref_id": "b2",
            "title": "Euro surveillance : bulletin Europeen sur les maladies transmissibles =",
            "authors": [
                {
                    "first": "J",
                    "middle": [
                        "A"
                    ],
                    "last": "Backer",
                    "suffix": ""
                },
                {
                    "first": "D",
                    "middle": [],
                    "last": "Klinkenberg",
                    "suffix": ""
                },
                {
                    "first": "J",
                    "middle": [],
                    "last": "Wallinga",
                    "suffix": ""
                }
            ],
            "year": 2020,
            "venue": "European communicable disease bulletin",
            "volume": "25",
            "issn": "",
            "pages": "",
            "other_ids": {},
            "annotations": [
                {
                    "start": "0",
                    "text": "Euro",
                    "ids": [
                        "NCBI:9319:T001:SPEC"
                    ]
                },
                {
                    "start": "42",
                    "text": "les",
                    "ids": [
                        "UMLS:C0227192:T023:ANAT"
                    ]
                }
            ]
        }
    },
    "ref_entries": {
        "FIGREF0": {
            "text": "Italy on the 31 st of January 2020, our model predicts in fact there were 28 COVID-19 cases in Italy. From the 31 st of January until the 22 nd of Febuary there was no detected transmission in Italy and the number confirmed cases remained at 3.",
            "latex": null,
            "type": "figure",
            "annotations": [
                {
                    "start": "77",
                    "text": "COVID-19",
                    "ids": [
                        "DOID:0080600::DISO"
                    ]
                }
            ]
        },
        "FIGREF2": {
            "text": "Plotting Estimated Prevalence (circles), Confirmed Cases (filled triangles)",
            "latex": null,
            "type": "figure",
            "annotations": []
        },
        "TABREF2": {
            "text": "Raw results data",
            "latex": null,
            "type": "table",
            "annotations": [
                {
                    "start": "0",
                    "text": "Raw",
                    "ids": [
                        "UNIPROT:Q99323:T116:PRGE",
                        "UNIPROT:P18289:T116:PRGE",
                        "UNIPROT:P02463:T116:PRGE",
                        "UNIPROT:Q01842:T116:PRGE"
                    ]
                }
            ]
        },
        "TABREF3": {
            "text": "Raw results data All rights reserved. No reuse allowed without permission.",
            "latex": null,
            "type": "table",
            "annotations": []
        }
    },
    "back_matter": [
        {
            "text": "The authors declare no competing interests.",
            "cite_spans": [],
            "ref_spans": [],
            "section": "Competing Interests",
            "annotations": []
        }
    ]
}
```
