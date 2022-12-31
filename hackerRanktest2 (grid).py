n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))
lst=[]
for i in range(n):
    x = input().split()
    lst.append(x)
count=0
for i in range(n):
    if i==0:
        if (lst[i][0] > lst[i][1] and lst[i][0] > lst[i+1][0]):
            count+=1
        for k in range(1,m-1):
            if (lst[i][k] > lst[i][k-1] and lst[i][k] > lst[i][k+1] and lst[i][k] > lst[i+1][k]):
                count+=1
                break
        if (lst[i][m-1] > lst[i][m-2] and lst[i][m-1] > lst[i+1][m-1]):
            count+=1
    elif i<n-1:
        if(lst[i][0] > lst[i-1][0] and lst[i][0] > lst[i+1][0] and lst[i][0] > lst[i][1]):
            count+=1
        for k in range(1,m-1):
            if(lst[i][k] > lst[i][k-1] and lst[i][k] > lst[i][k+1] and lst[i][k] > lst[i+1][k-1] and lst[i][k] > lst[i-1][k-1]):
                count+=1
                break
        if(lst[i][m-1] > lst[i][m-2] and lst[i][m-1] > lst[i-1][m-1] and lst[i][m-1] > lst[i+1][m-1]):
            count+=1
    elif i==n-1:
        if (lst[i][0] > lst[i-1][0] and lst[i][0] > lst[i][1]):
            count+=1
        for k in range(1,m-1):
            if(lst[i][k] > lst[i][k-1] and lst[i][k] > lst[i][k+1] and lst[i][k] > lst[i-1][k]):
                count+=1
                break
        if(lst[i][m-1] > lst[i][m-2] and lst[i][m-1] > lst[i-1][m-1]):
            count+=1

if count == 0:
    print("All the cells are submissive")
elif count == 1:
    print("Number of Dominant cell:",count)
else:
    print("Number of Dominant cells:",count)
        
