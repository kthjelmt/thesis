from chatterbot import ChatBot

chatbot = ChatBot(
    'SE-Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
 #       'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',

        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."]

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_level1 = open('training_data/level1.txt').read().splitlines()
#training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_level1 #+ training_data_personal

trainer.train(training_data)

# Training With Corpus
#from chatterbot.trainers import ChatterBotCorpusTrainer

#trainer_corpus = ChatterBotCorpusTrainer(chatbot)

#trainer_corpus.train('chatterbot.corpus.english')
