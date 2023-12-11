import PyPDF2
import re

class pdf_Object(object):
    def __init__(self):
        self.d_pdf_num_text = {} # diccionario que meustra todas las paginas. 
    def open_pdf(self, archivo_pdf_full_name):
        pdf_file = open(archivo_pdf_full_name, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            # Get the page object for the current page number
            page = pdf_reader.pages[page_num]
            # Extract the text from the page
            text = page.extract_text()
            self.d_pdf_num_text[page_num+1] = text.strip()
        name_pdf = archivo_pdf_full_name.split('/')[-1]
        return name_pdf
    def text_rule(self, text):
        if 'Mostrar la pagina'.lower() in text.lower():
            patron = r'\{(\d+)\}'
            number = re.search(patron, text)
            return self.d_pdf_num_text[int(number.group(1))]
