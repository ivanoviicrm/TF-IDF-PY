from utils import utils
import PyPDF2
import os


def convert_pdf_to_txt(paths=[]):
    pdf_files = utils.get_files_in_path(paths[0])

    if len(pdf_files) <= 0:
        print("No se encontraron documentos pdf en la ruta", paths[0])

    else:
        print("Creando los archivos txt...")
        for file in pdf_files:
            file_path = os.path.join(paths[0], file)
            stream = open(file_path, "rb")
            object_reader = PyPDF2.PdfFileReader(stream)

            file_total_pages = object_reader.getNumPages()
            text_file_name = os.path.join(paths[1], file[:-4] + ".txt")
            print("Creando archivo ", text_file_name, "Paginas: ", file_total_pages)
            txt_file = open(text_file_name, "w", encoding="utf-8")
            for i in range(0, file_total_pages):
                page_content = object_reader.getPage(i).extractText()
                txt_file.write(page_content + "\n")
