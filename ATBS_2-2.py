# this is a demonstration of using while loops

print("Please enter your age")

# reading input stores the inputted value as a string
# this line wouldn't work as you can't compare a int and a str hence the cast

age = int(input())
cnt = 0

print("Lets count how old you are!")
while cnt < age:
    cnt = cnt+1
    if cnt > 10:
        print("That's enough of that! I have no fingers left!")
        break
    print(cnt)

# number guesser with infinite while
num = 5
while True:
    print("Guess the number!")
    guess = int(input())

    if guess == num:
        print("Well Done!")
        break
    print("Guess Again!")

# for loop with range
i = 0
j = 0
k = 7

print("Can you hear that echo?")
for i in range(5):
    print("...echo...")

print("Now for the same with a while")
while j < 5:
    print("..while..")
    j = j + 1

# range doesnt need to be a single number
for k in range(7, 17):
    if k % 2 > 0:
        print(k)

# you can even specify the interval
for k in range(7, 17, 2):
    print(k)
