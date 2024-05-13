import json
import subprocess


def datos():
    global titulo, usuario_git, repositorio_git, nombre_archivo_json, nombre_archivo_md
    titulo = input("Introduce el título que tendrá el .md que quieres generar: ")
    usuario_git = input("Introduce el usuario de Git que contiene el repositorio: ")
    repositorio_git = input("Introduce el repositorio del que quieres obtener los commits: ")
    nombre_archivo_json = "commits_" + repositorio_git + ".json"
    nombre_archivo_md = "commits_" + repositorio_git + ".md"

def creacion_archivo_json():
    subprocess.run(["curl", "-s", f"https://api.github.com/repos/{usuario_git}/{repositorio_git}/commits", "-o",
        nombre_archivo_json])

def creacion_diccionario_commits():
    with open(nombre_archivo_json, 'r') as objeto_archivo_abierto_json:
        # cargamos el contenido del archivo abierto json al diccionario_commits_obtenidos
        diccionario_commits_obtenidos = json.load(objeto_archivo_abierto_json)
        return diccionario_commits_obtenidos

