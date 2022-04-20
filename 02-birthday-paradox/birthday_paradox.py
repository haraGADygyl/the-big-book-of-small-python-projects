import datetime
import random


def get_birthdays(number_of_birthdays):
    """ Returns a list of random date objects for birthdays. """

    birthdays_list = []
    for i in range(number_of_birthdays):
        """ The year is unimportant for our simulation, as long as all birthdays are in the same year. """
        start_of_year = datetime.date(2001, 1, 1)

        """ Get a random day into the year. """
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays_list.append(birthday)

    return birthdays_list


def get_match(bdays):
    """ Returns the date object of a birthday that occurs more than once in the birthday list. """
    if len(bdays) == len(set(bdays)):
        return None

    """ Compare each birthday to every other birthday. """
    for a, birthday_a in enumerate(bdays):
        for b, birthday_b in enumerate(bdays[a + 1:]):
            if birthday_a == birthday_b:
                """ Return the matching  birthday. """
                return birthday_a


""" Display the intro. """
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
''')

""" Set up a tuple of month names in order. r"""
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    """ Keep asking until the user enters a valid amount. """
    print('How many birthdays shall I generate?')
    response = input('>')
    if response.isdecimal() and (0 < int(response) <= 100):
        number_birthdays = int(response)
        """ User has entered a valid amount. """
        break

print()
""" Generate and display the birthdays. """
print(f'Here are {number_birthdays} birthdays:')

birthdays = get_birthdays(number_birthdays)

for sim, birthday in enumerate(birthdays):
    if sim != 0:
        """ Display a comma for each birthday after the first birthday. """
        print(', ', end='')

    month_name = MONTHS[birthday.month - 1]
    # month_name = birthday.strftime('%B')
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')

print()
print()

""" Determine if there are two birthdays that match. """
match = get_match(birthdays)

""" Display the results. """
print('In this simulation, ', end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print(f'multiple people have a birthday on {date_text}')
else:
    print('there are no matching birthdays.')

print()

""" Run through 100,000 simulations. """
print(f'Generating {number_birthdays} random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')

""" How many simulations had matching birthdays in them. """
sim_match = 0
for sim in range(100_000):
    """ Report on the progress every 10,000 simulations. """
    if sim % 10 == 0:
        print(f'{sim} simulations run...')

    birthdays = get_birthdays(number_birthdays)
    if get_match(birthdays) is not None:
        sim_match += 1

print('100,000 simulations run.')

""" Display simulation results. """
probability = round(sim_match / 100_000 * 100, 2)

print(f"""Out of 100,000 simulations of {number_birthdays} people, there was a matching birthday {sim_match} times. 
This means that {number_birthdays} people have a {probability}% chance of having a matching birthday in their group
That\'s probably more than you would think!""")

"""
Q: How are birthdays represented in this program?
A: As a datetime object.

Q: How could you remove the maximum limit of 100 birthdays the program generates?
A: By changing 100 value in (0 < int(response) <= 100) in line.

Q: What error message do you get if you delete or comment out number_birthdays = int(response) on line 51?
A: A NameError is raised in line 57:
    print(f'Here are {number_birthdays} birthdays:')
    NameError: name 'number_birthdays' is not defined

Q: How can you make the program display full month names, such as 'January' instead of 'Jan'?
A: Option 1 would be to change the names of the months in the MONTHS tuple to 'January' etc.
   Option 2 would be to change line 66 to:
   month_name = birthday.strftime('%B')

Q: How could you make 'X simulations run...' appear every 1,000 simulations instead of every 10,000?
A: By changing line 98 to:
   if sim % 1000 == 0:
"""