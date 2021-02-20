#Calls argv
from sys import argv

#ask for the filename in commandline
script, filename = argv

#asign an opened file to 'txt' variable
txt = open(filename)

print(f"Here's your file {filename}:")
#Put the content of filename into the prompt
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
