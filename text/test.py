import codecs

#Input filename
prompt = "Filename: "
z = raw_input(prompt)

#Get text and create new file
old_open = codecs.open(z, "r+", "utf-8")
old = old_open.read()
new = "new_" + z

def decoder(a):
    single = "'"
    for x in a:
        if x == single:
            a = a.replace("'", "J")

    #Still prints mutliple copies due to for statement
    new_open = open(new, "r+")
    t = new_open.write(a)
    

decoder(old)
