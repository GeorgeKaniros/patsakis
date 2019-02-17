from bs4 import BeautifulSoup
import requests

diefthinsi=input("Δωσε μια διευθυνση για ανιχνευση συνδεσμων και αλλαγων γραμμης")
selida=requests.get(diefthinsi)
kodikas=BeautifulSoup(selida.text, 'lxml')

all_gram=0
syndesmoi=0

syn=kodikas.find_all('a')
syndesmoi=len(syn)
brs=kodikas.find_all('br')
ps=kodikas.find_all('p')
all_gram=len(ps)+len(brs)

print("Συνδεσμοι:",syndesmoi)
print("Αλλαγες γραμμης:",all_gram)
