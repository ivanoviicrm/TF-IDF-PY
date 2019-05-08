from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def convert_pdf_to_txt(path):
    pdf_rsc_manager = PDFResourceManager()
    str_io = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(pdf_rsc_manager, str_io, codec=codec, laparams=laparams)
    pdf_file = open(path, 'rb')
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
    return text


print(convert_pdf_to_txt("../DocumentosPDF/BOE-A-2019-6771.pdf"))
