#!/bin/env python
import re


def extract_ip(line):
    ip_pattern = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]\.)+" * 3 + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])+"
    match = re.search(ip_pattern,line)
    if match:
        print(f'0: {match.group(0)}') # return the full match
        print(f'1: {match.group(1)}') # return the match of the first pattern within the overall pattern
        print(f'2: {match.group(2)}')
        print(f'3: {match.group(3)}')
        print(f'4: {match.group(4)}')
        return match.group(0)
    else:
        return "no match"

def extract_ips(file):
    ''' example based on findall shows that with below regex we obtain not only the full pattern match but all individual components as a tuple
    hence the need to extract a new list that only keeps each full match '''

    byte = r"25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]"
    ip_pattern = r"(" + (r"(%s)\." % byte) * 3 + r"(%s))+" % byte
    #print(ip_pattern)
    all_matches = re.findall(ip_pattern, file)
    matches = [ x[0] for x in all_matches ]
    return matches

if __name__ == "__main__":
    with open('Test_Driven_Development/ip_addresses.txt', 'r') as f_read:
        lines = f_read.read()
    for line in lines:
        print(f'line: {line}\nIP= {extract_ip(line.strip())}')
    print(f'all ip\'s {extract_ips(lines)}')

