# re — regular expression operations
import re

f = open("/var/lib/awx/wlc/input.txt", "r")
    # open a new file in write mode so that the file will be overwritten and not appended
with open ('/var/lib/awx/wlc/output.csv', 'w') as file:   
    for line in f:
        match = re.findall('ap+[a-zA-Z]+[a-zA-Z]+\S+\S', line)
        if match:
            file.writelines(match)
            file.write("\n")
file.close()
