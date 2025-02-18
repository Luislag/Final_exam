
my_list = [1, 2, 3]
print("Original list:", my_list)
my_list[0] = 100
print("Modified list:", my_list)
my_string = "hello"
print("Original string:", my_string)
try:
    my_string[0] = "H"
except TypeError as e:
    print("Error")