

# Analysing_papers
[![DOI](https://zenodo.org/badge/1176906870.svg)](https://doi.org/10.5281/zenodo.18929491)


- **Project name:** Analysing papers
- **Author:** Janele Sandonas Feliz
- **Version:** 3.0
- **License:** MIT
- **Keywords:** PDF analysis, TEI, wordcloud, figures, links, GROBID


**Documentación:** [https://analysing-paper.readthedocs.io/es/latest/](https://analysing-paper.readthedocs.io/es/latest/)


Este proyecto permite analizar papers en PDF, extraer abstracts, generar wordclouds, contar figuras y extraer enlaces externos.  

> **Nota**: los PDFs **no están incluidos** por copyright. Debes colocarlos en `data/pdf/` para ejecutar el pipeline.

## Estructura

```
docs/
data/
    pdf/     ← Coloca tus PDFs aquí
    tei/     ← Se generará automáticamente
results/     ← Resultados del pipeline
scripts/     ← Código principal
test/        ← Tests de ejemplo
environment.yml
README.md
mkdocs.yml
readthedocs.yaml
```
> **Nota**: Se deben crear las carpetas `data/` con las subcarpetas `pdf/` y `tei/`. También se debe crear la carpeta `results/`.

### Preparar el entorno para usuarios

Para ejecutar tu propio análisis:
1. Crear carpetas locales necesarias:
```bash
mkdir -p data/pdf data/tei results
```
2. Colocar tus PDFs en `data/pdf/`.

## Dependencia: GROBID

Este proyecto utiliza **GROBID (GeneRation Of BIbliographic Data)** para convertir PDFs académicos a formato TEI.

- Repositorio GitHub: https://github.com/kermitt2/grobid

### Instalación de GROBID con Docker

```bash
docker pull lfoppiano/grobid:0.7.2
```
Ejecutamos GROBID:

```bash
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
Levantamos el servicio en `http://localhost:8070`.

## Instalación
1. Clonación de repositorio
Primero, clonamos el repositorio. 

```bash
git clone https://github.com/SandonasFeliz/Analysing_papers.git
```

2. Crear el entorno Conda desde `environment.yml`:

```bash
conda env create -f environment.yml
conda activate ta_env
```
### Dependencias

- Python 3.11
- lxml
- numpy
- matplotlib
- wordcloud
- requests
- Otros paquetes especificados en environment.yml

3. Instalción de GROBID
   Como se explicó antes, para instalar Grobid, hacemos:
```bash
docker pull lfoppiano/grobid:0.7.2
```

## Uso
Una vez que se haya ejecutado Grobid. Abrimos otra terminal y seguimos los siguientes pasos:

Definir variable de entorno para que el script se conecte a GROBID:

- Linux/macOS
  ```bash
  export GROBID_URL=http://localhost:8070/api/processFulltextDocument
  ```
- Windows CMD
  ```bash
  set GROBID_URL=http://localhost:8070/api/processFulltextDocument
  ```
  
 Ejecutar el pipeline principal:
```bash
python scripts/run_pipeline.py
```
El pipeline se saltará automáticamente los pasos si no hay PDFs en data/pdf.

Genera:
- Archivos TEI en data/tei/
- Wordclouds en results/
- Gráfico de conteo de figuras en results/
- Extracción de links en results/


## Tests
Ejecutar tests en la raíz del proyecto:

```bash
python -m unittest discover tests
```
> **Nota**: El test que verifica el funcionamiento de wordcloud `test_wordcloud.py` genera una imagen en `test/`.

## Integración Continua
El workflow ejecuta:

1. Creación temporal de carpetas necesarias (data/pdf, data/tei, results)
2. Instalación de dependencias desde environment.yml
3. Ejecución del pipeline (si hay PDFs)
4. Ejecución de tests automáticos

   
## Uso con Docker
Realizamos los siguientes pasos desde la raíz del proyecto:
```bash
docker-compose build --no-cache
docker-compose up
```
Con eso, ya tenemos nuestra imagen de Grobid instalada y el entorno creado con Conda.
A su vez, podremos ver como se ejecuta el programa principal: `python scripts/run_pipeline.py`.
Para parar, solamente debe escribir:
```bash
docker-compose down
```

## Citation

Si usas este proyecto, por favor cita:

GROBID: GeneRation Of BIbliographic Data. https://github.com/grobidOrg/grobid

