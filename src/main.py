import PDFtoTXT
import PDFtoTXTminer
import tf_idf
import os
from config import config
from utils import utils
from collections import OrderedDict


def ask_for_paths():
    pdf_directory = config.DEFAULT_PDF_PATH
    txt_directory = config.DEFAULT_TXT_PATH

    print("El directorio de lectura de los documentos pdf por defecto es: " + config.DEFAULT_PDF_PATH)
    print("El directorio de escritura de los documentos txt por defecto es: " + config.DEFAULT_TXT_PATH)
    change = input("Desea cambiar alguna de estas rutas? [y | n] \n")

    if change == "y" or change == "Y":
        pdf_path = input("Introduca el directorio de los documentos PDF (Intro = default): \n")
        if len(pdf_path) > 0:
            pdf_directory = pdf_path

        txt_path = input("Introduca el directorio de los documentos TXT (Intro = default): \n")
        if len(txt_path) > 0:
            txt_directory = txt_path

    print("Directorio PDF --> " + pdf_directory)
    print("Directorio TXT --> " + txt_directory)

    return [pdf_directory, txt_directory]


def ask_for_lib():
    print("Las librerias disponibles para extraer TXT de documentos PDF son: ")
    print("\t [0] - PDFMiner.six  (recomendada)")
    print("\t [1] - PyPDF2")
    change = input("Seleccione libreria [ 0 | 1 ] \n")

    if change == "0":
        print("Libreria PDFMiner.six seleccionada")
    elif change == "1":
        print("Libreria PyPDF2 seleccionada")
    else:
        print("No seleccionó una libreria correcta, por defecto se usará PDFMiner.six...")
        change = "0"

    return change


def get_idf():
    print("Calculando tf-idf...")

    count_dictionary = {}
    txt_files = utils.get_files_in_path(config.DEFAULT_TXT_PATH, extension="txt")

    for file in txt_files:
        text = utils.read_txt(os.path.join(config.DEFAULT_TXT_PATH, file))
        tf_dictionary = tf_idf.calculate_tf(text)
        count_dictionary = tf_idf.calculate_occurrences(tf_dictionary, count_dictionary)

    return tf_idf.calculate_idf(count_dictionary, len(txt_files))


def save_idf_data(paths=[], idf_dict={}):
    with open(os.path.join(paths[1], "idf_data.txt"), "w", encoding="utf-8") as file:
        for word in idf_dict:
            file.write(word + "\t" + str(idf_dict[word]) + "\n")


def main():
    paths = ask_for_paths()
    lib = ask_for_lib()

    if lib == "0":
        PDFtoTXTminer.convert_pdf_to_txt(paths)
    elif lib == "1":
        PDFtoTXT.convert_pdf_to_txt(paths)

    # Obtengo el idf
    idf_dict = get_idf()

    # Ordeno alfabéticamente el diccionario
    ordered_d_as_list = sorted(idf_dict.items(), key=lambda x: x[0])
    idf_dict = OrderedDict(ordered_d_as_list)

    # Muestro el resultado del tf-idf:
    for word in idf_dict:
        print(word, idf_dict[word])

    # Guardo data en un txt
    save_idf_data(paths, idf_dict)


if __name__ == "__main__":
    main()
