import requests
from bs4 import BeautifulSoup

def get_book_data(book_url: str) -> dict:
    """
    Сбор информации о книге с указанной веб-страницы.
    
    Входные аргументы:
        book_url (str): url страницы книги
    
    Возвращаемые значения:
    
    При успешном запросе:
        book_data (dict): словарь, содержащий:
            title (str): название книги,
            price (str): цена книги,
            ranking (int): рейтинг книги от 1 до 5,
            quantity_in_stock (int): количество экземпляров книги в наличии,
            description (str): описание книги,
            product_information (dict): словарь, содержащий доп.характеристики из таблицы Product Information
    
    При неуспешном запросе:
        сообщение об ошибке и пустой словарь
            
    """

    # НАЧАЛО ВАШЕГО РЕШЕНИЯ
    response = requests.get(book_url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').get_text().strip()
        price = soup.find('p', attrs={'class': 'price_color'}).get_text()
        ranking = soup.find('p', attrs={'class': 'star-rating'})
        ranking_text = ranking['class'][1]
        ranking_num = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        ranking = ranking_num[ranking_text]
        in_stock = soup.find('p', attrs={'class': 'instock availability'}).get_text().strip()
        if 'In stock' in in_stock:
            quantity_text = in_stock.split('(')[1]
            quantity_text = quantity_text.split()[0]
            quantity_in_stock = int(quantity_text)
        else:
            quantity_in_stock = 0
        description = soup.find('div', attrs={'id': 'product_description'})
        if description is not None:
            description = description.find_next('p').get_text().strip()
        else: 
            description = ''
        product_information = {}
        for row in soup.find_all('tr'):
            features_name = row.find('th').get_text()
            features_value = row.find('td').get_text()
            product_information[features_name] = features_value
        book_data = {
            'title': title,
            'price': price,
            'ranking': ranking,
            'quantity_in_stock': quantity_in_stock,
            'description': description,
            'product_information': product_information
        }
        
        return book_data
    
    else:
        print('Ошибка запроса')
        return {}
    
    # КОНЕЦ ВАШЕГО РЕШЕНИЯ

    
def scrape_books(is_save: bool = False):
    """
    Сбор информации обо всех книгах из каталога books.toscrape.com.
    
    Входные аргументы:
        is_save (bool): аргумент-флаг, отвечающий за сохранение результата в файл.
           при True данные сохраняются в файл books_data.txt,
           при False не сохраняется
    
    Возвращаемые значения:
        books_data (list): список словарей с информацией о книгах, полученной с помощью get_book_data
    """

    # НАЧАЛО ВАШЕГО РЕШЕНИЯ
    books_data = []
    for page in range(1, 51):
        page_url = f'https://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(page_url)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            books_on_page = soup.find_all('h3')
            for book in books_on_page:
                book_link = book.find('a')
                book_href = book_link['href']
                book_url = 'https://books.toscrape.com/catalogue/' + book_href
                book_data = get_book_data(book_url)
                books_data.append(book_data)
    if is_save:
        with open('artifacts/books_data.txt', 'w', encoding='utf-8') as f:
            f.write(str(books_data))
    return books_data

    # КОНЕЦ ВАШЕГО РЕШЕНИЯ