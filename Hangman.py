import My_Lib as lib
import Constants as const

  
word_to_guess = lib.choose_a_word()
found_letters =[]
remains= const.TRIES
    

while remains > 0:
    
    letter = lib.input_letter()
    
    if letter in word_to_guess:
        
        found_letters.append(letter)
        
    remains = (remains-1)
    
    print("\r\n",lib.show_word_to_guess(word_to_guess,found_letters))

        

