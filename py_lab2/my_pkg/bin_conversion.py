#!/usr/bin/python3

def converse ():
    b = input("input binary number: ")
    b_string = '0b' + b
    result = "OCT> {0:o}\nDEC> {0:d}\nHEX> {0:x}".format(int(b_string, 2))
    print(result)

if __name__=="__main__":
    converse()
