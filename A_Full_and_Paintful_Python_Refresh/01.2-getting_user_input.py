## Getting user input (OOOOOH!)

name = input('Brah, What is your name?')

## Input return always a string and you know already, so convert to int if you need it :)

## Example

size_input = input('How big is your house?(in square feet): ')

square_feet = int(size_input) #str --> int

square_metres = square_feet / 10.8 # Conversion measure unit :)

print(f'{square_feet} square feet is {square_metres:.2f} square_metres')

#Example 2

x = 4863.4343091          # example float to format

print(f"{x:.6}")          # f-string version
print("{:.6}".format(x))  # format method version


x = 4863.4343091

print(f"{x:.3}")  # 4.86e+03

x = 4863.4343091

print(f"{x:.3f}")  # 4863.434

x = 4863.4343091

print(f"{x:f}")  # 4863.434309


#Separators

x = 1000000

print(f"{x:,}")  # 1,000,000
print(f"{x:_}")  # 1_000_000


x = 4863.4343091

print(f"{x:,.3f}")  # 4,863.434
print(f"{x:_.3f}")  # 4_863.434

## Percentages

questions = 30
correct_answers = 23

print(f"You got {correct_answers / questions :.2%} correct!")

# You got 76.67% correct! and we are done :)
