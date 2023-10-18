l1_str = input("Enter the list:")
l = list(map(int,l1_str.split()))
triple = lambda x: x * 3
result  = list(map(triple, l))
print("List of number:", l)
print("triple of list numbers:", result)
