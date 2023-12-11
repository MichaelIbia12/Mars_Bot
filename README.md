# Mars_bot 
Hello, this is mars bot. He is a bot that can peform specific tasks for you.

## Getting started

Clone the repo

```
$ git clone https://github.com/MichaelIbia12/Mars_Bot.git
```

Activate the env file
```
$ source env/bin/activate
```
Then
```
$ python bot.py
```

## Features

- Handling of Basic Greeting
- Can identify and search the dictionary
- **More coming soon**

## How it works 
### Initialization

```python
m = Mars()
```
Creates an instance of the Mars class.
### Response Engine

```python
m.response_engine(txt)
```

This method is responsible for generating responses based on user input. It performs the following steps:

    Lemmatization:
        Uses the bulk_lemmatizer method to lemmatize the input text. Lemmatization reduces words to their base or root form.

    Prediction:
        Uses the prediction_engine method to predict the type of the user's statement based on the lemmatized input.
        Chooses a response from the vocabulary based on the prediction.
        Handles personal information, recommendations, and internet connectivity checks.

### Prediction Engine

```python
m.prediction_engine(l)
```

Predicts the type of the user's statement based on the input list of lemmatized words. It evaluates the statement score for each statement type and returns the type with the highest score.

### Information Extractor

```python
m.information_extractor(txt)
```

Extracts information based on user queries. Uses the vocabulary to identify the subject of the query, queries an online dictionary API, and returns relevant information.
### Vocabulary

The Mars class has a vocabulary that contains patterns for greetings, personal information, recommendations, weather, and two fields of study: "food" and "tech."
### Field of Study Keywords

```python
self.fieldOfStudyKeywords = data['vocabulary']['fieldOfStudyKeyWords']
```

Contains keywords related to two fields of study: "food" and "tech."
### While Loop

```python
while True:
    txt = input("#- ")
    print("thinking")
    m.response_engine(txt)
```

Starts an infinite loop where the user can input text. The chatbot processes each input and generates responses until the user decides to exit.
### Recommendations (Incomplete)

```python
def recommendations(self):
    pass
```

The recommendations method is currently incomplete and has a pass statement. You can extend this method to provide recommendations based on user queries or preferences.
Additional Notes

    The chatbot uses the simple_chalk library for colored console output.
    It checks for an internet connection at the beginning to determine whether to make online queries.
    The lemmatization process is used to simplify the input text for better pattern matching.
    
# Buy a coffee
[☕ Buy a coffee 😊]("https://www.buymeacoffee.com/mars.shall")
