from bs4 import BeautifulSoup
import requests

def scrape():
    url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    
    pokemonEntries = soup.find_all('td', style='font-family:monospace,monospace')

    for entry in pokemonEntries:
        parent = entry.find_parent('tr')

        entryNumber = parent.find('td', {
            'style':'font-family:monospace,monospace'
            }).text.strip()
        entryName = parent.find('a', title=lambda value: value and ' (Pokémon)' in value).text.strip()

        with open('pokedexBin.text', 'a', encoding='utf-8') as file:
            file.write(f'{entryNumber} - {entryName}\n')

scrape()
