a = int(input("Enter the starting number:"))
b = int(input("Enter the ending number:"))
c = 0
for num in range (a,b+1):
    if num % 2== 0:
        c = c+ num 
print("total sum of even numbers:" ,c)