from sys import argv
import codecs, re, os

# Prompts for a file name if none is given.
if len(argv) != 2:
    file_name = raw_input("File name: ")
else:
    file_name = argv[1]


# Extract text and close the file
book_open = codecs.open(file_name, "r+", "utf-8")
book_read = book_open.read()
book_open.close()

# Checks if file has already been ebooked
def check(booked):
    search = booked.find("ebooked")    
    if search == -1:
        decoder(booked)
        print "REPLACED YOUR STUFF"
    else:
        print "Your book has already been ebooked."

# Creates a .pdf with LaTeX from the ebooked file_name
def create_tex(ebooked):
    print file_name
    os.system("pdflatex %s" % file_name)

# LaTeX character replacements
def decoder(book_new):
    # Adds the LaTeX preamble and closer to the book
    latex_preamble = '''
\documentclass[12pt]{book} \n \n

%Packages \n
\usepackage[usenames,dvipsnames]{color} \n
\usepackage[top=1.5in, bottom=1.5in, left=1.75in, right=1.75in]{geometry} \n
\usepackage[utf8]{inputenc} \n \n

%Book Properties\n
\linespread{1.3} \n\n

%Begin
\\begin{document} \n

%Centers the page number
\pagestyle{plain}

%Deletes extra pages 
\let\cleardoublepage\clearpage

'''
    book_tex = latex_preamble + book_new + "\n \end{document}"

    # Replace double quotes
    double_quotes = re.compile(r'"(.+?)"', re.MULTILINE | re.DOTALL)
    book_tex = double_quotes.sub(r'\\textquotedblleft \\textquotedblright \\textcolor{White}{a} ', book_tex)

    # Write new code to file
    book_open = codecs.open(file_name, "w", "utf-8")
    book_open.write(book_tex)

    # Makes it false for the check() next time
    book_add = codecs.open(file_name, "a", "utf-8")
    book_add.write("% ebooked") 

check(book_read)
create_tex(file_name)
