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
    def get_paramter_dict(self,foreignKey):
        elm = app.SearchObjectByForeignKey(foreignKey)
        return dict(zip(elm.parameterNames, elm.params))
