#!/usr/bin/python3
from my_pkg.bin_conversion import *
from my_pkg.union_inter import *

while True:    
    menu = int(input('Select menu: 1) conversion 2) union/intersection 3) exit ? '))
    if menu == 1:
        converse()
    elif menu == 2:
        calculate()
    elif menu == 3:
        print("exit the program...")
        break
