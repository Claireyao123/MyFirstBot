start = 10
end = 15
number = 10000

#  number - 10 - 11 - 12 - 13.... - 15

#  number - 10
#  number - 11

for i in range(start, end + 1):
    number = number - i
print(number)


# 7:  i = 10
# 8:  l = 10000 - 10   l:9990
# 7:  i = 11
# 8:  l = 10000 - 11   l:9989
# .....
# 7:  i = 15
# 8:  l = 10000 - 15   l:9985

#  10 + ... +15 = 75
# 10000 - 75 = 9925
# n = 0
# for i in range(start,end+1):
#     n = n + i
# print(n)
