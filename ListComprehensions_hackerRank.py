# def is_leap(year):
#     if (year % 4 == 0) and (year % 100 != 0):
#       # Note that in your code the condition will be true if it is not..
#       leap = True
#     elif (year % 100 == 0) and (year % 400 != 0):
#       leap = False
#     elif (year % 400 == 0):
#       # For some reason here you had False twice
#       leap = True
#     else:
#       leap = False
#
#     return leap
# year = int(input('Type here: >> '))
# print(is_leap(year))
x = int(input('>'))
y = int(input('>'))
z = int(input('>'))
n = int(input('>'))
lists = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
print(lists)
