# n=int(input("enter value of n:"))
# rows=int(input("enter number of rows:"))
# columns=int(input("enter number of columns:"))

#rectangle pattern
"""
rows=6
columns=4
output:

         ****
         ****
         ****
         ****
         ****
         ****
"""

"""
for i in range(rows):
    print(columns*"*")
OR
"""
"""
for i in range(rows):
    for j in range(columns):
        print("*",end="")
    print("")
"""
#Hollow rectangle pattern
"""
rows=6
columns=4
output:

         ****
         *  *
         *  *
         *  *
         *  *
         ****
"""
"""
for i in range(rows):
    for j in range(columns):
        if i==0 or i==(rows-1):
            print("*",end="")
        
        elif j==0 or j==(columns-1):
            print("*",end="")
            
        elif j!=0 or j!=(columns-1):
            print(" ",end="")
            
    print("")
"""
#inverted half pyramid
"""
n=7
output:

     *******
     ******
     *****
     ****
     ***
     **
     *
"""
"""
while n:
    print(n*"*")
    n-=1
OR
"""
"""
for i in range(n,0,-1):
    print(i*"*")
OR
"""
"""
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
"""    
#half pyramid 
"""
n=7
output:

     *
     **
     ***
     ****
     *****
     ******
     *******
"""
"""
i=1
while n:
    if i<=n:
        print(i*"*")
        i+=1
OR
"""
"""
for i in range(1,n+1):
    print(i*"*")
OR
"""
"""
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print("")
"""
#half pyramid after 180 rotation
"""
n=7
output:
      *
     **
    ***
   ****
  *****
 ******
*******
"""
"""
i=1
k=n
while i<=n:
    print((k-1)*" "+i*"*")
    i+=1
    k-=1
OR
"""
"""
k=1
for i in range(n,0,-1):
    print((i-1)*" "+k*"*")
    k+=1
OR
"""
"""
for i in range(1,n+1):#1,2,3,4,5
    for j in range(n-i):#1)(5-1),4=0,1,2,3
                        #2)(5-2),3=0,1,2
                        #3)(5-3),2=0,1,
                        #4)(5-4),1=0
        print(" ", end="")
    for k in range(i):#1
                      #2
                      #3
                      #4
                      #5
        print("*", end="")
    print()
"""
#half pyramid using number
"""
n=7
output:

       1
       22
       333
       4444
       55555
       666666
       7777777
"""
"""
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print("")
OR
"""
"""
i=1
while i<=n:
    j=0
    while j<i:
        print(i,end="")
        j+= 1
    print()
    i+=1
"""
#floyd's triangle
"""
n=5
output:

       1
       23
       456
       78910
       1112131415
"""
"""
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end="")
        k+=1
    print("")
OR
"""
"""
k=1
i=1
while i<=n:
    j=0
    while j<i:
        print(k, end="")
        k+=1
        j+=1
    print("")
    i+=1
"""
#butterfly pattern
"""
n=4
output:
        *      *
        **    **
        ***  ***
        ********
        ********
        ***  ***
        **    **
        *      *
        
"""
"""
for i in range(1,n+1):
    print('*'*i,end="")
    print(' '*(2*(n-i)),end="")
    print('*'*i)
for j in range(n,0,-1):
    print('*'*j,end="")
    print(' '*(2*(n-j)),end="")
    print('*'*j)
"""
#inverted pattern
"""
n=7
output:
        1234567
        123456
        12345
        1234
        123
        12
        1
        
"""
"""
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
OR
"""
"""
while n:
    j=1
    while j<=n:
        print(j,end="")
        j+=1
    print()
    n-=1
"""
#0-1 pattern
"""
n=7
output:
        1
        01
        101
        0101
        10101
        010101
        1010101
        
"""
"""
for i in range(1,n+1):#1,2,3
    for j in range(1,i+1):#1-2(1),1-3(1,2),1-4(1,2,3)
        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0) :
            print("1",end="")
        else:
            print("0",end="")
    print()
OR
"""
"""
i=1
while n:
    j=1
    while j<=i:
        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0) :
            print("1",end="")
        else:
            print("0",end="")
        j+=1
    print()
    i+=1
    n-=1
"""    
#rhombus pattern
"""
n=5
output:
    *****
   *****
  *****
 *****
*****
        
"""
"""
for j in range(n-1,-1,-1):
    print(j*" "+n*"*",end="")
    print()
OR
"""
"""
for i in range(n-1,-1,-1):#4,3,2,1,0
    for j in range(i):#0-3,0-2,0-1,not execute
        print(" ",end="")
    for k in range(n):#0-4,0-4,0-4,0-4,0-4
        print("*",end="")
    print()
"""    
#number pattern
"""
n=5
output:
    1
   12
  123
 1234
12345
        
"""
"""            
for i in range(1,n+1):#1,2,3,4,5
    for j in range(n-i):
        print(" ", end="")
    for k in range(1,i+1):
        print(k,end="")
    print()
OR
"""
"""
for i in range(1,n+1):
    print("#"*(n-i)+"".join(str(x) for x in range(1,i+1)))

OR
"""
"""
i = 1
while i <= 5:
    j = 5 - i
    while j > 0:
        print("#", end="")
        j -= 1
    k = 1
    while k <= i:
        print(k, end="")
        k += 1
    print()
    i += 1
"""    
#palindromic pattern
"""
n=5
output:
    1
   212
  32123
 4321234
543212345
        
"""
"""
for row in range(1,n+1):
    for space in range(n-row):
        print(" ",end="")
    for i in range(row,0,-1):
        print(i,end="")
    for j in range(2,row+1):
        print(j,end="")
    print()
"""
#palindromic pattern
"""
n=5
output:
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    * 
        
"""
"""
for row in range(1,n+1):
    for space in range(n-row):
        print(" ",end="")
    for i in range(0,(2*row)-1):
        print("*",end="")
    print()
for inverse_row in range(n,0,-1):
    for inverse_space in range(n-inverse_row):
        print(" ",end="")
    for j in range((2*inverse_row)-1,0,-1):
        print("*",end="")
    print()
"""
#Zig-Zag pattern
"""
n=9
output:

  *  *
 * * * *
*   *   *

"""
"""
for row in range(1,4):
    for column in range(1,n+1):
        if ((row+column)%4==0) or (row==2 and column%4==0):
            print(f"*",end="")
        else:
            print(f" ",end="")
    print()
"""    



    
