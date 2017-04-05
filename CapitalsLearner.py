### THIS PROGRAM CREATES TWO FILES IN THE FOLDER WHERE THIS FILE EXISTS ###
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


stateHandler = open('State Answers.py', 'w')
answerHandler = open('Capital Answers.py', 'w')

commaLooper = 0
answerNumber = 1


# Generates the files for states and capitals in a dictionary format
answerHandler.write('Answers = {')
stateHandler.write('States = {')
for keys, values in capitals.items():
    stateHandler.write('\'' + keys + '\'' + ': %s' % answerNumber)
    answerHandler.write('\'' + values + '\'' + ': %s' % answerNumber)
    answerNumber += 1
    if commaLooper < 49:
        answerHandler.write(', ')
        stateHandler.write(', ')
    commaLooper += 1
answerHandler.write('}')
stateHandler.write('}')

answerHandler.close()
stateHandler.close()


something = __import__('CapitalAnswers')
stateAnswers = __import__('State Answers')

readingCapitals = open('CapitalAnswers.py')
readingStates = open('State Answers.py')

States = stateAnswers.States
Capitols = something.Answers
capitalsShortcut = (list(Capitols.keys()))

for k in range(0, 2):
    # Generates random keys that will be linked to the files
    number1, number2, number3, number4, number5 = random.randint(1, 50), random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50)
    randomCapitals = [number1, number2, number3, number4, number5]
    # Randomizes the output
    random.shuffle(randomCapitals)
    # Generates the answer
    correctState = (list(Capitols.keys())[list(Capitols.values()).index(number1)], list(States.keys())[list(States.values()).index(number1)])
    print(correctState[0])  # for debuging answer
    print('The capital of', correctState[1], 'is: ')
    # Time to print 5 different options
    print('Your options are: ', capitalsShortcut[list(Capitols.values()).index(randomCapitals[0])], '|', capitalsShortcut[list(Capitols.values()).index(randomCapitals[1])], '|', capitalsShortcut[list(Capitols.values()).index(randomCapitals[2])], '|')
    print(capitalsShortcut[list(Capitols.values()).index(randomCapitals[3])], '|', capitalsShortcut[list(Capitols.values()).index(randomCapitals[4])])
    guesses = 0
    while guesses != 1:  # This is where you actually guess
        guess = input('Enter your guess: ')
        if guess == correctState[0]:
            print('You got it right!')
            guesses += 1
            print('\n'*10)
        else:
            print('Sorry! Guess again!')
readingCapitals.close()
readingStates.close()
