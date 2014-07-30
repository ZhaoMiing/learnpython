#choose modules we'll use in this script
from sys import argv
#declear a variable named 'filename' in script to accept argument when it runs
script, filename = argv
#open the file and return a file object
txt = open(filename)
#get the file content as string
print "Here's your file %r:" % filename
print txt.read()
#get the user input use raw_input with a prompt "> "
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()