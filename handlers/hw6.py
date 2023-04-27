import bs4
import requests
import xlsxwriter

main_url = 'https://trade59.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
data = [['Наименование','Цена','Ссылка', 'Картинка']]

def get_soup(url):
    res = requests.get(url, headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')


categories_page = get_soup(main_url+'catalog.html?cid=7')
categories = categories_page.findAll('a', class_='cat_item_color')
for cat in categories:
    subcategories_page = get_soup(main_url+cat ['href'])
    subcategories = subcategories_page.findAll('a', class_='cat_item_color')
    for subcat in subcategories
        iphones_page = get_soup(main_url+subcat{'href'})
        iphones = iphones_page.findAll('div', class = 'items-list')
        for iphone in iphones:
            title = iphone.find('a')['title'].strip()
            price = iphone.find('div', class_='price').find(text=True).strip()
            url = iphone.find('a')['href'].strip()
            img = iphone.find('div', class_='image')['style'].split('url'(')[1].split(')')[0].replace('/tn/', '/source/')
        data.append([title, price, url, img])


        with xlswriter.Workbook('iphone.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, info in enumerate(data):
                worksheet.write_row(row_num, 0, info)











