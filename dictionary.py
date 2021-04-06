import json
from difflib import get_close_matches
import sys

data = json.load(open('word_list.json'))
sys_arg = sys.argv[1:]
sys_input = ' '.join(sys_arg)


def translate_word(w):
    """Find definition of the words in the data dict

    Args:
        words (string): words that you want to find
    
    Return:
        value of the key(words) in the data    
    """
    w_lower = w.lower()
    if w in data or w_lower in data:
        if w.islower():
            return '%s: ' %w_lower.title() + '\n'.join(data[w_lower])
        else:
            return '%s: ' %w + '\n'.join(data[w])
    
    else:
        return 'Sorry, we could not find the word you mean'


def check_match(word):
    """Find the closest match of the word if the word
    doesn't exist

    Args:
        word (string): word that you want to find
    
    Return:
        the word you mean
    """   
    matches = get_close_matches(word, data.keys())
    if len(matches) > 0:
        for item in matches:
            print(f'Did you mean {item}?')
            ans = input('Y / N? ').upper()
            if ans == 'Y':
                return item
            elif ans == 'N':
                continue
            else:
                print("Incorrect answer.")
                break
    
    else:
        return 'a'


def main_program():
    """[Main Program]
    Take a user input and pass it to the dictionary
    """    
    print("""
           Welcome to the Py Dictionary
       ===================================
        We'll search a definition for you
          """)
    
    while True:
        ui = input('Enter a word or type e to exit: ')
        print('=========================================')
        if ui == 'e':
            print('Goodbye!')
            break
        
        elif (ui in data) or (ui.lower() in data):
            print('\n' + translate_word(ui) + '\n')
            
        else:
            ui = check_match(ui.lower())
            print('\n' + translate_word(ui) + '\n')


# capturing input from command line or argv                      
if len(sys_arg) != 0:
    if (sys_input in data) or (sys_input.lower() in data):
        print('\n' + translate_word(sys_input) + '\n')
        quit()
            
    else:
        sys_input = check_match(sys_input.lower())
        print('\n' + translate_word(sys_input) + '\n')
        quit()

elif len(sys_arg) == 0 and __name__ == ('__main__'):               
    main_program()        
    