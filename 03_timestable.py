
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

print("Here is the {} times table".format(times_table))
for x in range(1, max_value + 1):
    answer = x * times_table
    print("{} times {} is {}".format(x, times_table, answer))
