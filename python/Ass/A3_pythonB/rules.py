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
            del line['status'] # deleting status item
            with open('rules.json', 'r') as jsonfile: # opening json file to read
                rules_dict = json.load(jsonfile)  # parsing json string into python object
                
                flag=0
                for x in rules_dict:  # looping through elements in rules_dict
                    
                    if x['fields'] == line: # comparing the dictionaries
                        if x['status']== "Active" :
                            del x['fields'] # deleting fields item 
                            del x['status'] # deleting status item
                            intermediatecsvwriter.writerow(x) # writing dictionary'x' into intfile
                            flag=1 #flag will update to 1 to indicate that result tag is found
                            break   
                        else:
                            continue
                    else:
                        continue
                if flag==0 : # flag==0 means either we didn't the rule combination or the status of the rulecombination is inactive
                    intermediatecsvwriter.writerow({"results": "No Access"})
                else :
                    continue