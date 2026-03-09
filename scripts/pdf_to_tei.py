import requests
import glob
import os

def convert_pdfs_to_tei(pdf_folder, tei_folder, grobid_url="http://localhost:8070/api/processFulltextDocument"):
    """
    Convierte archivos PDF en archivos TEI XML utilizando el servicio GROBID.

    Parameters
    ----------
    pdf_folder : str
        Carpeta donde se encuentran los PDFs.
    tei_folder : str
        Carpeta donde se guardarán los archivos TEI.
    grobid_url : str
        URL del servicio GROBID.
    """

    os.makedirs(tei_folder, exist_ok=True)

    pdf_files = glob.glob(os.path.join(pdf_folder, "*.pdf"))

    print(f"Se han encontrado {len(pdf_files)} PDFs.")

    for pdf_file in pdf_files:

        print(f"Procesando: {os.path.basename(pdf_file)}")

        with open(pdf_file, "rb") as f:
            files = {"input": f}
            response = requests.post(grobid_url, files=files)

        if response.status_code == 200:

            output_file = os.path.join(
                tei_folder,
                os.path.basename(pdf_file).replace(".pdf", ".xml")
            )

            with open(output_file, "w", encoding="utf-8") as out:
                out.write(response.text)

            print(f"Guardado en : {output_file}")

        else:
            print(f"Error procesando {pdf_file} (status {response.status_code})")

    print("La conversión PDF → TEI ha finalizado.")