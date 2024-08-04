from datetime import datetime
import requests
from bs4 import BeautifulSoup

def scrape_whois(domain_name):
    url = f"https://www.ps.kz/domains/whois/result?q={domain_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    def extract_text(element):
        return element.get_text(strip=True) if element else None

    whois_data = {}
    
    rows = soup.find_all('tr')
    for row in rows:
        key_element = row.find('td', class_='valign-top')
        value_element = row.find_all('td')[1] if key_element else None

        if key_element and value_element:
            key = key_element.get_text(strip=True)
            if key == 'Доменное имя:':
                whois_data['domain_name'] = extract_text(value_element.find('b'))
            elif key == 'Статус:':
                whois_data['status'] = [extract_text(b) for b in value_element.find_all('b')]
            elif key == 'Регистратор:':
                whois_data['registrar'] = extract_text(value_element.find('b'))
            elif key == 'Регистрант:':
                whois_data['registrant'] = extract_text(value_element)
            elif key == 'Административный\nконтакт:':
                whois_data['administrative_contact'] = extract_text(value_element)
            elif key == 'Серверы имен:':
                whois_data['name_servers'] = [extract_text(b) for b in value_element.find_all('b')]
            elif key == 'Создан:':
                whois_data['created'] = extract_text(value_element).split('(')[0].strip()
            elif key == 'Последнее изменение:':
                whois_data['last_modified'] = extract_text(value_element).split('(')[0].strip()
            elif key == 'Дата окончания:':
                whois_data['expiry_date'] = extract_text(value_element).split('(')[0].strip()

    return whois_data
