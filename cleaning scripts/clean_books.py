#kishiyev, 21.03 (updated)
import os
import re

class TextCleaner:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

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
        text = re.sub(r'\b(?![a-zA-ZşçəğıİöüÖÜ]+)\w+\b', '', text)
        
        #"w"
        #text = re.sub(r'\b\w*w\w*\b', '', text) 
        
        self.cleaned_text = text
    
    def save_text(self):
        output_file_path = os.path.splitext(self.input_file_path)[0] + '_cleaned.txt'
        with open(output_file_path, 'w') as file:
            file.write(self.cleaned_text)

        print(f"Cleaned text at {output_file_path}")
    
if __name__ == '__main__':
    input_folder = '/content/my_data' #any file directory we provide

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            input_file_path = os.path.join(input_folder, file_name)
            clean = TextCleaner(input_file_path)
            clean.clean_text()
            clean.save_text()
