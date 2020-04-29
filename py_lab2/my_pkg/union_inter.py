#!/usr/bin/python3

def calculate ():
    in1 = input('1st list: ')
    in2 = input('2nd list: ')
    list1 = in1.strip('[]').replace(' ', '').split(',')
    list2 = in2.strip('[]').replace(' ', '').split(',')
    set1 = set(list1)
    set2 = set(list2)

    uni = set1.union(set2)
    inter = set1.intersection(set2)

    uni_list = list(uni)
    inter_list = list(inter)

    uni_list_int = list(map(int, uni_list))
    inter_list_int = list(map(int, inter_list))

    uni_list_int.sort()
    inter_list_int.sort()
    
    print('=> union', uni_list_int)
    print('=> intersection', inter_list_int)

if __name__== '__main__':
    calculate()
