# Usa Miniconda como base
FROM continuumio/miniconda3

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos de tu proyecto al contenedor
COPY . /app

# Crea el entorno Conda desde environment.yml
RUN conda env create -f environment.yml

# Configura el PATH para que el entorno sea usado por defecto
ENV PATH /opt/conda/envs/ta_env/bin:$PATH

# Comando por defecto
CMD ["python", "scripts/run_pipeline.py"]