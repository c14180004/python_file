import os

## CHECK FILE ###
if os.path.exists("demofile.txt"):
  print("The file exist")
else:
  print("The file does not exist")

## MODE ##
## 'r'	Open file for reading. This is the default mode. 

## 'w'	Open file for writing. Starts writing at the beginning of file. 
###### File pointer at the beginning of the file. Overwrite existing File.

## 'a'	Open file in append mode. Starts writing at the end of file.
###### File pointer at the end of the file

##  For 'w' and 'a' : If file does not exist, it creates a new file.

## '+'	This will open a file for reading and writing (updating). example : r+, a+, w+

## 'r+' Open for reading and writing. The stream is positioned at the beginning of the file.

## 'w+' Open for reading and writing. The file is created if it does not exist,
##### otherwise it is truncated. The stream is positioned at the beginning of the file.

## 'a+' Open for reading and writing in append mode. The file is created if it does not  
#####  exist.  The stream is positioned at the end of the file.

## 't'	This is the default mode. It opens in text mode. example : rt, at, wt
## 'b'	This opens in binary mode. example : rb, ab, wb

### OPEN FILE ###
file_object  = open("filename", "mode") <-#SYNTAX

### CLOSE FILE ###
file_object.close() <-#SYNTAX
## This will close the instance of the file file_object stored
file=open("test1.txt","r")
print('Is the file closed?:', file.closed) # Check whether file is closed
file.close()
print('Is the file closed?:', file.closed) # Check whether file is closed

## OPEN AND CLOSE FILE ##

#with open("test1.txt") as file:
    print("Name of the file:",file.name)
    print("Mode of the file:",file.mode)
    file.close()
print("Closed?",file.closed)


## READ FILE ##
##read([n])
##readline([n])
##readlines()

## n is the number of bytes to be read, if empty will read all

## READ ##
my_file=open("test1.txt","r")
print(my_file.read())
print(my_file.read(20)) ## print 20 bytes
my_file.close()

## READ LINE ##
my_file=open("test1.txt","r")

#my_file.readline()
print(my_file.readline())
print(my_file.readline(5))
outputs first two characters of next line

## READLINES
print(my_file.readlines())

### READ LINE WITH FOR LOOP
for line in my_file:
    print(line)

my_file.close()


## WRITE ##
new_file=open("newfile.txt","w")

new_file.write("Writing to a new file\n")
new_file.write("Writing to a new file\n")
new_file.write("Writing to a new file\n")

for i in range(10):
    new_file.write("This is line %d\n" %(i+1))

# WRITE LINES ##
shapes=["kotak\n","bulat\n","segitiga\n"]
new_file.writelines(shapes)

new_file.close()

## APPEND ##
fruits=["Orange\n","Banana\n","Apple\n"]
file=open("newfile.txt",mode="a+")
file.writelines(fruits)
file.close()



### CLASS ### STRUCTURE WRITING TO FILE
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def pprint(self):
    print(self.name, self.age)


ListPeople=[Person("Jennifer", 21), Person("John", 36), Person("Jane", 26),Person("Blake", 46)]

for people in ListMahasiswa:
    people.pprint()

new_people=[Person("Janet", 27), Person("Agni", 28)]

f = open("people.txt", "w+")
for people in new_people:
    f.write(people.name+","+str(people.age)+"\n")
f.close()


file = open("people.txt", "r+")
for line in file:
    data = line.split(",")
    ListPeople.append(Person(data[0], int(data[1])))
file.close()

for people in ListPeople:
    people.pprint()












