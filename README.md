# ScrapyCinemex

Ejemplo de Scrapy, para scrapear la información de los cines (Estado, Dirección, Latitud, Longitud) de cinemex.com

El script principal con el código relevante se encuentra en:

**Cinemex -> spiders -> cinemex_spider.py**

En la carpeta del proyecto, ejecutar en la terminal:

>scrapy crawl cines -o cines_prueba.csv

En esta versión, el archivo .csv ya contempla un registro por cine.

### Recursos

Para instalar Python 3.6: http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/

Para instalar Pip (manejar de paquetes para Python): https://www.rosehosting.com/blog/how-to-install-pip-on-ubuntu-16-04/

Para instalar Scrapy: https://scrapy.org/

Introducción a Scrapy: https://doc.scrapy.org/en/latest/intro/tutorial.html
