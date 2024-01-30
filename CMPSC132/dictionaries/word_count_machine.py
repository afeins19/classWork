'''
Program Specification:
This program will take a file as input and display information such as
total words, most frequently used words, etc. There is deeper fucnctionality
aswell, such as string searches and organized data structures.
-------------------------------------------------------------------------------
To-do:

-  encapsulate as a class
-  move word processes into __init()__
        - put the 'with open(file=file_adress...)' in __init()__
- ur dumbass didnt use sorted() method for ranking words
and now you got this nut ass for loop and 600 new variables
'''


import string

file_address= ''
distinct_words=dict()
total_words=0

file_address=r'/Users/aaronfeinberg/PycharmProjects/Playground/text_files/bee_movie.txt'

#displays total words, word count, most frequent
def display_dict():
    print('\nTotal Words: '+str(total_words),end='\n')
    print('Distinct words: ' + str(len(distinct_words)), end='\n\n')

    #write dictionary to file -> word_count_doc.txt
    with open("word_count_doc",'w') as export:
        for k,v in sorted(distinct_words.items()):
            export.write('\n'+k+': '+str(v))

#find most frequently used word
def most_frequent_word(word_dict):
    max_val=0
    max_key=''
    for k,v in word_dict.items():
        if v > max_val:
            max_val, max_key= v,k

    #print('\nMost Frequent: '+'"'+max_key+' "'+'is used '+str(max_val)+' times')

    return max_key

#parse file (separate words and remove punctuation) then move into dict
with open(file=file_address) as fobj:
    remove=list(string.punctuation)
    for word in fobj.read().lower().split():
        word = ''.join(c for c in word if c not in remove).lower()
        distinct_words.setdefault(word, 0)
        distinct_words[word]= distinct_words[word] + 1
        total_words+=1


def search_string(user_input=None):
    '''returns # of occurences of speicified word'''
    while(user_input!='exit()'):
        try:
            print('\n'+user_input+ ' is used '+str(distinct_words[user_input])+' times')
        except KeyError:
            return 'Word not found'
        except user_input==None:
            return 'Please input a word...'
        user_input=input("\nPlease input your word (to exit type exit()): ")

def get_freq_words(stop_val=1, verbose=True):
    '''finds most frequently used words up to the stop value'''
    clone_words=distinct_words.copy()
    ranked_dict = {}
    for i in range(stop_val):
        word = most_frequent_word(clone_words)
        ranked_dict[word]=clone_words[word]
        del clone_words[word]

    if verbose:
        print('\nMost Frequent words (stop_val = '+str(stop_val)+'):\n')
        i=0
        for k,v in ranked_dict.items():
            i+=1
            print(str(i)+': '+k+':', str(v))

    return ranked_dict

#Calls go here:
display_dict()
get_freq_words(10, True)
search_string(user_input='')


