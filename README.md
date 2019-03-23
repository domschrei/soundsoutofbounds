# Sounds Out Of Bounds - Re-usable Song Modules

**[Download Original Edition PDF](https://github.com/domschrei/soundsoutofbounds/releases/download/1.0.3/SoundsOutOfBounds_V1.0.3.pdf)**

This songbook was originally created at the University of Stuttgart and intended to be a successor to previous songbooks *Chor Dump* and *Chor Dump 2* about computer science and IT, which were written by former students.
It featured more than 20 song texts about IT, computer science and software engineering, also referencing many topics for "end users".
Since then, new songs are added to the project from time to time.

Each song text is based on some popular pop song in terms of melody and phrasing. The adapted lyrics are original content.
A few songs are written in German, but the majority is in English.

The contents of this book may be distributed and used according to the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

## Songs

These songs are featured in the printed Original Edition:

* Alles in der Cloud (orig. "Alles nur geklaut")
* A New PC (orig. "Everything At Once")
* Another Byte In The Code (orig. "Another Brick In The Wall")
* Another Day In Tech Support (orig. "Another Day In Paradise")
* Applaus, Applaus
* Branching Tree (orig. "Lemon Tree")
* Codefinger (orig. "Goldfinger")
* Commit The Code, Jack (orig. "Hit The Road, Jack")
* Firewall (orig. "Wonderwall")
* Gamer (orig. "Bitch")
* Mad World
* Never Gonna Push You Up (orig. "Never Gonna Give You Up")
* Overflow (Security Regrets) (orig. "Let Her Go")
* Python (orig. "Angels")
* Smombie (orig. "Zombie")
* That's What Math Is For (orig. "That's What Friends Are For")
* The Final Countdown
* Tux, The Magic Penguin (orig. "Puff, The Magic Dragon")
* Word User Trying TeX (orig. "Englishman In New York")
* You Are The Best Phone (orig. "You Are Sunshine Of My Life")
* Bonus I: Kunst am Bau (orig. "What A Wonderful World")
* Bonus II: Volker Claus (orig. "Annabell, ach Annabell")

The following songs have been added afterwards:

* Make It Slow (orig. "Let It Go")
* Learning In The Deep (orig. "Rolling In The Deep")

## Getting a PDF

There are the following ways to get a PDF copy of SoundsOutOfBounds:

The PDF of the Original Edition as it has been printed back in 2016 can be downloaded [here](https://github.com/domschrei/soundsoutofbounds/releases/download/1.0.3/SoundsOutOfBounds_V1.0.3.pdf).

This PDF, with minor corrections, can also be compiled from sources using PdfLatex (as long as the needed packages are available):

`pdflatex -synctex=1 -interaction=nonstopmode main.tex`

To build a custom PDF with the songs you like, consult the script `build.py` (Python 3 required). Calling it without any parameters will provide detailed instructions on how to build the songbook exactly as you want.
