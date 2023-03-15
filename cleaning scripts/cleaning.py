"""
kishiyev, 15/03/2023
"""
import re

def clean(file_name):
    # Open the input file and read its contents
    with open(file_name, "r", encoding="utf8") as f:
        text = f.readline()
    text = re.sub("<.*?>", "", text)
    text = re.sub("\S+@\S+", "", text)
    text = re.sub("https?:\/\/\S+", "", text)
    text = re.sub("[^a-zA-Z0-9\s]+", "", text)
    text = re.sub("(^|\. )[A-Z][a-z]+( [a-z]+)*\.", "\\1", text)
    text = re.sub("(^|\n)[^\n]*(\n[^\n]*)+", "\\1", text)
        
    return text

input_file = "file2.txt"
output_file = "cleaned.txt"
cleaned_text = clean(input_file)

with open(output_file, "w", encoding="utf8") as f:
    f.write(cleaned_text)
    
print(f"Cleaned text in {output_file}")