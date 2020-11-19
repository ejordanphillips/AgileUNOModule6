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
with open("input.json","r") as infile:
    customers = json.load(infile)

# Check: are all customer numbers unique?

# Create empty list
temp = []

# Pull each ID and append to list

for client in customers["clients"]:
    temp.append(client["id"])
    print(temp)

# Add values to a set; this will delete any duplicates
unique = set(temp)

# Add same values to a tuple
original = (temp)

# Compare lengths of each to check for duplicates in the data
if len(unique) != len(original):
     print("There are duplicate ID numbers in the data. Exiting.")
     sys.exit()
else:
    print("All customer IDs are unique.")

    
"""
1. Create a set of customer emails and check for uniqueness.
""" 

# Create empty list
emails = []

# Pull each email and append to list
for client in customers["clients"]:
    emails.append(client["email"])
    print(emails)

# Add values to a set
email_set = set(emails)

# Add same values to a tuple
email_tuple  = (emails)

# Compare lengths
if len(email_set) != len(email_tuple):
    print("There are duplicate email addresses in the data.")
else:
    print("All customer emails are unique.")

"""
2. Create a dictionary containing the names and emails of each client. Write this as JSON 
to a new file entitled email_list.json. 
"""

# Create empty dictionary
email_list = {}

for client in customers["clients"]:
    email_list[client["name"]] = client["email"]
    
with open("email_list.json", "w") as outfile:
    json.dump(email_list, outfile)


"""
3. Set each male customer's active status to false. Write this new data to a file called 
current_customers.json  
"""

for client in customers["clients"]:
    if client["gender"] == "male":
        client["isActive"] = False

with open("current_customers.json", "w") as outfile:
    json.dump(customers, outfile)

sys.exit()
