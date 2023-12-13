"""Here are all of my test functions for my quiz chatbot. Monkeypatch was required for the diff_type_of_question, drink_reccomendations, main_coffee_chatbot functions because they have multiple inputs, but I decided to omit it because the functions still run.
"""

from functions import is_question, remove_punctuation, preparing_answers, select_output, end_chat, user_moods, happy, sad, diff_type_of_question, drink_reccomendations, main_coffee_chatbot

def is_question():
    assert is_question("Is this a coffee?") == True
    assert callable(is_question)
    
    
def remove_punctuation():
    assert remove_punctuation("yay!!") == "yay"
    assert callable(writing_input)
    assert callable(remove_punctuation)
    
def preparing_answers():
    assert preparing_answers("I love coffee!") == "i love coffee"
    assert callable(writing_input)
    assert callable(preparing_answers)
    
def select_output():
    assert select_output(["happy","meh"],["happy","sad"],["Good for you!", "I'm sorry."]) in ["I'm sorry.", None]
    assert callable(input_list)
    assert callable(select_output)

def end_chat():
    assert end_chat("quit") == True
    assert callable(writing_list)
    
def user_moods():
    assert callable(HAPPYMOOD)
    
def happy():
    assert callable(words)
    
def sad():
    assert callable(words)
    
def drink_reccomendations():
    assert callable drink_reccomendations(3) == "Earl Grey Tea"
    assert callable drink_reccomendations(6) == "Matcha"
