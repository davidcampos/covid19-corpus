#!/bin/bash
./venv/bin/python3.8 scripts/cord-19/annotate.py corpus/cord-19/raw/biorxiv_medrxiv corpus/cord-19/annotated/biorxiv_medrxiv
./venv/bin/python3.8 scripts/cord-19/annotate.py corpus/cord-19/raw/noncomm_use_subset corpus/cord-19/annotated/noncomm_use_subset
./venv/bin/python3.8 scripts/cord-19/annotate.py corpus/cord-19/raw/comm_use_subset corpus/cord-19/annotated/comm_use_subset
./venv/bin/python3.8 scripts/cord-19/annotate.py corpus/cord-19/raw/custom_license corpus/cord-19/annotated/custom_license

