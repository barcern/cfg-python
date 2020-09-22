# Write a program that asks two questions using input() then prints the values that
# were entered.

name = input('What\'s your name? ')
language = input('Which programming language is your favourite? ')
reason = input('Why do you like this programming language? ')

message = '{}\'s favourite programming language is {} because {}.'.format(name, language, reason)
print(message)