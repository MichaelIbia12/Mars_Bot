import json
import random 
from simple_chalk import green, red
import time
import requests
import nltk

nltk.download('averaged_perceptron_tagger') 
nltk.download('punkt')   

file = open('data/vocabulary.json')
data = json.load(file)

class Mars():
    def __init__(self):
        self.age = 0
        self.name = 'Mars'
        self.vocabulary = data['vocabulary']['data']
    
    #engine responsinle for responding    
    def response_engine(self, txt:str):
    
        statment_arr =  txt.split()
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
                        if word in refrence_sentence:
                            prediction_score += 1
            
            prediction_list.append((statment_type, prediction_score))
        
        main_scores = []
        for stastment_tupl in prediction_list:
             score = stastment_tupl[1]
             main_scores.append(score)
        
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
        print(pos_tags)
m = Mars()

while True:
    txt = input("#- ")
    print("thinking")
    time.sleep(1)
    m.response_engine(txt)        