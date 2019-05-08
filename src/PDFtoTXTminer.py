from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from utils import utils
import os


def convert_pdf_to_txt(paths=[]):
    pdf_files = utils.get_files_in_path(paths[0])

    if len(pdf_files) <= 0:
        print("No se encontraron documentos pdf en la ruta", paths[0])

    else:
        print("Creando los archivos txt...")
        for file in pdf_files:
            file_path = os.path.join(paths[0], file)
            text_file_name = os.path.join(paths[1], file[:-4] + ".txt")

            print("Creando archivo ", text_file_name)
            txt_file = open(text_file_name, "w", encoding="utf-8")

            pdf_rsc_manager = PDFResourceManager()
            str_io = StringIO()
            codec = 'utf-8'
            laparams = LAParams()
            device = TextConverter(pdf_rsc_manager, str_io, codec=codec, laparams=laparams)
            pdf_file = open(file_path, 'rb')
            interpreter = PDFPageInterpreter(pdf_rsc_manager, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos=set()

            for page in PDFPage.get_pages(pdf_file, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
                interpreter.process_page(page)

            text = str_io.getvalue()

            pdf_file.close()
            device.close()
            str_io.close()

            txt_file.write(text)
