import scrapy
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from scrapy.utils.project import get_project_settings
from sel_scrapy.sel_scrapy.items import FeijaoItem

class FeijaoSpider(scrapy.Spider):
    name = 'feijao'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def start_requests(self):

        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = ChromeOptions()
        options.headless = True
        navegador = Chrome(executable_path=navegador_path, options=options)
        navegador.get('https://www.minhacooper.com.br/loja/a.verde-bnu/produto/busca?q=feijao')
        sleep(4)
        navegador.find_element('xpath', '//*[@id="variant-list"]/div/div/div/div[4]/div[3]/div[2]/div/a').click()
        sleep(4)
        navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(4)

        xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-variation__name", " " ))]'

        link_elements = navegador.find_elements('xpath', xpath)

        for link_el in link_elements:
            href = link_el.get_attribute("href")
            yield scrapy.Request(href)
        navegador.quit()

    def parse(self, response):
        item = FeijaoItem()
