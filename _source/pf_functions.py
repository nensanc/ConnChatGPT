import sys

class pf_Object(object):
    def __init__(self):
        self.app = None
    def open_folder(self, carpeta_seleccionada):
        global app
        sys.path.append(carpeta_seleccionada)
        import powerfactory
        self.app = powerfactory.GetApplicationExt()
        python_dir = 'PF '+carpeta_seleccionada.split('/')[-2]+' V.'+carpeta_seleccionada.split('/')[-1]
        self.app.Show()
        return python_dir
    def validate(self,foreignKey, df):
        elm = self.app.SearchObjectByForeignKey(foreignKey)
        pf_values = dict(zip(elm.parameterNames[0].split(','), elm.params))
        d_result = []
        for i in range(df.shape[0]):
            row = df.iloc[i]
            try:
                if float(row[1].strip())==float(pf_values.get(row.get(0).strip())):
                    igual = 'Si'
                else: 
                    igual = 'No'
            except:
                igual = ' - '
            d_result.append(
                {
                    "Variable": row.get(0).strip(),
                    "ValorPDF": row[1].strip(),
                    "ValorDIG": pf_values.get(row.get(0).strip()),
                    'Iguales?': igual
                }
            )
        return d_result
