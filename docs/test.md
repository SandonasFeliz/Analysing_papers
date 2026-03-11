# Tests e integración continua

## Tests

!!! warning "Atención"
    Solo se pueden hacer los test con la ejecución sin Docker.

Existe la carpeta `tests/data`, donde se guardan archivos de ejemplos. Solo para usos de testeo. 

Para ejecutar los test, hacemos lo siguiente en la raíz del proyecto.

```bash
python -m unittest discover tests
```
1. Archivo: `tests/test_links.py` -> Comprueba que los links extraídos empiezan con `http` o `https`.
2. Archivo: `tests/test_pdf.py` -> Comprueba que el archivo existe y tiene extensión `.pdf`.
3. Archivo: `tests/test_figures` -> Ver que XML de pruba tiene 2 figuras.
4. Archivo: `tests/test_wordcloud.py` -> Comprueba que la imagen se genera correctamente. 

!!! warning "Test de wordcloud"
    La imagen se genera en la misma carpeta de `tests/`.




## Integración Continua
El workflow ejecuta:

1. Creación temporal de carpetas necesarias (data/pdf, data/tei, results)
2. Instalación de dependencias desde environment.yml
3. Ejecución del pipeline (si hay PDFs)
4. Ejecución de tests automáticos
