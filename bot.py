import json
import random
from simple_chalk import green, red
import requests
import nltk
from nltk.stem import WordNetLemmatizer


internet_connection = True

print(green("Updating/Installing Nltk Packages"))

try:
    requests.get("http://google.com")
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')
    print(green("Initializing"))
except:
    internet_connection = False
    print(red("No internet connection"))
    quit()
file = open('data/vocabulary.json')
data = json.load(file)
lemmatizer = WordNetLemmatizer()


class Mars():
    def __init__(self):
        self.age = 0
        self.name = 'Mars'
        self.vocabulary = data['vocabulary']['data']

    # engine responsinle for responding

    def response_engine(self, txt: str):
        simplified_text = self.bulk_lemmatizer(txt)
        statment_arr = simplified_text.lower().split()
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
                meaning = self.information_extractor(txt)
                response += " " + meaning

            if internet_connection:
                print(green(response))
            else:
                print(red("no internet"))

    # engine responsible for pediction of statement type
    def prediction_engine(self, l: list):
        # evaluating statment score

        prediction_list = []

        for statment_type in self.vocabulary:
            prediction_score = 0
            for data in self.vocabulary[statment_type]:
                for refrence_sentence in data:
                    for word in l:
                        if word in refrence_sentence.lower().split(" "):
                            prediction_score += 1

            prediction_list.append((statment_type, prediction_score))

        main_scores = []
        for stastment_tupl in prediction_list:
            score = stastment_tupl[1]
            main_scores.append(score)

        max_score = max(main_scores)
        if max_score == 0:
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

        subjects = []
        for data in self.vocabulary["information_and_knowledge"][0]:
            if len(txt.split(data.lower())) >= 2:
                uknown, subject = txt.split(data.lower())
                subjects.append(subject.strip())

        if internet_connection:
            dic_req = requests.get(dictionary_api+subjects[0]).json()

            if dic_req is dict and dic_req['title'] == "No Definitions Found":
                print("Searching the web")

                meaning = " "
                return meaning
            else:
                definition = dic_req[0]["meanings"][0]
                partofspeach = definition['partOfSpeech']
                definitions = []
                example = []
                for i in definition['definitions']:
                    definitions.append(i['definition'])
                    if 'example' in i:
                        example.append(i['example'])

                meaning = f"""
                {subjects[0]} : {partofspeach}
                
                1: {definitions[0]} 
                example: {example[0]}
                
                2: {definitions[1]} 
                example: {example[1]}
                
                """

                return meaning
        else:
            print(red("Please connect to an internet connection"))

    def bulk_lemmatizer(self, text: str):
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
    m.response_engine(txt)
