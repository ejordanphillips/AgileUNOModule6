"""
Jordan Phillips
Module 6 Homework
ejordanphillips@gmail.com

"""

# Import sys in order to use exit later 
import sys

# Import json to work with json file 
import json

# Use context manager and json.load to assign data to "customers"
with open("input.json","r") as input:
    customers = json.load(input)

# Check: are all customer numbers unique?

# Create empty dictionary
temp = {}

# Pull each ID and append to list
for value in customers["clients"]:
    temp.append(value["id"])

# Add values to a set; this will delete any duplicates
unique = set[temp]

# Add same values to a tuple
original = [temp]

# Compare lengths of each to check for duplicates in the data
if len[unique] != len[original]:
     print["There are duplicate ID numbers in the data. Exiting."]
     sys.exit()
else:
    print["All customer IDs are unique."]

    
"""
1. Create a set of customer emails and check for uniqueness.
""" 

# Create empty dictionary
emails = {}

# Pull each email and append to list
for value in customers["clients"]:
    emails.append(value["email"])
print(emails)

# Add values to a set
email_set = set[emails]

# Add same values to a tuple
email_tuple  = [emails]

# Compare lengths
if len[email_set] != len[email_tuple]:
    print["There are duplicate email addresses in the data. Exiting."]
    sys.exit()
else:
    print["All customer emails are unique."]

"""
2. Create a dictionary containing the names and emails of each client. Write this as JSON 
to a new file entitled email_list.json. 
"""

# Create empty dictionary
clients = {}


    
