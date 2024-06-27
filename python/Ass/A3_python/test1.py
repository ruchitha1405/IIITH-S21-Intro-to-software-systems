import json
import csv

with open('rules.json', 'r') as jsonfile:
    rules_dict = json.load(jsonfile) 
    #print(rules_dict)
    #print(rules_dict[0]['fields'])      # parsing json string into python object
    with open('data.csv', 'r') as datafile:
        datacsvreader = csv.DictReader(datafile)
    
        with open('intermediate.csv', 'w') as intfile:
   
            fieldname = ['results']
            intermediatecsvwriter = csv.writer(intfile,fieldnames=fieldname)
            intermediatecsvwriter.writerow(fieldname)
            for line in datacsvreader:
                del line['email']
                del line['chronic']
                #print(line)
                for x in rules_dict:
                    y = x['fields']
                    #print(y)
                    if line['profession'] == y['profession'] :
                        if line['travel'] == y['travel'] :
                            if line['symptomatic'] == y['symptomatic'] :
                                del x['fields']
                                z= x.values()
                                intermediatecsvwriter.writerow(z)