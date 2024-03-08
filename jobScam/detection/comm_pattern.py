from .nlp import *
import joblib

model = joblib.load("jobScam.joblib")
tfidf_vec = joblib.load("jobVec.pkl")

# Command Interface
class TextAnalysisCommand:
    def execute(self, text):
        pass
    
    def get_result(self):
        pass

# Concrete Command: Sentiment Analysis Command
class PredictCommand(TextAnalysisCommand):
    def execute(self, text):
        # Perform sentiment analysis logic here
        test = tfidf_vec.transform(text)

        predict = model.predict(test)
        
        self.result = predict
        
    def get_result(self):
        return self.result

# Invoker (Button Click Handler)
class TextAnalysisInvoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_analysis(self, text):
        if self.command:
            self.command.execute(text)