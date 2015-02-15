import sys
import requests
import re


# Parses all urls and returns a sorted list of all found email addresses.
def find_addresses(urls):
    addresses = []
    for url in urls:
        response = requests.get(url)
        txt = response.text
        found_addresses = re.findall(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\b', txt)
        for address in found_addresses:
            if address not in addresses:
                addresses.append(address)
    return sorted(addresses)


if __name__ == "__main__":
    urls = sys.argv[1:]
    email_addresses = find_addresses(urls)
    for address in email_addresses:
        sys.stdout.write(address + '\n')
    print "Found {0} unique email addresses!".format(len(email_addresses))




