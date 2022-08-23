# Players generally sit in a circle. The player designated to go first says the number "1", 
# and the players then count upwards in turn.
#  However, any number divisible by three is replaced by the word fizz and any number divisible by five by the word buzz.
#  Numbers divisible by 15 become fizz buzz. A player who hesitates or makes a mistake is eliminated.

# For example, a typical round of fizz buzz would start as follows:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, 
# Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...


# for loop
def fizz_buzz():
    result_list = []
    for number in range(1,101):
        if (number % 3 == 0) and (number % 5 == 0):
            result_list.append("Fizz Buzz")
        elif (number % 3 == 0):
            result_list.append("Fizz")
        elif (number % 5 == 0):
            result_list.append("Buzz")
        else:
            result_list.append(number) 
    return result_list

print(fizz_buzz())


print()
print()
print()

# while loop
def fizz_buzz():
    number = 1
    result_list = []
    while number <= 100:
        if (number % 3 == 0) and (number % 5 == 0):
            result_list.append("Fizz Buzz")
        elif (number % 3 == 0):
            result_list.append("Fizz")
        elif (number % 5 == 0):
            result_list.append("Buzz")
        else:
            result_list.append(number) 
        number += 1
    return result_list


print(fizz_buzz())



