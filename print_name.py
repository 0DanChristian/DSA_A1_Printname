# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

str1 = "DAN"
print_D = [[" " for i in range(5)] for j in range(5)]
print_A = [[" " for i in range(5)] for j in range(5)]
print_N = [[" " for i in range(5)] for j in range(5)]

# code for letter D
for row in range(5):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=4)) or (row==0 or row==4) and (col>0 and col<4):
            print_D[row][col]= "*"

# code for letter A
for row in range(5):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print_A[row][col]= "*"

# code for N
for row in range(5):
    for col in range(5):
        if ((col==0 or col==4) or row==col):
            print_N[row][col]= "*"

 
for i in range(5):
    print(end="  ")
    for j in range(5):
        print(print_D[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(print_A[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(print_N[i][j], end=" ")
    print(end="  ")
    print()


