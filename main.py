from os import popen as system
from sys import argv
def get_var():
    out = system("python Execute\\scan.py " + argv[1])
    global ips
    ips = ((out.read()).split("\n"))
def edit():
    global ips
    for i in range(0,4):
        ips.pop(0)
    for i in range(0,len(ips)):
        ips[i] = ips[i].split()
    ips.pop(len(ips)-1)
def main():
    get_var()
    edit()
    global ips
    for i in ips:
        print(i[0] + " " + i[1] + " " + i[2])
main()
