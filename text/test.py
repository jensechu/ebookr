import codecs

#Input filename
prompt = "Filename: "
z = raw_input(prompt)

#Extract text and close the file
book_open = codecs.open(z, "r+", "utf-8")
book = book_open.read()
book_open.close()

#Checks if file has already been ebooked.
def check(a):
    search = a.find("ebooked")    
    if search == -1:
        decoder(a)
        print "REPLACED YOUR STUFF"
    else:
        print "Your book has already been ebooked."

#LaTeX character replacements
def decoder(a):
    #Verifies check for future
    book_add = codecs.open(z, "a", "utf-8")
    book_add.write("% ebooked") 

    #Characters
    double = "'"

    #Replacement
    a = a.replace("'", "\\textquotedblleft{}")
    print a

    #Write new code to file
    book_open = codecs.open(z, "w", "utf-8")
    book_open.write(a)

check(book)
