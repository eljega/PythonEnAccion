"""
visualizacion de actividad de commits en repositorio Git

Descripcion:
este script genera un histograma que muestra la actividad de commits en un proyecto Git,
indicando la frecuencia de commits a lo largo del tiempo. seria util para visualizar la intensidad
del trabajo en el proyecto tanto para equipos grandes como para desarrolladores individuales.

Instrucciones de uso:
1. instalar dependencias, GitPython y matplotlib instalados.
2. modifica la variable 'ruta_de_repositorio' con la ruta a tu repositorio local.
3. ejecuta este script para generar el histograma.

"""
# Dependencias:
from git import Repo
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import Counter
from datetime import datetime

# Ruta al repositorio local
ruta_de_repositorio = 'configura la ruta'

# Inicializar el repositorio
repo = Repo(ruta_de_repositorio)

fechas_commits = []

# Obtener fechas de commits
for commit in repo.iter_commits():
    fechas_commits.append(commit.committed_datetime.date())

# Contamos los commits por fechas
contador_fechas = Counter(fechas_commits)
fechas = list(contador_fechas.keys())
commits = list(contador_fechas.values())

# Convertirmos fechas a formato matplotlib
fechas = [mdates.date2num(datetime.strptime(str(fecha), '%Y-%m-%d')) for fecha in fechas]

fig, ax = plt.subplots(figsize=(10, 5))

# Creamos el histograma
ax.bar(fechas, commits, width=10, color='skyblue')

ax.xaxis_date()
plt.xticks(rotation=45)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.title('Actividad de Commits en el Repositorio')
plt.xlabel('Tiempo')
plt.ylabel('Número de Commits')
plt.tight_layout()

plt.show()
