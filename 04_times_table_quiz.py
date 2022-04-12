
print("Enter calculation values.")
try:
    times_table = int(input("Enter a times table digit: "))
except ValueError:
    print("Input a number!")
    times_table = int(input("Enter a times table digit: "))
try:
    max_value = int(input("Enter the max value of the calculations: "))
except ValueError:
    print("Input a number!")
    max_value = int(input("Enter the max value of the calculations: "))

answer = 0

print("You will now be tested on your chosen times table.".format(times_table))
for x in range(1, max_value + 1):
    user_input = int(input("{} times {} is: ".format(x, times_table)))
    answer = x * times_table
    if user_input == answer:
        print("Correct.".format(x, times_table, answer))
    else:
        print("Incorrect. {} times {} is {}".format(x, times_table, answer))

