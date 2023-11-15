import json
import random 
from simple_chalk import green, red
import time
import requests
import nltk
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
import threading

print(green("Updating/Installing Nltk Packages"))

nltk.download('averaged_perceptron_tagger') 
nltk.download('punkt')   
nltk.download('words')         

print(green("Initializing"))

file = open('data/vocabulary.json')
data = json.load(file)
lemmatizer = WordNetLemmatizer()

class Mars():
    def __init__(self):
        self.age = 0
        self.name = 'Mars'
        self.vocabulary = data['vocabulary']['data']
        self.dictionary = set(words.words())

    #engine responsinle for responding    
    def response_engine(self, txt:str):
        simplified_text = self.bulk_lemmatizer(txt)
        print(simplified_text)
        statment_arr =  simplified_text.lower().split()
        prediction = self.prediction_engine(statment_arr)
        if prediction == 404:
            print(red("I didnt get that"))
        else:
            statment_type = prediction[0]   
            personal_split = statment_type.split("_")   
            response_arr = self.vocabulary[statment_type][1]
            
            randomInt = random.randrange(-1, len(response_arr))
            response = response_arr[randomInt]

            
            if 'personal' in personal_split:
                match personal_split[1]:
                    case "name":
                        response += " "+self.name
            if 'information' in personal_split:
                self.information_extractor(txt)
            print(green(response))
    
    # engine responsible for pediction of statement type 
    def prediction_engine(self, l:list):
        #evaluating statment score
        prediction_list = []
        for statment_type in self.vocabulary:
            prediction_score = 0
            for data in self.vocabulary[statment_type]:
                for refrence_sentence in data:
                    for word in l:
                        if word in refrence_sentence and word in self.dictionary:
                            prediction_score += 1
    
            prediction_list.append((statment_type, prediction_score)) 
        main_scores = []
        for stastment_tupl in prediction_list:
             score = stastment_tupl[1]
             main_scores.append(score)
        
        print(prediction_list)
        max_score = max(main_scores)
        if max_score == 0 :
            return 404
        else:
            max_score_index = main_scores.index(max_score)
            return prediction_list[max_score_index]
        
    def information_extractor(self, txt):
        
        dictionary_api = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        google = "https://www.google.com"
        bing = "https://www.bing.com/search?q="
        yahoo = "https://search.yahoo.com/search?p="
        summerization_api = "https://api.meaningcloud.com/summarization-1.0"
        
        # find the subject of the sentence
        txt_token = nltk.word_tokenize(txt) 
        pos_tags = nltk.pos_tag(txt_token)
        pos_arr = []
        
        # pre-Noun prase
        for i in range(0 ,len(pos_tags)):
            if "VB" in pos_tags[i][1]:
                word = lemmatizer.lemmatize(pos_tags[i][0], "v")
                word_token = nltk.word_tokenize(word)
                pos_arr.append(word_token)
            elif "NN" in pos_tags[i][1]:
                word = lemmatizer.lemmatize(pos_tags[i][0], "n")
                word_token = nltk.word_tokenize(word)
                pos_arr.append(word_token)
            elif "JJ" in pos_tags[i][1]:
                word = lemmatizer.lemmatize(pos_tags[i][0], "a")
                word_token = nltk.word_tokenize(word)
                pos_arr.append(word_token)
            else:
                pos_tags.append(pos_tags[i][1])
        
        self.subject_finder(pos_arr)
               
        print(pos_tags, txt)
        print(pos_arr)
        
    def subject_finder(self, pos_list:list):
        try:
            verb = pos_list.index("VB")
            preposition = pos_list.index("IN")
            print(verb, preposition)
        except ValueError:
            print("VB,IN not found") 
            
    def bulk_lemmatizer(self, text:str):
        txt = []
        filtered_Arr = []
        noun_lemma = lemmatizer.lemmatize(text, "n")
        verb_lemma = lemmatizer.lemmatize(text, "v")
        for noun_word in noun_lemma.split():
            for verb_word in verb_lemma.split():
                if len(noun_word) > len(verb_word):
                    txt.append(noun_word)
                elif len(verb_word) > len(noun_word):
                    txt.append(verb_word)
                elif len(noun_word) == len(verb_word):
                      txt.append(noun_word)
        print(txt)
        for word in txt:
            if word not in filtered_Arr:
                filtered_Arr.append(word)
            else:
                pass
            
        return " ".join(filtered_Arr)
                    

m = Mars()

while True:
    txt = input("#- ")
    print("thinking")
    time.sleep(1)
    m.response_engine(txt)        