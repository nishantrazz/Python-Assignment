numbers = []
num = int(input('How many numbers: '))
for n in range(num):
    x = int(input('Enter number '))
    numbers.append(x)
print("Sum of numbers in the given list is :", sum(numbers))