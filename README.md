# Mars_bot 

Hello, this is mars bot. He is a bot that can peform specific tasks for you.

## Getting started

Clone the repo

```bash
$ git clone https://github.com/MichaelIbia12/Mars_Bot.git
```

Activate the env file
```bash
$ source env/bin/activate
```
Then
```bash
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

This method is responsible for generating responses based on user input. 

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

The recommendations method is currently incomplete and has a pass statement. You can extend this method to provide recommendations based on user queries or preferences

# Buy a coffee
<a href="https://www.buymeacoffee.com/mars.shall">☕ Buy a coffee 😊<a>