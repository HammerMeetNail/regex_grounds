'''
For use in conjunction with NetResViewer, seperates computer names from file
Accepts files containing strings in the following format:
\\Server-Name\ADMIN$,Admin Share,Domain,Remote Admin,C:\Windows,Microsoft Windows Network,0,5.02,Windows 7,,,,
'''
import re
import sys


# Accepts lines of comma delimited strings, splits strings by comma
def split_resources(resources):
    with open(resources, 'r') as f:
        data = f.readlines()
    split = [line.split(',') for line in data]
    return split

# Parses first value in split_resources list and returns computer name
def grab_resources(split_resources):
    comps = []
    for x in split_resources:
        r = re.search(r'([\w|-]+\d{0,10})', x[0])
        if r.groups()[0] not in comps:
            comps.append(r.groups()[0])
    return comps


# input is path to file containing comma delimited strings of network resources
if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    split_data = split_resources(input)
    computers = grab_resources(split_data)
    with open(output, 'w') as f:
        for computer in computers:
            f.write(computer + '\n')
