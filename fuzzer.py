#opermite ejecutar el programa con opciones sin modificar el codigo
import argparse
#podriamos guardar los resultados en csv para poder abrirlos con excel
import csv
#permite conecion mediante sockets
import socket
# se usa para introducir pasar entre las peticiones para evitar bloqueos
import time
#permite hacer varias tareas en paralelo (acepta )
from concurrent.futures import ThreadPoolExecutor, as_completed
#permite analizar la url en host, puerto ruta y parametros
from urllib.parse import urlsplit , urlunsplit

#request para peticiones
import requests



