# COVID-19 corpus

COVID-19 corpus repository contains research articles annotated with biomedical entities of interest, namely **Disorder**, **Species**, **Chemical or Drug**, **Gene or Protein**, Enzyme, Anatomy, Biological Process, Molecular Function, Cellular Component, Pathway and microRNA.

Two different datasets are provided:
- [**CORD-19**](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) **full-text articles** with more than **31 million** annotations.
- [**Pubmed**](https://pubmed.ncbi.nlm.nih.gov/) **abstract articles** with more than **680 thousand** annotations.

Annotated corpora are **freely available** and can be used to further research topics related with COVID-19, contributing to **find insights** towards a **better understanding of the disease**, in order to **find effective drugs** and reduce the pandemic impact.

# CORD-19
Full-text research articles related with COVID-19 topics. Raw text and detailed description available on the [official CORD-19 corpus Kaggle page](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

## Download
[Download the latest version of the CORD-19 annotated corpus](corpus).

## Statistics
Overall corpus statistics:
- Number of **articles**: **33 375**
- Number of entity annotation **occurrences**: **31 272 212**
- Number of **unique** entity annotations: **141 604**

Number of annotations per entity type:

| Entity | # Occurrences| # Unique |
|--------|--------------|------------|
|  Disorder  |  5638277  |  18704  |
|  Species  |  5899678  |  30343  |
|  Chemical or Drug  |  4458126  |  11173  |
|  Gene and Protein  |  2013425  |  57738  |
|  Enzyme  |  372308  |  1480  |
|  Anatomy  |  5420584  |  10373  |
|  Biological Process  |  3701117  |  7765  |
|  Molecular Function  |  842418  |  1722  |
|  Cellular Component  |  2542276  |  1099  |
|  Pathway  |  382338  |  517  |
|  microRNA  |  1665  |  690  |

## Technical description
Technical description of the annotated CORD-19 corpus is available [here](documentation/cord-19.md).


# Pubmed
Abstracts of research articles from Pubmed related with COVID-19 topics. **Blog post about building this corpus is available at [https://hands-on-tech.github.io/2020/03/28/covid19-corpus.html](https://hands-on-tech.github.io/2020/03/28/covid19-corpus.html)**.

## Download
[Download the latest version of the annotated Pubmed corpus](corpus).

## Statistics
Overall corpus statistics:
- Number of **abstracts**: **17 740**
- Number of entity annotation **occurrences**: **683 349**
- Number of **unique** entity annotations: **29 423**

Number of annotations per entity type:

| Entity | # Occurrences| # Unique |
|--------|--------------|------------|
|  Disorder  |  183528  |  4477  |
|  Species  |  128356  |  2170  |
|  Chemical or Drug  |  70619  |  2768  |
|  Gene and Protein  |  51114  |  15025  |
|  Enzyme  |  7892  |  282  |
|  Anatomy  |  106401  |  2369  |
|  Biological Process  |  74286  |  1561  |
|  Molecular Function  |  15089  |  383  |
|  Cellular Component  |  39451  |  263  |
|  Pathway  |  6587  |  97  |
|  microRNA  |  26  |  28  |

## Technical description
Technical description of the annotated Pubmed corpus is available [here](documentation/pubmed.md).

# Resources
The following resources were applied to annotate each entity type:
- Disorder (DISO): [UMLS](https://www.nlm.nih.gov/research/umls/index.html)
- Species (SPEC): [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy)
- Chemical or Drug (CHED): [ChEBI](https://www.ebi.ac.uk/chebi/)
- Gene or Protein (PRGE): NER with CRFs and normalization with [UniProt](https://www.uniprot.org)
- Enzyme (ENZY): [ExPASy](https://enzyme.expasy.org)
- Anatomy (ANAT): [Unified Medical Language System (UMLS)](https://www.nlm.nih.gov/research/umls/index.html)
- Biological Process (PROC): [Gene Ontology (GO)](http://geneontology.org) and [UMLS](https://www.nlm.nih.gov/research/umls/index.html)
- Molecular Function (FUNC): [Gene Ontology (GO)](http://geneontology.org)
- Cellular Component (COMP): [Gene Ontology (GO)](http://geneontology.org)
- Pathway (PATH): [NCBI BioSystems](https://www.ncbi.nlm.nih.gov/biosystems)
- microRNA (MRNA): [miRBase](http://www.mirbase.org)

For more details please check the [article](https://doi.org/10.1186/1471-2105-14-281). Unfortunately dictionaries could not be shared for download, due to UMLS usage license. Nevertheless, keep in mind that **Disorder and Species entities were extended to include COVID-19 entities of interest**.

# Annotation
[Neji](https://github.com/BMDSoftware/neji) is the tool used for NER (Named Entity Recognition) and normalization, which is optimized for biomedical scientific articles and provides an easy to use CLI.
For more details please check the [article](https://doi.org/10.1186/1471-2105-14-281).

# Changelog
### 04-04-2020:
- CORD-19 annotated corpus.
### 28-03-2020:
- Initial release.
### 29-03-2020:
- Annotate "methods", "results" and "conclusions" sections from JSON files.

# Next steps
Possible next steps to improve the COVID-19 corpus:
- ~~Annotate "methods", "results" and "conclusions" sections from JSON files~~;
- Further optimize resources to target entities related with COVID-19;
- Include additional entities of relevance;
- ~~Annotate PMC and Elsevier full text articles~~;
- Collect co-occurrences to understand which entities might be related more often;
- Index articles and annotations and provide access to search tool.

# Contact
If you would like to know more or contribute, please send an e-mail to [david.marques.campos@gmail.com](mailto:david.marques.campos@gmail.com) or create a [ticket on GitHub](https://github.com/davidcampos/covid19-corpus/issues).

# License
The annotations and scripts are free to use and released under the [MIT license](LICENSE).