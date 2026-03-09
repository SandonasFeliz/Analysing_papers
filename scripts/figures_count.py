from lxml import etree
import matplotlib.pyplot as plt
import os

def count_figures(xml_file):
    """
    Cuenta el número de figuras presentes en un archivo TEI XML.

    Parameters
    ----------
    xml_file : str
        Ruta al archivo XML.

    Returns
    -------
    int
        Número de figuras encontradas.
    """

    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

    tree = etree.parse(xml_file)

    figures = tree.xpath('//tei:figure', namespaces=ns)

    return len(figures)


def save_figures_plot(figures_dict, output_folder):

    names = list(figures_dict.keys())
    counts = list(figures_dict.values())

    plt.figure(figsize=(10,5))
    plt.bar(names, counts)
    plt.xticks(rotation=45)
    plt.ylabel("Number of figures")
    plt.title("Figures per article")

    output_path = os.path.join(output_folder, "figures_per_article.png")

    plt.tight_layout()
    plt.savefig(output_path)

    print(f"Gráfico guardado en  {output_path}")