import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    # convert word to lower case
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0 :
        new = input("did you mean %s instead. type y if yes and n if no:" % get_close_matches(word, data.keys())[0])  
        new = new.lower()

        if new == 'y':
            return data[get_close_matches(word, data.keys())[0]] 
        elif new == 'n':
            return 'Sorry, the word entered was not found'    
        else :
            return 'Please Type Y/N only'  
    else :
        return 'The word entered is wrong, please recheck and type again'


enter = input('Enter your word here:')
means = meaning(enter)
print(means)         
       

