from lxml import etree
import os

def filter_external_links(xml_file):
    """
    Extrae los enlaces externos presentes en un archivo TEI.

    Parameters
    ----------
    xml_file : str
        Ruta al archivo TEI XML.

    Returns
    -------
    list
        Lista de URLs encontradas en el documento.
    """

    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

    tree = etree.parse(xml_file)

    links = tree.xpath('//tei:ref/@target', namespaces=ns)

    # Filtrar solo links externos
    external_links = [link for link in links if link.startswith("http")]

    return external_links


def save_links(links_dict, output_folder):

    output_file = os.path.join(output_folder, "links.txt")

    with open(output_file, "w", encoding="utf8") as f:

        for paper, links in links_dict.items():

            f.write(paper + "\n")

            for link in links:
                f.write("  " + link + "\n")

            f.write("\n")

    print(f"Los links se han guardado en  {output_file}")