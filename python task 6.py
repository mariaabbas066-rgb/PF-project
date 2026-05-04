a = int(input("Enter obtained marks"))
b = int(input("Enter total marks"))
percentage = a/b*100
print(percentage)

if a>=90:
   grade='A++'
elif a>=80:
 grade="A"
elif a>=70:
  grade="B" 
elif a>=60:
  grade="pass"
else:
  grade='Fail'
print(grade)

