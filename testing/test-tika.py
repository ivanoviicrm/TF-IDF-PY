from tika import parser

raw = parser.from_file("../DocumentosPDF/BOE-A-2019-6770.pdf")
file = open("../DocumentosTXT/test.txt", "w")
file_content = raw["content"]
palabras = file_content.strip().split("\n")

for palabra in palabras:
    file.write(palabra + "\n")
