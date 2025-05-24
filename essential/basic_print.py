#print something
print('hello!')

#ask user for something
question = input("Enter the number:")
print(question)

print(type(question)) # will give 'str' class

question1 = int(input("Enter the number:"))
print(question1)
print(type(question1)) #will now give 'int' class

add = question + str(question1) # '+' concatenates strings
print(add)

add1 = question1 + int(question)  # '+' adds integers
print(add1)

#other ways to take inputs

q1 = input("no 1:")
q2 = input("no 2:")

print(q1 + q2)


#what if we don't input anything? (i.e. just press enter)

q3 = input("")
print(q3)
print(type(q3))
print(len(q3))

#can we take two numbers as input together, seperated by space?

q4, q5 = input("Enter numbers:") # will give error

#correct way
q1, q2 = input("Values:").split() #this will separte values between space and assign to different variables
print(q1)
print(q2)