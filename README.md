# Analysing_papers
Este proyecto permite analizar papers en PDF, extraer abstracts, generar wordclouds, contar figuras y extraer enlaces externos.  

> Nota: los PDFs **no están incluidos** por copyright. Debes colocarlos en `data/pdf/` para ejecutar el pipeline.


## Instalación

1. Crear el entorno Conda desde `environment.yml`:

```bash
conda env create -f environment.yml
conda activate grobid-env
