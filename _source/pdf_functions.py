import PyPDF2
import re
from openai import OpenAI
from pandas import DataFrame
class pdf_Object(object):
    def __init__(self):
        self.d_pdf_num_text = {} # diccionario que meustra todas las paginas. 
        self.client = OpenAI(api_key='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')
        self.GPT_MODEL = "gpt-4-1106-preview" #"gpt-3.5-turbo-1106"
        self.chat_history = []
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
        if 'Q-1.' in text:
            numbers = re.findall(r'\d+', text)
            return self.d_pdf_num_text[int(numbers[1])]
        elif 'Q-2.' in text:
            numbers = re.findall(r'\d+', text)
            pdf_text = self.d_pdf_num_text[int(numbers[1])]
            message = f"devuelve la tabla {numbers[2]} como un archivo csv separado por ; en '{pdf_text}'"
            return self.chastGPTMessage(message)
        elif 'Q-3.' in text:
            numbers = re.findall(r'\d+', text)
            pdf_text = self.d_pdf_num_text[int(numbers[1])]
            message = f"devuelve la tabla {numbers[2]} como un archivo csv separado por ; en '{pdf_text}'"
            tabla_text = self.chastGPTMessage(message)
            datos = []
            for line in tabla_text.split('\n'):
                if len(line.split(';'))>1:
                    datos.append(line.split(';'))
            df = DataFrame(datos)
            return str(df)

    def chastGPTMessage(self, message):
        self.chat_history.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.GPT_MODEL,
            messages=self.chat_history,
            max_tokens=1500)
        full_reply_content = response.choices[0].message.content  # extract the message
        self.chat_history.append({"role": "assistant", "content": full_reply_content})
        # print the time delay and text received
        return full_reply_content.split('```')[1]
