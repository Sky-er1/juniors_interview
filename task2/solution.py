import re
from collections import defaultdict

import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://ru.wikipedia.org/'
FiRST_URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

russian_letters = re.compile('^[А-Яа-яЁё]$')


def get_animal_list(url: str):
    letter_counts = defaultdict(int)
    while url:
        print(f'Текущая страница: {url}')
        res = requests.get(url=url)
        soup = BeautifulSoup(res.text, 'lxml')
        animal_groups = soup.find_all('div',
                                      class_='mw-category mw-category-columns')
        for animal_group in animal_groups:
            animals = animal_group.find_all('a', title=True)
            for animal in animals:
                animal_name = animal.get('title')
                first_letter = animal_name[0].upper()
                if not russian_letters.match(first_letter):
                    return letter_counts
                letter_counts[first_letter] += 1

        next_page = soup.find('a', string='Следующая страница')
        if next_page:
            relative_url = next_page.get('href')
            url = BASE_URL + relative_url if relative_url.startswith(
                '/') else relative_url
        else:
            url = None
    return letter_counts


def write_csv(letter_counts: dict):
    with open(f'beats.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for letter, count in sorted(letter_counts.items()):
            writer.writerow([letter, count])


if __name__ == '__main__':
    counts = get_animal_list(FiRST_URL)
    write_csv(counts)
