from PyPDF2.pdf import PdfFileReader


def getDataUsingPyPdf2(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""

    for i in range(0, pdf.getNumPages()):
        #print(str(i))
        extractedText = pdf.getPage(i).extractText()
        content += extractedText + "\n"

    content = " ".join(content.replace("\xa0", " ").strip().split())
    return content.encode("ascii", "ignore")


print(getDataUsingPyPdf2("../DocumentosPDF/BOE-A-2019-6770.pdf"))
