import string
import nltk 
import random

#chatbot inputs
HAPPYMOOD = ['good', 'happy', 'excited']
SADMOOD = ['sad', 'bad', 'terrible', 'meh']
HAPPYMOOD_OUT = ["That's awesome! We're going to start the test!"]
SADMOOD_OUT = ["I'm sorry to hear that. Hopefully this test makes you feel better!"]

#basic functions to prepare input from user, cleaning up the input 
def is_question(question_input):
    """Checks if the input is a question.

    PARAMETERS
    ----------
    question_input : str
        This is the input string that will be checked.

    RETURNS
    -------
    bool
        Will return True if the input has '?', or will return False.
    """
    if '?' in question_input:
        output = True
    else:
        output = False
    return output


def remove_punctuation(writing_input):
    """Removes the punctuation after it realizes the input is a question

    PARAMETERS
    ----------
    writing_input : str
        This is the input string with punctuation.

    RETURNS
    -------
    str
        This is the input string with removed punctuation.
    """
    output_string = ''
    for value in writing_input:
        if value not in string.punctuation:
            output_string += value
    return output_string


def preparing_answers(writing_input):
    """ This prepares the input for processing by converting it to lowercase, removing punctuation, splitting it into words

    PARAMETERS
    ----------
    writing_input : str
        This is the input string that will be prepared.

    RETURNS
    -------
    str
        This is the prepared string.
    """
    lowercase_writing = writing_input.lower()
    lowercase_writing = remove_punctuation(lowercase_writing)
    output_lowercase = lowercase_writing.split()
    finished_message = ' '.join(output_lowercase)
    return finished_message


def select_output(input_list, check_list, return_list):
    """Chooses an output for the chatbot based on the input. It takes in a list of words, checks if they appear, and a list of the possible outputs.

    PARAMETERS
    ----------
    input_list : list
        Word list that will be checked
    check_list : list
        Word list that will be checked to see if they're in the list of inputs
    return_list : list
        Possible outputs list

    RETURNS
    -------
    None or str
    Randomly chosen from return list if there's a match or returns None
    """
    output = None
    for value in input_list:
        if value in check_list:
            output = random.choice(return_list)
    return output


def end_chat(writing_list):
    """If the user quits the chatbot, the code stops running.

    PARAMETERS
    ----------
    writing_list : list
        Word list from input.

    RETURNS
    -------
    bool
        Will return True if 'quit' is in input, or will return False
    """
    if 'quit' in writing_list:
        output = True
    else:
        output = False
    return output


def happy(words):
    """Checking if words in the list are happy.

    PARAMETERS
    ----------
    words : list
        Check if they're happy.

    RETURNS
    -------
    bool
        Will return True if happy words are in the input, or will return False
    """
    global HAPPYMOOD
    return any(word in words for word in HAPPYMOOD)

def sad(words):
    """Checking if words in the list are sad.

    PARAMETERS
    ----------
    words : list
        Checkif they're sad.

    RETURNS
    -------
    bool
        Will return True if sad words are in the input, or will return False
    """
    global SADMOOD
    return any(word in words for word in SADMOOD)


