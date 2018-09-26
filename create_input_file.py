#create a file handler
file = open("data.csv", "w")

#write some things to our file
file.write("name_first,name_last\n")
file.write("Homer,Simpson\n")
file.write("Marge,Simpson\n")
file.write("Bart,Simpson\n")
file.write("Lisa,Simpson\n")
file.write("Maggie,Simpson\n")
file.write("Ned,Flanders\n")
file.write("Maude,Flanders\n")
file.write("Rod,Flanders\n")
file.write("Todd,Flanders\n")

#close the file
file.close()