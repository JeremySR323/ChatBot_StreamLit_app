import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def es_usuario_valido(usuario):
    if "@" in usuario and "." in usuario:
        return True
    partes = usuario.strip().split()
    return len(partes) >= 2

def obtener_fecha_actual():
    return datetime.now().strftime("%Y-%m-%d")

def buscar_imagenes_web(consulta):
    query = consulta.replace(" ", "+")
    url = f"https://www.bing.com/images/search?q={query}&form=HDRSC2"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")
    urls = [img["src"] for img in images if img.get("src", "").startswith("http")]
    return urls[:3]