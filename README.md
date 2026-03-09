# Analysing_papers
Este proyecto permite analizar papers en PDF, extraer abstracts, generar wordclouds, contar figuras y extraer enlaces externos.  

> **Nota**: los PDFs **no están incluidos** por copyright. Debes colocarlos en `data/pdf/` para ejecutar el pipeline.


## Instalación

1. Crear el entorno Conda desde `environment.yml`:

```bash
conda env create -f environment.yml
conda activate grobid-env
```

## Estructura

```
data/
    pdf/     ← Coloca tus PDFs aquí
    tei/     ← Se generará automáticamente
results/     ← Resultados del pipeline
scripts/     ← Código principal
test/        ← Tests de ejemplo
environment.yml
README.md
```
> **Nota**: Se deben crear las carpetas `data/` con las subcarpetas `pdf/` y `tei/`. También se debe crear la carpeta `results/`.

## Uso
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

Ejecutar tests con archivos de ejemplo:

```bash
python -m unittest discover test
```
> **Nota**: Hay test que requieren poner un pdf en `test/data/`.
> El test que verifica el funcionamiento de wordcloud genera una imagen en `test/`.

## Integración Continua
El workflow ejecuta:

1. Creación temporal de carpetas necesarias (data/pdf, data/tei, results)
2. Instalación de dependencias desde environment.yml
3. Ejecución del pipeline (si hay PDFs)
4. Ejecución de tests automáticos

> **Nota**: No requiere subir PDFs ni carpetas vacías para funcionar.

## Dependencias

- Python 3.11
- lxml
- numpy
- matplotlib
- wordcloud
- requests
- Otros paquetes especificados en environment.yml

## Preparar el entorno para usuarios

Para ejecutar tu propio análisis:
1. Crear carpetas locales necesarias:
```bash
mkdir -p data/pdf data/tei results
```
2. Colocar tus PDFs en data/pdf/
3. Ejecutar el pipeline principal:
   
```bash
python scripts/run_pipeline.py
```

4. Ejecutar tests opcionalmente:

```bash
python -m unittest discover test
```


