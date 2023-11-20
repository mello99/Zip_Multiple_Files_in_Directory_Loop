import itertools
import os
import re
import sys
import zipfile

# Split them into chunks, produce these chunks using code, THEN ZIP THEM
# Could use Regex, or slicing, or split() function on each string name, then zip them

groups = {}
#print all files in directory 
for filename in os.listdir("."):
    if filename.endswith('.jpg'):
        group = "SC_ENLACE_finances_" + filename.split("_")[3]
        print(filename, group)
        if group not in groups: # if the group doesn't exist in the dictionary (key-val-pair), make an empty group
        	groups[group] = []
        groups[group].append(filename)


for k, v in groups.items(): #This block processes one group: for each group, process that group
    zip_file_name = k + '.zip' # setting up a key
    with zipfile.ZipFile(zip_file_name, mode='w') as zf: #opening zip
        for file in v: # looping over all files for this group
            zf.write(file) # writes each one
    print(k, v)


#print(r"C:\Users\...\SC_ENLACE_board\jpg")
#itertools "groupby" 
#dictionary
#print multiple things, separate by commas
