#!/usr/bin/python3

n = int(input("input count of number: "))
nums = []

for i in range(0, n):
    num = int(input("input the "+str(i+1)+"th number: "))
    nums.append(num)

total = 0
for num in nums:
    total += num

average = total / n
print("average: {}".format(average))
