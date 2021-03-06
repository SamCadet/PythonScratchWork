'''
p. 25

Save each of the following exercises as a separate file with a name like
name_cases.py. If you get stuck, take a break or see the suggestions in
Appendix C.

2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
'''
name = 'Deedee'
print(f'Hey {name}, you owe me five bucks!')
'''
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
'''
name = 'janet'
print(name.upper())
print(name.lower())
print(name.title())
'''
2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:

Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
'''
print('Michael Scott once said, "You miss 100%% of the shots you don\'t take."')
'''
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
famous person’s name using a variable called famous_person. Then compose
your message
and represent it with a new variable called message. Print your
message.
'''
name = 'Michael Scott'
print(f'{name} once said, "You miss 100%% of the shots you don\'t take."')
'''
2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''
name = ' \n\tBokeem Woodbine '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
