"""UDF in Python"""

# Greeter
def hello(name):
    print ("Hello, " + name + "!")
    print ("Welcome to Python, " + name + "!")
    print ("Enjoy it!, " + name + "!")
print ("Greeter")
input_name = input("What is your name? ")
hello(input_name)

#Full Names
def full_name(first_name, last_name):
    print ("Hello " + first_name + " " + last_name + "!")
print ("Full Names")
input_first_name = input("What is your first name? ")
input_last_name = input("What is your last name? ")
full_name(input_first_name, input_last_name)

