# Instalación


## Clonación de repositorio
Primero, clonamos el [repositorio de GitHub](https://github.com/SandonasFeliz/Analysing_papers). 

```bash
git clone https://github.com/SandonasFeliz/Analysing_papers.git
```

## Creación del entorno de Conda

!!! tip "Entorno de Conda"
    Para este proyecto, solo se ha tenido en cuenta la creación de entrono virtual con Conda. 

Para crear este entorno, necesitamos `environment.yml`. Hacemos lo siguiente:
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

## Instalación de GROBID 
Instalamos GROBID. Para la instalación de GROBID en Docker.
```bash
docker pull lfoppiano/grobid:0.7.2
```

