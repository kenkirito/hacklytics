import time
from flask import Flask

app = Flask(__name__)

@app.route('/submit')
def get_current_time():
    return {'time': time.time()}




import math
import string
import sys

app = Flask(__name__)

#read text file, will return a list of lines of text in file
def read_file(filename):
    try:
        with open(filename, 'r') as f: 
            data = f.read() 
        return data 
      
    except IOError: 
        print("Error opening or reading input file: ", filename) 
        sys.exit()

#split text lines into words
#make upper to lower case and puncuation to space
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase)

#return list of the words in the file
def get_words_from_line_list(text):  
    text = text.translate(translation_table) 
    word_list = text.split() 
    #print(word_list)
    return word_list 


#count frequency each word
#returns dictionary which maps the words to thier frequency
def count_frequency(word_list):  
      
    D = {} 
      
    for new_word in word_list: 
          
        if new_word in D: 
            D[new_word] = D[new_word] + 1
              
        else: 
            D[new_word] = 1
              
    return D


# returns dictionary of (word, frequency) pairs from the previous dictionary. 
def word_frequencies_for_file(filename):  
      
    line_list = read_file(filename) 
    word_list = get_words_from_line_list(line_list) 
    freq_mapping = count_frequency(word_list)
    percent = len(freq_mapping)/len(word_list)
  
    print("File", filename, ":", ) 
    print("There are a total of ",len(word_list), "words, and ", len(freq_mapping), "distinct words.", ) 
    if (percent > 0.7):
        print("Since the percentage of distinct words is over 70%, you are not in a filter bubble!")
    else:
        print("Since the percentage of distinct words is less than 70%, you are in a filter bubble!")
  
    return 


word_frequencies_for_file("C:/Users/betzy/Documents/filter_bubble_text.txt")
word_frequencies_for_file("C:/Users/betzy/Documents/non_filter_bubble_text.txt")