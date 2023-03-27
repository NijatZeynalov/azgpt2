def clean_oskar_corpus(text):
  
  sentences = text.split(".")


  text = re.sub(r'<.*?>', '', text)  
  text = re.sub(r'[^\w\s]', '', text)  
  text = re.sub(r'\n', '. ', text) 

  pattern = re.compile(r'\b\w*[а-яА-Я]+\w*\b')


  text = pattern.sub("", text)
  text = text.strip()  
  sentences = text.split(". ")

  filtered_sentences = []
  for sentence in sentences:
      if len(sentence) >= 45 and len(sentence)<100:
          filtered_sentences.append(sentence)
  
  filtered_text = ". ".join(filtered_sentences)

  words = filtered_text.split()
  for i in range(len(words)):
      if words[i] == "Copyright":
          filtered_text = " ".join(words[:i-1])
          break

  for i in range(len(words)):
      if words[i] == "Telefon":
          filtered_text = " ".join(words[:i-1])
          break

  words = filtered_text.split()
  new_words = []
  for word in words:
      if not word.startswith("http"):
          new_words.append(word)
  filtered_text = " ".join(new_words)

  
  filtered_text = filtered_text.replace("Bütün hüquqlar qorunur", "")
  return filtered_text
