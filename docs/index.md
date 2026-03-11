# Welcome to Analysing papers

Para ver el repisotrio de GitHub, pulse aquí: [Repositorio en GitHub](https://github.com/SandonasFeliz/Analysing_papers).

- Project name: Analysing papers
- Author: Janele Sandonas Feliz
- Version: 3.0
- License: MIT
- Keywords: PDF analysis, TEI, wordcloud, figures, links, GROBID

Este proyecto permite analizar papers en PDF, extraer abstracts, generar wordclouds, contar figuras y extraer enlaces externos.

Nota: los PDFs no están incluidos por copyright. Debes colocarlos en data/pdf/ para ejecutar el pipeline. Posteriormente se explicará la esctrutura de este proyecto, de manera que se pueda facilitar su uso.

## Estructura
A continuación, se explica la estructura que se tiene que tener para usar este repositorio. 
```
data/
    pdf/     ← Coloca tus PDFs aquí
    tei/     ← Se generará automáticamente
results/     ← Resultados del pipeline
scripts/     ← Código principal
test/        ← Tests de ejemplo
Dockerfile
docker-compose.yml
environment.yml
README.md
docs/
mkdocs.yml
.readthedocs.yaml

```

!!! note "Crear carpetas necesarias"
    Se deben crear las siguientes carpetas:
     - data
     - data/pdf
     -data/tei
     - results


## GROBID (GeneRation Of BIbliographic Data)
Este proyecto utiliza GROBID (GeneRation Of BIbliographic Data) para convertir PDFs académicos a formato TEI.
### Instalación de GROBID con Docker
Para la instalación de GROBID en Docker.
```bash
docker pull lfoppiano/grobid:0.7.2
```
Para ejecutar, hacemos:
```bash
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```




