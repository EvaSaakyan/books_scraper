from scraper import get_book_data, scrape_books

def test_book_data_type():
    book_url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    result = get_book_data(book_url)
    assert isinstance(result, dict)
    assert 'title' in result
    assert 'price' in result
    assert 'ranking' in result
    assert 'quantity_in_stock' in result
    assert 'description' in result
    assert 'product_information' in result

            
def test_scrape_books():
    result = scrape_books(is_save=False)
    assert isinstance(result, list)
    assert len(result) == 1000
    
    
def test_book_title():
    book_url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    result = get_book_data(book_url)
    assert result['title'] == 'A Light in the Attic'