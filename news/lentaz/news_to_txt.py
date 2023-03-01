# https://drive.google.com/file/d/1ZDVm2i-uuqo12C9WsR2i7rTCHiA5C8MJ/view?usp=share_link

df = pd.read_csv('lent_az_urls.csv')

def news_to_txt(url_list):
    
    for base_url in url_list:
    
        file_name = base_url.split('/')[-1]

        reqs = requests.get(base_url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        mydivs = soup.find("div", {"class": "news_content"})

        with open(f'{file_name}.txt', 'w') as f:
            f.write(mydivs.text)
            
            
n = 50000
for g, chunck_df in df.groupby(np.arange(len(df)) // n):
    news_to_txt(chunck_df['0'])
