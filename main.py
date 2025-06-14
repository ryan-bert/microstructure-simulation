from sortedcontainers import SortedDict

dict = SortedDict()

dict[6] = "six"
dict[3] = "three"
dict[1] = "one"
dict[5] = "five"
dict[2] = "two"
dict[4] = "four"

del dict[3]

print(dict)