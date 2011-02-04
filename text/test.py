import codecs
import re

#Input filename
prompt = "Filename: "
file_name = raw_input(prompt)

#Extract text and close the file
book_open = codecs.open(file_name, "r+", "utf-8")
book_read = book_open.read()
book_open.close()



#Checks if file has already been ebooked.
def check(booked):
    search = booked.find("ebooked")    
    if search == -1:
        decoder(booked)
        print "REPLACED YOUR STUFF"
    else:
        print "Your book has already been ebooked."



#LaTeX character replacements
def decoder(book_new):
    #Replace double quotes
    double_quotes = re.compile(r'"(.+?)"', re.MULTILINE | re.DOTALL)
    book_new = double_quotes.sub(r'\\textquotedblleft \1\\textquotedblright \\textcolor{White}{a} ', book_new)

    #Write new code to file
    book_open = codecs.open(file_name, "w", "utf-8")
    book_open.write(book_new)

    #Makes it false for the check() next time
    book_add = codecs.open(file_name, "a", "utf-8")
    book_add.write("% ebooked") 

check(book_read)
