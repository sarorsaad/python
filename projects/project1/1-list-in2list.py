# A program that takes a list of numbers and divides it into 2 lists, one with even numbers And one has the odd numbers and prints them

n=int(input('enter the numbers of elements:\t' ))
numbers=[]
even_l=[]
odd_l=[]
for i  in range(1,n+1):
    all_elements=int(input('enter your element'))
    numbers.append( all_elements)
for j in numbers:
    if j%2==0:
        even_l.append(j)
    else:
        odd_l.append(j)
print('this is even list',even_l)
print('this is odd list',odd_l)