#first Question
a=int(input("enter the first integer: "))
b=int(input("enter the second integer: "))
list1 = [54,76,2,4,98,100]
for i in list1:
    if a < i < b:
        print(i)

#Second Question 
names=["Maria","Shady","Ehsan","Joe","Zoe"]
while True:
    letter=input("enter a letter: ")
    if len(letter)!=1 or not letter.isalpha():
        print("the length of this letter is greater then 1.Please re enter the character")
        continue
    for name in names:
        if letter in name.lower():
            print(name)
    break
#third Question 
numbers=[-12, 4, 12, 25, 67]
while  True:
    n= int(input("enter a number:"))
    if n == -99:
        break
    numbers.append(n)
    numbers.sort()
   
    print(f"the sorted list",numbers)
    break
    
    
