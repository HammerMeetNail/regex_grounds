import sys
import requests
import re


# Parses all urls and returns a sorted list of all found email addresses.
def find_usernames(urls):
    names = []
    names_lower = []
    for url in urls:
        response = requests.get(url)
        txt = response.text
        found_names = re.findall(r'@[a-zA-Z0-9_]+\b', txt)
        for name in found_names:
            if name not in names and name.lower() not in names_lower:
                names.append(name)
                names_lower.append(name.lower())
    return sorted(names)


if __name__ == "__main__":
    urls = sys.argv[1:]
    usernames = find_usernames(urls)
    for name in usernames:
        sys.stdout.write(name + '\n')
    print "Found {0} unique usernames!".format(len(usernames))




