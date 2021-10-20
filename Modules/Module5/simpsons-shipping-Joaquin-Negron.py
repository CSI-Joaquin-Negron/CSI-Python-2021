print('Welcome to Simpson Shipping!')
uWeight:float = float(input('What is the wight of your package in Killograms?: '))
if(uWeight <= 2):
    gCost = uWeight * 1.75 + 20
elif(uWeight > 2 or uWeight == 6):
    gCost = uWeight * 3.50 + 20
elif(uWeight > 6 or uWeight == 10):
    gCost = uWeight * 4.50 + 20
elif(uWeight > 10):
    gCost = uWeight * 5.25 + 20

if(uWeight <= 2):
    cCost = uWeight * 3.50 + 5.00
elif(uWeight > 2 or uWeight == 6):
    cCost = uWeight * 7.00 + 8.00
elif(uWeight > 6 or uWeight == 10):
    cCost = uWeight * 9.00 + 12.00
elif(uWeight > 10):
    cCost = uWeight * 10.50 + 15.00

if(uWeight <= 2):
    aCost = uWeight * 5.25
elif(uWeight > 2 or uWeight == 6):
    aCost = uWeight * 10.50
elif(uWeight > 6 or uWeight == 10):
    aCost = uWeight * 13.50
elif(uWeight > 10):
    aCost = uWeight * 15.75

print(f'Ground Shipping: {gCost}$')
print('Ground Shipping Premium is 150$')
print(f'Courier Shipping: {cCost}$')
print(f'Air Shipping: {aCost}$')
