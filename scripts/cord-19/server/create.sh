#!/bin/bash
cwd=$(pwd)
projectFolder=$cwd
pubmedFolder=$projectFolder/corpus/pubmed
nejiFolder=$projectFolder/tools/neji-2.0.2/
dictionariesFolder="$projectFolder/resources/dictionaries"
modelsFolder="$projectFolder/resources/models"
threads=5

cd "$nejiFolder" || return
rm -rf "$pubmedFolder/annotations"
mkdir "$pubmedFolder/annotations"
./neji.sh -i "$pubmedFolder/raw" -if RAW -o "$pubmedFolder/annotations" -of A1 -d "$dictionariesFolder" -m "$modelsFolder" -t $threads -s
