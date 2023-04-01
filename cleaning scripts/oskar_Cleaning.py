
from datasets import load_dataset

access_token = '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'

ds_oscar = load_dataset('oscar-corpus/OSCAR-2201', 'az', split="train", use_auth_token=access_token)
import uuid
import re


def clean_oskar_corpus(text):

    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\n', '. ', text)
    substrings = text.split()  # split the string into a list of substrings

    output_string = ""

    for substring in substrings:
        if len(substring) > 50:
            output_string += " "  # add a space to separate words
        else:
            output_string += substring + " "  # add the substring to the output string with a space

    text = output_string.strip()
    pattern = re.compile(r'\b\w*[а-яА-Я]+\w*\b')

    text = pattern.sub("", text)
    text = text.strip()
    sentences = text.split(". ")

    filtered_sentences = []
    for sentence in sentences:
        if len(sentence) >= 45 and len(sentence) < 100:
            filtered_sentences.append(sentence)

    filtered_text = ". ".join(filtered_sentences)

    words = filtered_text.split()
    for i in range(len(words)):
        if words[i] == "Copyright":
            filtered_text = " ".join(words[:i - 1])
            break

    for i in range(len(words)):
        if words[i] == "Telefon":
            filtered_text = " ".join(words[:i - 1])
            break

    words = filtered_text.split()
    new_words = []
    for word in words:
        if not word.startswith("http"):
            new_words.append(word)
    filtered_text = " ".join(new_words)

    filtered_text = filtered_text.replace("Bütün hüquqlar qorunur", "")
    return filtered_text


for i in range(len(ds_oscar)):
    name = str(uuid.uuid4())
    if len(clean_oskar_corpus(ds_oscar[i]['text']))>0:
        with open(f"oskar/{name}.txt", "w") as f:
            f.write(clean_oskar_corpus(ds_oscar[i]['text']))

