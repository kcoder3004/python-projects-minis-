import random 
from collections import Counter 
  
someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
  
someWords = someWords.split(' ') 

word = random.choice(someWords) 
  
if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a fruit') 
  
    for i in word: 
        
        print('_', end=' ') 
    print() 
