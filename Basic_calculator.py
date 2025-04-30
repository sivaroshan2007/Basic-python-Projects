print("WELCOME TO SIMPLE CALCULATOR")
print('''For Addition Select 1
         For Subraction Select 2
         For Multiplication Select 3
         For Division Select 4
         For Exponential Select 5''')

selection = int(input('Select a number from 1 to 5 according to your desired operation:'))

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

if(selection==1):
    result = num1 + num2
elif(selection==2):
    result = num1 - num2
elif(selection==3):
    result = num1*num2
elif(selection==4):
    result = float(num1/num2)
elif(selection==5):
    result = num1**num2

else:
    print("Your selected is not from the range 1 to 5 Please select a number from 1 to 5")

print("Answer=",result)