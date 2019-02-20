import os

os.system('clear')

print("\n******************** Variables ******************************")

var = 3
var2 = 2.234
var3 = "Hello"

#print multiple values
print("Different variable types {a} {q} {w}".format(a=var, q=var2, w=var3))

print("\n******************** List ******************************")

'''multiple comments here'''
#single comment here

#list is ordered, not sorted
list = [77,99,88,66]
print("List: {}".format(list))

list.append(1)
print("List append 1: {}".format(list))

list.remove(88)
print("List remove 88: {}".format(list))

list.sort()
print("List sorted: {}".format(list))

print("List length {}".format(len(list)))

#comprehensive list creation
list2 = [x for x in range(5) if(x % 2 != 0)]
print("comprehensive list example even:{}".format(list2))
list2 = [x for x in range(5) if(x % 2 == 0)]
print("comprehensive list example odd:{}".format(list2))

#intersection, union and diff of two lists
list1 = [1,2,3,9]
list2 = [4,5,6,9]

print("list union: {}".format(set(list1).union(list2)))
print("list intersection: {}".format(set(list1).intersection(list2)))
print("list diff: {}".format(set(list1).difference(list2)))

print("\n******************** set ******************************")

#sets not ordered, no duplication
set = {1,2,3,4,5,6}
print("set example: {}".format(set))

set.add(-1)
print("set add -1: {}".format(set))

set.add(6)
print("set duplicate value 6: {}".format(set))

set.remove(4)
print("set remove element 4: {}".format(set))

print("\n******************** triplets ******************************")

#triplets => immutable
tripet = (1,2,3)
print("Triplet example: {}".format(tripet))

#tripet.add(7); this is not allowed
tripet = tripet + (4,5,6)
print("Add more to the triplet: {} ".format(tripet))

#add only one element to the triplet
tripet = tripet + (7,)
print("Add single item to the triplet: {} ".format(tripet))

print("\n******************** String and Input ******************************")
#string trim
test = "   ----welcome----   "
test = test.strip()
print("String strip {}".format(test))
test = test.lstrip('-')
print("String lstrip {}".format(test))
test = test.rstrip('-')
print("String rstrip {}".format(test))
print("String upper {}".format(test.upper()))
print("String lower {}".format(test.lower()))
test = "Italy,Spain,France,UK,BRUGGE"
test_split = test.split(",")

'''
for string in test_split:
	print("string from test string {} ".format(string))
'''
print("test split:{}".format(test_split))

user = raw_input("enter a name: ")

if user in test_split:
	print("In the list")
else:
	print("Not in the list")

print("\n******************** Dictionary ******************************")

#Dict: is similar to HashMap in Java (key-value) pair


