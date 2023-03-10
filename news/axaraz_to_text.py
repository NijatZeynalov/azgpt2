
from tqdm import tqdm
import gzip, json

from datasets import load_dataset
dataset = load_dataset("nijatzeynalov/azerbaijani-multi-news")

your_path = 


for i in tqdm(range(len(dataset['train']['text']))):
    text_file = open(f"{your_path}/axar_az_txts/data{i}.txt", "w")
    text_file.write(dataset['train'][i]['text'])
    text_file.close()


for i in tqdm(range(len(dataset['test']['text']))):
    text_file = open(f"{your_path}/axar_az_txts/data_test{i}.txt", "w")
    text_file.write(dataset['test'][i]['text'])
    text_file.close()


for i in tqdm(range(len(dataset['validation']['validation']))):
    text_file = open(f"{your_path}/axar_az_txts/data_validation{i}.txt", "w")
    text_file.write(dataset['validation'][i]['text'])
    text_file.close()

