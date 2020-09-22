# re — regular expression operations
import re

f = open("/var/lib/awx/wlc/input.txt", "r")
    # open a new file in append mode
with open ('/var/lib/awx/wlc/output.csv', 'w') as file:   
    for line in f:
        match = re.findall('ap+[a-zA-Z]+[a-zA-Z]+\S+\S', line)
        if match:
            file.writelines(match)
            file.write("\n")
file.close()
