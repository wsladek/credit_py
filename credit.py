from cs50 import get_int


#Get user input, introduce some variables
card = get_int("Credit Card Number: ")
digitize = card
count = len(str(abs(card)))
total = 0


#Store digits in list
digits=[]
for i in range(count):
    digits.append(int(digitize % 10))
    digitize = (digitize-digits[i])/10


#Grab the first couple digits for checkin later
firstTwo = digits[count-1]*10+digits[count-2]
firstOne = digits[count-1]


#Step 1: Multiply every other digit by 2,
#starting with the number’s second-to-last digit,
#then add those products' digits together
position = 1
productsSum = 0

for j in range(int(count/2)):
    digits[position]=2*digits[position]
    for k in range(len(str(abs(digits[position])))):
        productsSum = productsSum+(int(digits[position]%10))
        digits[position]=(digits[position]-(int(digits[position]%10)))/10
    position=position+2


#Step 2: Add the sum to the sum of the digits that weren’t multiplied by 2.
position=0
stepTwoCounter=0

if count % 2 == 0:
    stepTwoCounter = int(count/2)
else:
    stepTwoCounter = int((count+1)/2)

for l in range(stepTwoCounter):
    productsSum=productsSum+digits[position]
    position=position+2


#Step 3: If the total’s last digit is 0 (or, put more formally,
#if the total modulo 10 is congruent to 0), the number is valid!
if productsSum % 10 == 0:
    if firstOne == 4 and (count == 13 or count == 16):
        print("VISA")
    elif (firstTwo == 34 or firstTwo == 37) and count == 15:
        print("AMEX")
    elif (firstTwo == 51 or firstTwo == 52 or firstTwo == 53 or firstTwo == 54 or firstTwo == 55) and count == 16:
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")