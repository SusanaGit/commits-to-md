
def datos():
    global titulo, usuario_git, repositorio_git, nombre_archivo_json, nombre_archivo_md
    titulo = input("Introduce el título que tendrá el .md que quieres generar: ")
    usuario_git = input("Introduce el usuario de Git que contiene el repositorio: ")
    repositorio_git = input("Introduce el repositorio del que quieres obtener los commits: ")
    nombre_archivo_json = "commits_" + repositorio_git + ".json"
    nombre_archivo_md = "commits_" + repositorio_git + ".md"