def diff_type_of_question():
    """Asks questions that will determine a drink for the user and keeping count of points that will determine the final result.

    RETURNS
    -------
    int
        The total amount of points based on the user's answers
    """    
    points = 0

    while True:
        question_1 = input("What is your favorite color out of these four? \nA. Blue \nB. Pink \nC. Black \nD. Red\n").lower()
        if question_1 in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Please input either 'a', 'b', 'c', or 'd'")
        #makes sure that the code doesn't accept any other answers other than a,b,c, or d
    if question_1 == 'a':
        points += 1
    elif question_1 == 'b':
        points += 1
        #for happier drinks, the points are less
    elif question_1 == 'c':
        points += 3
    elif question_1 == 'd':
        points += 2
        #for more intense drinks, the points are more

    while True:
        question_2 = input("Which one of these activities would you like to experience? \nA. Surfing and fishing at the beach \nB. Reading a romance novel by the fireplace \nC. Watching a psychological thriller with friends \nD. Playing aggressive rounds of ping pong with family\n").lower()
        if question_2 in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Please input either 'a', 'b', 'c', or 'd'")
        #makes sure that the code doesn't accept any other answers other than a,b,c, or d

    if question_2 == 'a':
        points += 1
    elif question_2 == 'b':
        points += 2
    elif question_2 == 'c':
        points += 4
    elif question_2 == 'd':
        points += 5
        #the point system follows the same philosophy as the previous question

    while True:
        question_3 = input("What sort of music do you like listening to? \nA. Jazz \nB. Classical \nC. Rap \nD. Pop\n").lower()
        if question_3 in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Please input either 'a', 'b', 'c', or 'd'")
        #makes sure that the code doesn't accept any other answers other than a,b,c, or d

    if question_3 == 'a':
        points += 2
    elif question_3 == 'b':
        points += 1
    elif question_3 == 'c':
        points += 4
    elif question_3 == 'd':
        points += 2
        #the point system follows the same philosophy as the previous ones

    while True:
        question_4 = input("Which animal would you like to domesticate? \nA. Raccoon \nB. Ostrich \nC. Whale \nD. Flamingo\n").lower()
        if question_4 in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Please input either 'a', 'b', 'c', or 'd'")
        #makes sure that the code doesn't accept any other answers other than a,b,c, or d

    if question_4 == 'a':
        points += 1
    elif question_4 == 'b':
        points += 3
    elif question_4 == 'c':
        points += 2
    elif question_4 == 'd':
        points += 5
        #the point system follows the same philosophy as the previous ones

    while True:
        question_5 = input("What would you like to get with your cafe drink? \nA. Chocolate-chip cookie \nB. Brownie \nC. Strawberry shortcake \nD. Croissant\n").lower()
        if question_5 in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Please input either 'a', 'b', 'c', or 'd'")
        #makes sure that the code doesn't accept any other answers other than a,b,c, or d

    if question_5 == 'a':
        points += 1
    elif question_5 == 'b':
        points += 2
    elif question_5 == 'c':
        points += 3
    elif question_5 == 'd':
        points += 4
        #the point system follows the same philosophy as the previous ones
    return points


def drink_reccomendations(points):
    """Reccomends the drink after the points are calculated from the questions.

    PARAMETERS
    ----------
    points : int
        Total amount of points from the user's answers. 

    RETURNS
    -------
    str
        Will return what drink the chatbot would reccomend
    """
    if 5 <= points <= 7:
        return "Matcha"
    elif 8 <= points <= 10:
        return "Caramel Cappuccino"
    elif points >= 11:
        return "Black Coffee"
    elif 0 <= points <= 4:
        return "Earl Grey Tea"
    else:
        return "Hot Chocolate"


def main_coffee_chatbot():
    """Main function to run chatbot."""

    global HAPPYMOOD
    global SADMOOD
    global HAPPYMOOD_OUT
    global SADMOOD_OUT

    print("Hi, my name is Koffee! I am coffee chatbot, and I will ask you some questions to determine what drink best suits your personality. ")
    print("How are you feeling today?")
    chat = True
    out_message = "Enjoy!"

    while chat: 
            #while the user doesn't end the chat
        message = input('Input:\t')
            #shows where the user inputs her writing

        question = is_question(message)
            #checks if the message is a question

        message = preparing_answers(message)
            #prepares the input message

        if end_chat(message):
            out_message = 'See you next time!'
            chat = False

        else:
            outputs = []
            #empty list to store what the chatbot says based on the user's inputs
            words = message.lower().split(" ")
            #lowercases the list and makes it into a word list

            if happy(words):
                outputs.append(select_output(words, HAPPYMOOD, HAPPYMOOD_OUT))
                print('Koffee: ', outputs[0])

            elif sad(words):
                outputs.append(select_output(words, SADMOOD, SADMOOD_OUT))
                print('Koffee: ', outputs[0])

            points = diff_type_of_question()
            reccomendation = drink_reccomendations(points)
            print(f"Based on your inputs, I reccomend a delicious {reccomendation} for you.")

            chat = False


#      
        print(out_message)