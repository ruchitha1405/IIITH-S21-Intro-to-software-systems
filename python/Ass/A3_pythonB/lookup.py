import csv
#rows=[]
#fields=[]
with open('data.csv', 'r') as datafile: # opening data.csv to read
    datacsvreader = csv.reader(datafile) # creating reader object
    fields = next(datacsvreader) # returns fieldnames list
    fields.remove("status") #remove status from fieldnames list
    with open('intermediate.csv', 'r') as intfile: # opening intermediate.csv to read
        intcsvreader = csv.reader(intfile) # creating reader object
        field = next(intcsvreader)  # returns fieldnames list
        fields.extend(field) # merges the two fieldnames lists
        with open('results.csv', 'w') as resultfile:# creating results.csv to write
            resultcsvwriter = csv.writer(resultfile)# creating writer object
            resultcsvwriter.writerow(fields) # writing headers (field names)

            for line in datacsvreader:  # looping through the lines in data.csv
                risklevel= next(intcsvreader) # returns the current row as a list and advances the iterator to the next row in intfile 
                del line[5] # delete status from line
                line.extend(risklevel) # merges two lists
                resultcsvwriter.writerow(line) # writes the merged list into results.csv as a row