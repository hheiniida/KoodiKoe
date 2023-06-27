import sys
from operator import itemgetter

# Get the filename from command line arguments
filename = input("Give the file name: ")

# Open the file for reading
with open(filename, 'r') as file:
    # Read the entire file contents
        contents=file.read()
        print(contents)


#ask operation
operation = input("Select an operation: 1) Add new book, 2) Print current database content in ascending order by publishing year or Q) Exit the program: ")

#1)add new book
if operation=="1":
    #ask information
    bookname=input("Name of the book: ")
    writer=input("Writer of the book: ")
    ISBN=input("ISBN: ")
    year=input("Publishing year: ")
    book=bookname + "/"+ writer +"/"+  ISBN +"/"+ year
    with open(filename, "a") as file:
        file.write("\n"+book)

#2) print current db
if operation=="2":
    #open file
    with open(filename, 'r') as file:
        sorted_by_year=[]

        #Strips the newline character
        for line in file:
            parts = line.split("/")
            my_dictionary={}
            my_dictionary['name']=parts[0]
            my_dictionary['writer']=parts[1]
            my_dictionary['isbn']=parts[2]
            my_dictionary['year']=parts[3]
            sorted_by_year.append(my_dictionary)

        newlist = sorted(sorted_by_year, key=itemgetter('year')) 
           
        print(newlist)  
          

#Q)exit the program
if operation=="Q":        
     quit