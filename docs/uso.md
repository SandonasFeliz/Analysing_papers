# Usar Analysing papers

## Uso sin docker
Ejecutamos GROBID en una terminal:

```bash
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

Una vez que se haya ejecutado Grobid, abrimos otra terminal y seguimos los siguientes pasos:

Si no se ha activado antes, activamos el entorno n¡con conda:

```bash
conda activate ta_env
```
!!! note "Desactivar entorno de conda"
    Para desactivar el entorno de conda, hacemos: `conda deactivate`.

Nos dirigimos a la raíz del proyecto. Definimos variable de entorno para que el script se conecte a GROBID:

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

- Archivos TEI en `data/tei/`
- Wordclouds en `results/`
- Gráfico de conteo de figuras en `results/`
- Extracción de links en `results/`



## Uso con Docker


!!! tip "Uso con Docker"
    Si ha ejecutado el programa sin docker y ahora desea hacerlo con docker, por favor, hágalo en otra terminal. Puede haber fallos.



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

