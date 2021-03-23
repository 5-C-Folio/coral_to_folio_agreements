# coral_to_folio_agreements
## Purpose
### Takes coral resources from a CSV and will create a FOLIO agreements json file
## Requirements
1. Python 3.7x
2. SQL access to Coral server
3. Organizations must be loaded, with Coral relationship maintained via an org code

## Steps
1) Run sql query example: [Amherst Coral sql query](https://github.com/5-C-Folio/Coral-Queries/blob/master/amherst_resource.sql)  
Sql queries were customized for each schools specifications and how they used Coral Values
2) Output query results as CSV
3)  Edit agreementcreator.py. 
4) Modify org getter function for your data.  5 colleges included organization prefixes in FOLIO, but not in coral
5) Modify line 78 with your csv
6) modify get org parameter in line 75.  
5C has many orgs, so prefix was used to limit the results to the school being worked on
7) create credentials.json in the format 
{"userName": "[username]" ,  
"password": "[password]",  
"tenant": "[tenant]",  
  "URL": "[url]"} where values in brakets are the actual credentials
8) execute program

## Known issues
1)  This was intended to be a program used exclusively by me, for a one off task.  It doesn't have enough comments,too many hardcoded values,  
and is far more complicated in structure than it needs to be to do what it has to do
3)  I am not a developer and my understanding of object oriented programing is pretty low
4)  It was customized for the way Coral data is used in the three 5C servers.  It will require adaptation by anyone else
5) Notecreator.py was a proof of concept that we could attach Coral notes to Folio agreements.  It was a success, but NoteCreator will not work
