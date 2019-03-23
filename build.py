import sys
import os
from os import listdir
from os.path import isfile, join
from subprocess import call
import datetime
import socket
import re

def print_usage():
    
    print("Build Tool for SoundsOutOfBounds \"Rolling Release\"")
    print("Usage: " + sys.argv[0] + " [--jokes] [--footnotes] <selection>")
    print("  --jokes      Include terrible German jokes and puns as fillers on some pages")
    print("  --footnotes  Include footnotes (in German) explaining some of the lyrics' details")
    print("  <selection>  List of numbers corresponding to the songs to include, in that order")
    print("               0: Include all songs")
    print("               Pos. number: Include the song of that index (see list below)")
    print("               Neg. number: Exclude the song of that index")
    print("Examples:")
    print("  python3 " + sys.argv[0] + " 0")
    print("    => All songs in alphabetical order")
    print("  python3 " + sys.argv[0] + " 1 2 4 6 9 12 13 14 16 17 5 18 23")
    print("    => Some custom selection, ordered such that long songs are on double pages")
    print("  python3 " + sys.argv[0] + " 0 -2 -5 -11 -22")
    print("    => All songs except for #2, #5, #11, #22")
    print()
    
    # List all available songs
    print("All songs:")
    for i in range(1, len(songfiles)+1):
        print("%i:\t%s" % (i, songnames[i-1]))
    

# Fetch all songs
songfiles = [f for f in listdir("songs/") if str(f).endswith(".tex")]
songfiles.sort()
songnames = [str(f).replace(".tex", "") for f in songfiles]

# Check arguments
if len(sys.argv) <= 1:
    print_usage()
    exit()

else:

    # Configuration
    picked_songfiles = []
    include_jokes = False
    include_footnotes = False
    
    # Parse configuration from arguments
    for arg in sys.argv[1:]:
        if "--jokes" in arg:
            include_jokes = True
            continue
        if "--footnotes" in arg:
            include_footnotes = True
            continue
        i = int(arg)
        if i == 0:
            # Select all songs
            for song in songfiles:
                if song not in picked_songfiles:
                    picked_songfiles += [song]
        elif i < 0:
            # Exclude a song
            idx = 0
            while idx < len(picked_songfiles):
                if picked_songfiles[idx] == songfiles[-i-1]:
                    del picked_songfiles[idx]
                else:
                    idx += 1
        else:
            # Include a song
            if songfiles[i-1] not in picked_songfiles:
                picked_songfiles += [songfiles[i-1]]
    print("Chosen songs: " + str(picked_songfiles))
    
    # Substitutions in the main.tex and preamble_rr.tex files
    aliases = [["%INCLUDE_DATE", datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")], 
               ["%INCLUDE_HOST", socket.gethostname()], 
               ["%INCLUDE_SCRIPTNAME", sys.argv[0]],
               [".pdf", "_rr.pdf"]]
    # Remove some elements by redefining the respective command
    if not include_jokes:
        aliases += [["\\newcommand\\joke", "\\newcommand\\joke[1]{} \\newcommand\\nojokeever"]]
    if not include_footnotes:
        aliases += [["%INCLUDE_CUSTOM_CMDS", "\\renewcommand{\\footnote}[1]{}\n"]]
    
    # Write new main.tex with selected songs
    outfile = open("main_selection.tex", "w")
    for line in open("main.tex", "r").readlines():
        # Include modified preamble
        if "%INCLUDE_PREAMBLE" in line:
            for preamble_line in open("preamble_rr.tex", "r"):
                for alias in aliases:
                    preamble_line = preamble_line.replace(alias[0], alias[1])
                outfile.write(preamble_line)
        # Include selected songs
        if "%INCLUDE_SONGS" in line:
            for songfile in picked_songfiles:
                outfile.write("\input{songs/" + str(songfile) + "}\n\n")
        # Include usual lines (but no explicit tex includes)
        if not re.search(r"\\input\{.*\.tex\}", line):
            for alias in aliases:
                line = line.replace(alias[0], alias[1])
            outfile.write(line)
    outfile.close()
    
    # Compile twice because of table of contents
    for i in range(2):
        call(["pdflatex","-synctex=1","-interaction=nonstopmode","main_selection.tex"])
    
    # Move output file, delete working files
    os.rename("main_selection.pdf", "out.pdf")
    #for f in listdir("./"):
    #    if str(f).startswith("main_selection."):
    #        os.remove(f)
    
    print("Output written to out.pdf.")
