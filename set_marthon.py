# Create a set containing numbers 1 to 5 and print it.
'''my={1,2,3,4,5}
print(my)

#Add the element 6 to a set {1, 2, 3}.
my = {1, 2, 3, 4, 5}
my.add(6)
print(my)

# Remove the element 2 from {1, 2, 3}
my = {1, 2, 3, 4, 5}
my.remove(2)
print(my)

# Try removing an element that does not exist in {1, 2, 3} using .discard()
my = {1, 2, 3, 4, 5}
my.discard(9)
print(my)
# Check if 5 is in {1, 3, 5, 7}
this = {1, 3, 5, 7}
if 5 in this:
    print('yes 5 in there')

# Create a set from the list[1, 2, 2, 3, 4, 4] and print it.
my_list = [1, 2, 2, 3, 4, 4]
my_set = set(my_list)
print(my_set)

#Find the length of {1, 2, 3, 4}
my_list = {1, 2, 3, 4}
length=len(my_list)
print(length)

# Clear all elements from a set {1, 2, 3}
gram = {1, 2, 3}
gram.clear()
print(gram)

#Create a set using the set() constructor from a string 'hello'.
s=set("hello")
print(s)

# Check if two sets {1, 2, 3} and {3, 4, 5} are disjoint
a={1,2,3}
b={3,4,5}
print(a.isdisjoint(b))

# Find the union of {1, 2} and {2, 3}
a={1,2}
b={2,3}
union_a=a.union(b)
print(f"union of a and b :{union_a}")

# Find the intersection of {1, 2} and {2, 3}
a={1,2}
b={2,3}
intersection_a=a.intersection(b)
print(f"intersection of a and b is:{intersection_a}")

# Find the difference between {1, 2, 3} and {2, 3}
a = {1, 2, 3}
b = {2, 3}
result = a.difference(b)
print(result)

# Find the symmetric difference between {1, 2, 3} and {2, 3, 4}
a = {1, 2, 3}
b = {2, 3, 4}
diff = a.symmetric_difference(b)
print(diff)


# Update a set {1, 2} with elements from {3, 4}
a = {1, 2}
b = {3, 4}
a.update(b)
print(a)

# Update a set {1, 2, 3} to keep only elements in {2, 3, 4}
b={1,2,3}
c={2,3,4}
b.intersection_update(c)
print(b)

# Copy a set {1, 2, 3} into another variable without linking references
a = {1, 2, 3}
b = a.copy()
print(b)

# Create an empty set and check its type
A={1,2,3}
print(type(A))

# Check if {1, 2} is a subset of {1, 2, 3}
a={1,2}
b={1,2,3}
if a.issuperset(b):
    print('yes it is')
else:
    print('none')

# Check if {1, 2, 3} is a superset of {1, 2}
a={1,2,3}
b={1,2}
if a.issuperset(b):
    print('yes it is')
else:
    print('none')

# Iterate over the elements of a set and print them
t = {1, 2, 3}
for element in t:
    print(element)

    # Create a set of even numbers from 0 to 10 using set comprehension
n=[1,2,3,4,5,6,7,8,9,10]
even_squares={num for  num in n if num %2==0}
print(even_squares)

# Create a set of the first letters of each word in a list['apple', 'banana', 'cherry']
fruit = ['apple', 'banana', 'cherry']
res=map(lambda x:x[0],fruit)
print(set(res))

#Convert {1, 2, 3} into a list.
my={1,2,3}
lis=list(my)
print(lis)

# Convert a list[1, 2, 3] into a set
p=[1,2,3]
s=set(p)
print(s)

# Merge {1, 2} and {3, 4} into a new set without changing the originals.
a={1,2}
b={3,4}
new=a.union(b)
print(f"using union method:{new}")

# Remove and return an arbitrary element from {1, 2, 3}
a={1,2,3}
print(a.pop())
print(a)

# Create a set from the keys of a dictionary {'a': 1, 'b': 2}
ser = {'a': 1, 'b': 2}
keys_view = set(ser.keys())
print(keys_view)

# Check if a set is empty.
a={1,2,3,4}
if not a:
    print('empty')
else:
    print('none')

# Use in and not in to check membership in a set
joy = {'anik', 'brigade', 'alto'}
if 'anik' in joy:
    print('yes')

# Find the common elements in three sets
a = {1, 2, 3}
b = {2, 4, 6}
c = {4, 2, 8}
multiple = a.intersection(b, c)
print(multiple)

# Find elements that are in either of two sets but not both
a = {1, 2, 3}
b = {2, 4, 6}
uq=a.union(b)
print(uq)

# Create a set of unique words from a sentence
q = 'Create a set of unique words'
words=q.split()
print(f"list of words:{words}")
unique=set(words)
print(f"set of words:{unique}")

# Find elements in one set that are not in another
a = {1, 2, 3}
b = {9, 4, 6, 1}
up = a.difference(b)
print(up)

# Given two sets, remove all elements of one from the other.
a = {1, 2, 3}
b = {9, 4, 6, 1}
c = a-b
print(c)

# Given two sets, add all elements from the second to the first without using .union()
a = {1, 2, 3}
b = {9, 4, 6, 1}
c = a | b
print(c)

# Create a set of squares of numbers 1–10
squares = {a**2 for a in range(1, 11)}
print(squares)

# Filter a set to keep only numbers greater than 5
b = {9, 4, 6, 1}
silter = set(filter(lambda x: x > 5, b))
print(silter)

# Given {1, 2, 3} and {4, 5, 6}, swap their contents without creating a new set
a = {1, 2, 3}
b = {4, 5, 6}
a, b = b, a
print(a)
print(b)

# Count how many vowels are in a given string using a set.
a = 'hello'
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(a.count(v) for v in set(a) & vowels)
print(c)

# Given two sets of student IDs, find those who are enrolled in both courses.
class_A = {
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie"),
}

class_B = {
    (103, "Charlie"),
    (102, "Diana"),
    (105, "Ethan"),
}
class_c=class_A.intersection(class_B)
print(class_c)

# Find IDs in one course but not the other.
class_A = {
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie"),
}

class_B = {
    (103, "Charlie"),
    (102, "Diana"),
    (105, "Ethan"),
}
class_c=class_A.difference(class_B)
print(class_c)

# Check if two sets are exactly the same
a={1,2,3}
b={1,2,4}
c={1,2,3}
print(a==b)
print(a==c)

# Create a set of all characters that appear in two different strings
a = 'The sun was setting behind the mountains, painting the sky orange and pink'
b = 'A small dog chased butterflies across the grassy field'
words = a.split()
wordsone = b.split()
uniqueone = set(words)
unique = set(wordsone)
print(f"set of words:{unique}")
print(f"set of words:{uniqueone}")
  
s1 = "hello world"
s2 = "yellow bird"

# Convert both strings to sets of characters
set1 = set(s1)
set2 = set(s2)

# Find common characters (intersection)
common_chars = set1 & set2

print(common_chars)

# Find the union of multiple sets stored in a list
from functools import reduce
a=[{1,2},{3,4},{5,6}]
union_set=reduce(set.union,a)
print(union_set)

# Find the intersection of multiple sets stored in a list
from functools import reduce
a = [{1, 2}, {3, 4}, {5, 6}]
union_set = reduce(set.intersection, a)
print(union_set)

# Create a set of even numbers from another set
 a={1,2,3,4,5,6,7,8,9}
b={x for x in a if x%2==0}
print(b)

# Remove all odd numbers from a set in place
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {x for x in a if x % 2 !== 0}
print(b)

# Create a set of words in a file(ignore duplicates)
with open("example.txt","r") as f:
    text=f.read()
words=set(text.split())
print(words)

# Find the number of unique characters in a text
with open("example.txt", "r") as f:
    text = f.read()
words = set(text.split())
r = len(words)
print(r)

#Given two lists, check if they have any common elements using sets
students = ["Alice", "Bob", "Charlie", "Diana"]
b = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
one=set(students)
two=set(b)
three=one.intersection(two)
print(three)

# Given a set of numbers, print the max and min values
student_ids = {101, 102, 103, 104, 105}
print(max(student_ids))
print(min(student_ids))

# Given a set of integers, print them in sorted order.
i = {2, 7, 3, 6, 9}
a = sorted(i)
print(a)

# Convert a set of tuples into a set of strings
r = {(1, 2), (3, 4), (5, 6)}
my = {f"{a} {b}" for a, b in r}
print(my)

# Remove all elements from a set that are divisible by 3
i = {2, 7, 3, 6, 9}
a={x for x in i if x%3!=0}
print(a)

#Given a string, find all unique vowels in it
a = 'want me to also show you how to do this wit'
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = {v for v in a if v in vowels}
print(c)

#Check if a set is a proper superset of another
a={1,2,3,4,5}
b={2,3}
print(f"a is superset of b {a.issuperset(b)}")

# Create a set of ASCII codes from characters in a string
def string_to_ascii_codes(s):
    return [ord(char) for char in s]

text="crypto"
ascii_codes=string_to_ascii_codes(text)
print(ascii_codes)

# Create a set of all lowercase letters from a text
a = 'CREATE'
c = {d.lower() for d  in a}
print(c)
'''


