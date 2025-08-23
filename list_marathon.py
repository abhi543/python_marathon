'''lis1=[1,2,3,4]
lis2=[5,6,7,8] concatenate list using +
lis3=lis1+lis2
print(lis3)

#Find the second largest number in a list.
numbers = list(range(1, 21))
unique_numbers=list(set(numbers))
unique_numbers.sort(reverse=True)
if len(unique_numbers)>=2:
    print("second largest:",unique_numbers[1])
else:
    print("no second largest exists")

#Create a list of words and sort them in alphabetical order.
list=['team','hyper','ena','cat','xlm']
list.sort()
print(list)

#Count how many times a specific number appears in a list
list = ['team', 'hyper', 'ena', 'cat', 'xlm']
x=list.count('team')
print(x)

# Replace all negative numbers in a list with 0.
lis=[21,40,-3,12,23,-89]
for i in range(len(lis)):
    if lis[i]<0:
        lis[i]=0

print(lis)
# Merge two lists and remove duplicates
list1 = ['team', 'hyper', 'ena', 'cat', 'xlm']
list2 = ['eam', 'hyper', 'na', 'at', 'klm']
list3=list1+list2
list3=list(dict.fromkeys(list3))
print(list3)

# Create a list of the first 10 multiples of 3
numbers = list(range(1, 11))
factor=3
mul=[]
for item in numbers:
    mul.append(item*factor)
print(mul)

# Find the index of the first occurrence of a given number in a list
list1 = ['team', 'hyper', 'ena', 'cat', 'xlm']
x = list1.index('team')
print(x)

# Remove the last element of a list using slicing
list1 = ['team', 'hyper', 'ena', 'cat', 'xlm']
sub=list1[:4]
print(sub)

# Create a list of characters from a given string.
text = "hblengine"
char_list = list(text)
print(char_list)

# Replace the first element of a list with 100
list1 = ['team', 'hyper', 'ena', 'cat', 'xlm']
list1[0] = 100
print(list1)

# Sum all positive numbers in a list
lis = [21, 40, -3, 12, 23, -89]
sum1=sum(x for x in lis if x>0)
print(sum1)

# Create a list of numbers divisible by 5 between 1 and 100
numbers = list(range(1, 101))
for num in numbers:
    if num%5==0:
        print(num)

# Check if a list is sorted in ascending order
numbers = [21, 40, -3, 12, 23, -89]
is_ascending = numbers == sorted(numbers)
print(is_ascending)
'''
# Insert an element at the third position in a list
numbers = [21, 40, -3, 12, 23, -89]
numbers.insert(2, 123)
print(numbers)
