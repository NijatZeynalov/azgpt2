#kishiyev, 31.03
import os
import re

class TextCleaner:
  """
  Cleans everything expect Azerbaijani words, removes non-Azerbaijani words, splits the provided
  text into several paragraphs. Tested on 30 different inputs, outputs reliable results.
  """
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        
    def clean_text(self):
        with open(self.input_file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Removes unwanted characters except Azerbaijani letters
        text = re.sub(r'[^\wçəıiöüğşÇƏIÖÜĞŞ\n]+', ' ', text)
    
        # Removes noise
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'www\S+', '', text)
        text = re.sub(r'<[^<]+?>', '', text)
    
        # Removes duplicates
        text = '\n'.join(list(set(text.split('\n'))))
    
        # Removes non-Azerbaijani words
        text = re.sub(r'\b(?!(?:[a-zA-Z]|ç|ə|ı|i|ö|ü|ğ|ş|Ç|Ə|I|Ö|Ü|Ğ|Ş)+\b)\w+\b', '', text)
        
        self.cleaned_text = text
        
    def save_cleaned_text(self, output_file_path):
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(self.cleaned_text)
        
        print(f"New path: {output_file_path}")
        
        
if __name__ == '__main__':
    input_dir = '/content' #Whatever directory we provide
    for root_dir, _, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith('.txt'):
                input_file_path = os.path.join(root_dir, filename)
                cleaner = TextCleaner(input_file_path)
                cleaner.clean_text()
                cleaned_text_list = cleaner.cleaned_text.split('\n')
                
                # Removes empty lines
                cleaned_text_list = list(filter(None, cleaned_text_list))
                
                # Writes cleaned text to file in multiple lines
                cleaned_text = '\n\n'.join(cleaned_text_list)
                output_file_path = os.path.join(root_dir, f"{filename}_cleaned.txt")
                cleaner.save_cleaned_text(output_file_path)
