import scrapy
from scrapy.spider import BaseSpider
from scrapy.http import Request

class CinemexSpider(scrapy.Spider):
    name = "cines" # Nombre de mi Scrapeador
    allowed_domains = ['cinemex.com'] # Lista de dominios permitidos
    custom_settings = {
        "DOWNLOAD_DELAY": 1   # 1000 milisegundos de retraso para cada peticion
        #"CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }
    
    def start_requests(self):
        for i in range(1,33): # Un Request para cada Estado de la Republica
            yield Request('https://cinemex.com/cines/%d' % i,
                    callback=self.parse_2, meta={'index':i})

    def parse_2(self, response):
	cines = response.css('li.cinema-item') # "Lista" de todos los cines de un Estado
	for cine in cines: # Para cada cine en mi "lista" de cines, vamos a guardar un registro
		coordenada = ''.join(cine.css('::attr(data-pos)').extract()) # Mi coordenada es una lista, la convertimos a string
		yield {
			'id': response.meta['index'], # Indice del estado
			'estado': response.css('div.sidebar-heading span::text').extract(), # Nombre del estado
			'direccion' : cine.css('::attr(data-address)').extract(), # Direccion del estado
			'lat' : coordenada.split(',',1)[0], # Separamos lo que esta a la izquierda de la coma
							    # (en mi variable coordenada) y lo guardamos como latitud 
			'lon' :	coordenada.split(',',1)[1], # Lo que esta a la derecha de la coma, es la longitud

			# Codigo viejo:		
			#'coordenadas' : cine.css('::attr(data-pos)').extract(),
			#'direccion': response.css('li.cinema-item::attr(data-address)').extract(),
			#'coordenadas': response.css('li.cinema-item::attr(data-pos)').extract(),	
		}

