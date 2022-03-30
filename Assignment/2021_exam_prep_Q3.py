############### Question 3 #################
"""
Remember the comment your solution with logical comments and comments describing the
programming constructs. This will be weighted heavily.
See the skeleton code relating to this question. The file details.txt contains rows of
information formatted as tuples, each tuple has 3 elements, which are user_id, user_name,
and user_address. Note: multiple rows for the same user_id, user_name will contain
different user_address. A sample of the formatting of the document text is shown.
(765, "Maurice Murphy", "space address 1")
(865, "Mike Smith", "home address 2")
(825, "Sinead Crotty", "home address 2")
(765, "Maurice Murphy", "space address 2")

Write a function read_file(input_file) that will read in the content of the input file, and
create a dictionary Users with user_id as the key (integer) and a list of user_name and
user_address(s) as the dictionary value. The function read_file will return this dictionary and it
will be printed.

Expected output:
{765 : ["Maurice Murphy", "space address 1", "space address 2"], 865: ["Mike Smith", "home address 2"], 825: ["Sinead Crotty", "home address 2"]}
"""

def read_file (input_file):
    Users = {}
    #Your code goes here
    
    with open (input_file, 'r') as inFile:
    
        for line in inFile:
            
            line = line.strip('(').strip(')').strip('\n').replace('"', " ").replace(')','').split(",")
            
            print(line)
            
            if int(line[0]) not in Users:
                Users [ int(line[0]) ] = line[1:]
            # else:
            #     Users [ int(line[0]) ] = line.append(line[:2])

    return Users

print(read_file ("details.txt"))