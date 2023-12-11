
import PyPDF2

pdf_path = "D:\Admin BaseDig\Temporales\Proyecto Revisión Informes Desempeño 2023\documento.pdf"
pdf_file = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

def get_table(text):
    if 'Tabla ' in text:
        print(text)
        return True
    return False


result_file = open(pdf_path.replace('.pdf','_Result4.txt'),'w', encoding='utf-8')
table_data = []
for page_num in range(len(pdf_reader.pages)):
    if page_num==115:
        result_file.write(f'\npage_num_{page_num}\n')
        print(f'\npage_num_{page_num}\n')
        # Get the page object for the current page number
        page = pdf_reader.pages[page_num]
        # Extract the text from the page
        text = page.extract_text() 

        # get tables
        is_table = get_table(text)
        # Split the text into lines
        result_file.write(text)

        if is_table: break