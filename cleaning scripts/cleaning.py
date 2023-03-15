import re

def clean(file_name):
    # Open the input file and read its contents
    with open(file_name, "r", encoding="utf8") as f:
        text = f.read()
    text = re.sub("<.*?>", "", text)
    text = re.sub("\S+@\S+", "", text)
    text = re.sub("https?:\/\/\S+", "", text)
    text = re.sub("[^a-zA-Z0-9\sƏəŞşÇçĞğÖöIıÜü]+", "", text)
    text = re.sub("(^|\. )[A-Z][a-z]+( [a-z]+)*\.", "\\1", text)
    text = re.sub(r"\b(istinadən|əsasən|məlumatına görə|məlumata görə)\b", "", text)
    text = re.sub(r"[^a-zA-Z0-9]+", ' ', text)

    return text

input_file = "file1.txt"
output_file = "cleaned.txt"
cleaned_text = clean(input_file)

with open(output_file, "w", encoding="utf8") as f:
    f.write(cleaned_text)
    
print(f"Cleaned text in {output_file}")