''' 
1.Given a set of words, find those that have more than 5 letters.

2.Create a set from a range of numbers skipping multiples of 5.

3.Use a set to remove duplicates from a list of lists(by converting each list to a tuple).

4.Given a list of names, find names starting with a vowel using a set.

5.Create a set of all two-letter combinations from a given string.

6.Create a set containing all factors of a number.

7.Given a set of numbers, split it into even and odd sets.

8.Merge multiple sets into one using set.update().

9.Create a set of numbers that are prime from 1 to 50.

10.Find all letters that appear in either of two sentences but not both.

11.Advanced(frozenset, Performance & Tricky Cases) — 71–100

12.Create a frozenset from a list of numbers.

13.Check if a frozenset can be modified.

14.Use a frozenset as a dictionary key.

15.Find the difference between a set and a frozenset.

16.Store multiple frozenset objects in a set.

17.Create a frozenset from the characters of a string.

18.Check if a frozenset is a subset of a set.

19.Create a frozenset containing tuples.

20.Merge two frozensets into a new frozenset.

21.Use a set comprehension with a frozenset.

22.Use a set to find the first repeated character in a string.

23.Use a set to detect if a list has duplicates.

24.Given a list of integers, return the missing numbers from a range using sets.

25.Find the symmetric difference between more than two sets.

26.Compare the performance of checking membership in a list vs a set.

29.Implement a set-like structure using only dictionaries.

30.Find common divisors of two numbers using sets.

31.Create a set of all substrings of a given string.

32.Given a set of points(x, y), find those in the first quadrant.

33.Check if a set of words forms a pangram(contains all letters).

34.Use sets to detect anagrams between two strings.

35.Count the number of distinct words across multiple files.

36.Store sets inside a dictionary for categorizing items.

37.Create a set from a generator expression.

38.Remove all strings shorter than 4 characters from a set.

39.Given a set of numbers, keep only those whose binary representation has exactly two 1s.

40.Create a set of palindromes from a list of words.
'''
