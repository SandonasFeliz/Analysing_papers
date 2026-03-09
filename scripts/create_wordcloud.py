import os
import glob
from lxml import etree
from wordcloud import WordCloud

def extract_abstract_texts(tei_folder):
    """
    Extrae el texto de los abstracts de todos los archivos TEI XML
    dentro de una carpeta.

    Parameters
    ----------
    tei_folder : str
        Ruta a la carpeta que contiene los archivos TEI XML.

    Returns
    -------
    list
        Lista con los fragmentos de texto encontrados en los abstracts.
    """

    tei_files = glob.glob(os.path.join(tei_folder, "*.xml"))
    all_abstracts = []

    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

    for file in tei_files:
        try:
            tree = etree.parse(file)

            # Extrae todo el texto dentro del abstract
            abstracts = tree.xpath('//tei:abstract//tei:p//text()', namespaces=ns)

            if abstracts:
                all_abstracts.extend(abstracts)

        except Exception as e:
            print(f"Error leyendo {file}: {e}")

    return all_abstracts


def generate_wordcloud(text, output_folder, filename="abstract_wordcloud.png", show=False):
    """
    Genera una nube de palabras a partir de un texto.

    Parameters
    ----------
    text : str
        Texto combinado de todos los abstracts.
    output_folder : str
        Carpeta donde se guardará la imagen.
    filename : str
        Nombre del archivo de salida.
    show : bool
        Si es True muestra la imagen en pantalla.
    """

    os.makedirs(output_folder, exist_ok=True)

    wc = WordCloud(width=800, height=400, background_color="white").generate(text)

    output_path = os.path.join(output_folder, filename)
    wc.to_file(output_path)

    print(f"Nube de palabras guardada en: {output_path}")