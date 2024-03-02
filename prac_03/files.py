# 1:
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# 2 :
with open('name.txt', 'r') as file:
    name = file.read()
print("Your name is", name)

# 3 :
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
total = num1 + num2
print("The sum of the first two numbers is:", total)

# 4:
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
total = sum(numbers)
print("The total of all numbers is:", total)

