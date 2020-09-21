# the OS module allows you to interface with the underlying operating system
import os
# re — regular expression operations
import re

directory = '/var/lib/awx/wlc'

for filename in os.listdir(directory):
    if filename.startswith('in'):
        f = open(filename)
        # open a new file in append mode
        with open ('output.txt', 'a') as file:   
            for line in f:
                match = re.findall('ap+[a-zA-Z]+[a-zA-Z]+\S+\S', line)
                if match:
                    file.writelines(match)
                    file.write("\n")
        file.close()
