import requests
from bs4 import BeautifulSoup
import schedule
import time


def webscrapping_69b():
    """
    Functions that get the list from Sat Web.
    """
    url_page='http://omawww.sat.gob.mx/cifras_sat/Paginas/datos/vinculo.html?page=ListCompleta69B.html'
    try:
        response = request.get(url_page)
        response.raise_for_status()
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')

        link_list = soup.find('a', href=lambda href: href and href.endswith('Listado_Completo_69-B.csv.csv'))

        response_csv = requests.get(link_list["href"])
        response_csv.raise_for_status()

        return response_csv.content

    except requests.exceptions.HTTPError as e:
        print(f"Error de HTTP en la solicitud: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Error en obtener la lista: {e}")


def schedule_list(hr='06:00'):
    """
    Functions that recibe the hr to check list,
    and execute webscraping function.
    """
    schedule.every().day.at(hr).do(webscrapping_69b)
