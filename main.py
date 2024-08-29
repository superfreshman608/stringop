'''
Write a program that takes your first name as user input
Then ask the user for the number of repeats
(Don't forget to convert this to an int)
Then print out the first name joined to itself repeat number of times

Sample Output if you used the word Nick for the name input and 3 for the repeat inputN
NickNickNick
'''
name = input("Enter your first name: ")
#INSTRUCTION #1 ask the user with the input() "How many repeats do you want: "
# Store this in a variable called repeats
repeats = input("How many repeats do you want: ")
###YOUDO convert repeats to repeats_num with the int()
repeats_num = int(repeats)
print(name * repeats_num)