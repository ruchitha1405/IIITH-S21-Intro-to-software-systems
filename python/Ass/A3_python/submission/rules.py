import json
import csv


with open('intermediate.csv', 'w') as intfile:   # creating intermediate file
   
    fieldname = ['results']    # creating list of fieldnames in intfile
    intermediatecsvwriter = csv.DictWriter(intfile,fieldnames=fieldname) 
    intermediatecsvwriter.writeheader() # writing headers (field names)
    

    with open('data.csv', 'r') as datafile: # opening data.csv to read
        datacsvreader = csv.DictReader(datafile) # creating reader object
        for line in datacsvreader: # looping through the lines in data.csv
            del line['email'] # deleting email item 
            del line['chronic'] # deleting chronic item
            with open('rules.json', 'r') as jsonfile: # opening json file to read
                rules_dict = json.load(jsonfile)  # parsing json string into python object
                for x in rules_dict:  # looping through elements in rules_dict
                
                    if x['fields'] == line: # comparing the dictionaries
                        del x['fields'] # deleting fields item 
                        intermediatecsvwriter.writerow(x) # writing dictionary'x' into intfile
                        break   

       
            

