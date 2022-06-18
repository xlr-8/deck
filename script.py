#!/usr/env/bin python
#
# Small script used to generate latex/pdf file based on a CSV file.
# This CSV file must contain a certain amount of columns in a specific
# order, to be able to substitute each variable properly in each card.
#

import csv

# The overall structure of the tex file is split into 3 elements:
# - the header: containing all packages, structure definition, etc
# - the card: which will be generated for each entry of the CSV file
# - the end: which will basically close the document

header = r'''
\documentclass[grid,avery5371,landscape]{flashcards}

\usepackage[T1]{fontenc}
\usepackage[sfdefault,semibold,scaled=.85]{FiraSans}
\usepackage{graphicx}
\usepackage{newtxsf}
\usepackage{xcolor}
\usepackage{calc}
\usepackage{geometry}
\usepackage{enumitem}

\geometry{a4paper,portrait}

\renewcommand{\cardpaper}{a4paper}
\renewcommand{\cardpapermode}{landscape}
\renewcommand{\cardrows}{4}
\renewcommand{\cardcolumns}{2}
\setlength{\cardheight}{54mm-2\fboxrule}
\setlength{\cardwidth}{85mm-2\fboxrule}
\setlength{\topoffset}{0mm}
\setlength{\oddoffset}{0.0mm}
\setlength{\evenoffset}{0.0mm}
\setlength{\cardmargin}{2.5mm}
\setlength{\fboxrule}{2.5mm}


\cardfrontstyle[\raggedright\large\color{black}]{headings}
\cardbackstyle[\raggedright\small\color{black}]{plain}
\cardfrontheadstyle[\small\color{black}]{left}
\newcounter{nocarte}
\newcommand{\categ}[1]{%
  \def\@categ{#1}%
  \setcounter{nocarte}{0}%
}
\cardfrontfoot{\textcolor{black}{\@categ --\refstepcounter{nocarte} \thenocarte}}
\cardfrontfootstyle[\small]{right}


\setlist[itemize]{label=$\bullet$,labelindent=0em,labelsep=1ex,leftmargin=*,labelwidth=1em,itemsep=0mm}

\newcommand{\source}[1]{%
  \medskip
  \itshape%
   ~ \hfill Réf. : #1}

\begin{document}
'''

card = r'''
\color[HTML]{%color%}
\categ{%category%}
\begin{flashcard}[%type%]{
 %question%   }
  %answer%
  \source{%reference%}
\end{flashcard}
'''

end = r'''
\end{document}
'''

colors = {
        "CE-CP-REG": "01DF01",  # green
        "PSE+": "FF6D01",       # orange
        "PSE": "003273",        # blue
        "TECH": "01DFA5",       # turquoise
}

print(header)
with open('flashcard.csv', 'rt', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, quotechar='"', delimiter=';')
    # Skip first line as it's headers
    next(reader, None)
    for row in reader:
        new_card = card

        # By default the color red is selected, if the category found
        # matches the known ones then we switch the color to that one
        color = "FF0000"
        if row[0] in colors:
            color = colors[row[0]]

        # Proceed to replace every variable from the card with the
        # respective values of the column from the CSV file
        new_card = new_card.replace("%category%", row[0])
        new_card = new_card.replace("%color%", color)
        new_card = new_card.replace("%type%", row[1])
        new_card = new_card.replace("%date%", row[2])
        new_card = new_card.replace("%question%", row[3])
        new_card = new_card.replace("%answer%", row[4])
        new_card = new_card.replace("%reference%", row[5])
        print(new_card)
print(end)
