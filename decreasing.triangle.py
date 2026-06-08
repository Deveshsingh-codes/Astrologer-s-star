# Decreasing Triangle by using for loop
                     #**********
                     #*********s
                     #********
                     #*******
                     #******
                     #*****
                     #****
                     #***
                     #**
                     #*

n=int(input("Entern the number of rows:-"))
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()