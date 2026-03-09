import os
import glob

from pdf_to_tei import convert_pdfs_to_tei
from create_wordcloud import extract_abstract_texts, generate_wordcloud
from figures_count import count_figures, save_figures_plot
from extract_links import filter_external_links, save_links


# Carpetas del proyecto
pdf_folder = "data/pdf"
tei_folder = "data/tei"
results_folder = "results"

os.makedirs(results_folder, exist_ok=True)


# 1️Convertir PDFs → TEI
print("\nEjecutando...")
print("\nConvirtiendo PDFs a TEI")

convert_pdfs_to_tei(pdf_folder, tei_folder)



# 2️Wordcloud 

print("\nCreando wordcloud")

abstracts = extract_abstract_texts(tei_folder)

if abstracts:
    text = " ".join(abstracts)
    generate_wordcloud(text, results_folder, show=False)
else:
    print("No se encontraron abstracts.")



# 3️Conteo de figuras

print("\nContando figuras...")

"""
tei_files = glob.glob(os.path.join(tei_folder, "*.xml"))

for file in tei_files:
    num_figures = count_figures(file)

    print(f"{os.path.basename(file)}: {num_figures} figuras")
"""

tei_files = glob.glob(os.path.join(tei_folder, "*.xml"))

figures_dict = {}

for file in tei_files:
    num_figures = count_figures(file)

    paper_name = os.path.basename(file)

    print(f"{paper_name}: {num_figures} figuras")

    figures_dict[paper_name] = num_figures


# guardar gráfico
save_figures_plot(figures_dict, results_folder)



# 4️Extracción de links
"""
print("\nExtrayendo links...")

for file in tei_files:
    links = filter_external_links(file)

    print(f"\n{os.path.basename(file)} ({len(links)} links):")

    for link in links:
        print(" -", link)


print("\nPipeline completado.")
"""
print("\nExtrayendo links...")

links_dict = {}

for file in tei_files:

    paper_name = os.path.basename(file)

    links = filter_external_links(file)

    print(f"\n{paper_name} ({len(links)} links):")

    for link in links:
        print(" -", link)

    links_dict[paper_name] = links


# guardar links
save_links(links_dict, results_folder)

print("\nProceso completado.")