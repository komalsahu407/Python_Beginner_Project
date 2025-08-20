len("123456")

print(type("hello"))
print(type(123))
print(type(True))
print(type(34.1))

print("123" + "345")
print(int("133") + int("345"))
# print(int("abc") + int("345"))#value error

# print("Number of letter in your name:" + len(input("enter your name"))) #type error
name_of_the_user=input("enter the user name:")
length_of_the_name=len(name_of_the_user)
print(type("Number of letters in your name: "))#str
print(type(length_of_the_name))#int

print("Number of letter in your name:" + str(length_of_the_name))
