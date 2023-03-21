#kishiyev, 21.03
import re

class TextCleaner:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def clean_text(self):
        with open(self.input_file_path, 'r') as file:
            text = file.read()
        
        #Remove formatting (or metadata)
        text = re.sub(r'^[^\w\n]+|[^\w\n]+$', '', text, flags=re.MULTILINE)

        #Unwanted characters
        text = re.sub(r'[^\w\s]|_+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()

        #Remove noise
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'www\S+', '', text)

        #Non-Azerbaijani Words
        #text = re.sub(r'\b(?!(?:[a-zA-Z]|ç|ə|ı|i|ö|ü)+\b)\w+\b', '', text) 
        text = re.sub(r'\b(?![a-zA-ZşçəğıİöüÖÜ]+)\w+\b', '', text)
        
        self.cleaned_text = text
    
    def save_text(self):
        with open(self.output_file_path, 'w') as file:
            file.write(self.cleaned_text)

        print(f"Cleaned text at {self.output_file_path}")
    
if __name__ == '__main__':
    input_file = 'Balet_librettolari_XIX_esr-XX_esrin_evveli.txt'
    output_file = 'output.txt'

    clean = TextCleaner(input_file, output_file)
    clean.clean_text()
    clean.save_text()
