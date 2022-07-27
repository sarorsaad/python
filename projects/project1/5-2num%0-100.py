# A program that takes two numbers from the user and prints all the numbers that are divisible by the two numbers from 0 to 100

x=int(input('Enter first number '))
y =int(input('Enter second number '))
for i in range (0,100):
     if (i % x == 0 and i % y== 0):
        print(i ,end=' /')

# x=int(input('enter first number'))
# y=int(input('enter second number'))
# i=1
# while i<=100:
#     if i%x==0 and i%y==0:
#           print(i)
#     i+=1 