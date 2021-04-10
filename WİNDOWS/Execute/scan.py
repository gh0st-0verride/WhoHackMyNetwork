import scapy.all as scapy
import re
from sys import argv
def scan(ip_range):
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    while True:
        ip_add_range_entered = ip_range
        if ip_add_range_pattern.search(ip_add_range_entered):
            break
    arp_result = scapy.arping(ip_add_range_entered)
def get_range():
    try:
        res = argv[1]
    except:
        print("null")
    return res
def main():
    scan(get_range())
main()
