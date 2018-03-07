import Constants
import random


def choose_a_word():
    return random.choice(Constants.WORD_LIST)


def input_letter():
    letter = input("give me a letter: ").lower()
    
    if letter.isalpha() and (len(letter) == 1): #est_ce_que lettre une lettre et < a 1
        return letter
    
    else :
        return input_letter()



def show_word_to_guess(word_to_find,found_letters): #word_to_find parametre, found_letters est une liste 
    word_to_show="" #liste qui sera le mot a montrer ex: t**i pour taxy
    for letter in word_to_find: #balayage des lettres de la chaine de caracteres word_to_find
        
        if letter in found_letters:  #la lettre input est une lettre du mot
            word_to_show = word_to_show+letter #alors l ajouter a la liste
            
        else :
            word_to_show = word_to_show+"*"  #si lettre pas dans la liste alors mettre "_"
            
    return word_to_show