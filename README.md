# Deck

## Requirements

Python 3.x, Latex (and associated packages of style, graphics, etc) installed

## Usage

By default you need to have the CSV file named: flashcard.csv - as it will be this one that will be read.

Generate the file.pdf
```bash
> python3 script-v2.py > file.tex && pdflatex file.tex
> evince file.pdf # Or your favorite pdf reader
```
