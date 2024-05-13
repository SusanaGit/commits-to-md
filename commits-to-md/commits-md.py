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

def creacion_archivo_md(diccionario_commits_obtenidos):
    with open(nombre_archivo_md, 'w') as objeto_archivo_abierto_md:

        # título del .md
        objeto_archivo_abierto_md.write("# " + titulo + "\n")

        # escribimos cada commit del diccionario en el archivo md
        for commit in reversed(diccionario_commits_obtenidos):
            titulo_commit = f"{commit['commit']['message']}"
            url_commit = f"https://github.com/{usuario_git}/{repositorio_git}/commit/{commit['sha']}"
            objeto_archivo_abierto_md.write("### ["+titulo_commit+"]" + "("+url_commit+")")
            objeto_archivo_abierto_md.write("\n")

def ejecucion():
    datos()
    creacion_archivo_json()
    diccionario_commits_obtenidos = creacion_diccionario_commits()
    creacion_archivo_md(diccionario_commits_obtenidos)