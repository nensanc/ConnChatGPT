import sys

pf_app = None

def init(action, path):
    try:
        sys.path.append(path)
        import powerfactory
        ##-------- Power Factory -------- ##
        global pf_app
        pf_app=powerfactory.GetApplicationExt()
        return 
    except RuntimeError:
        result = {"action":action, "msg": "Conexión Exitosa con Power Fatory", "data":None}
        return {"res":result}, 200
    except:
        result = {"action":action, "msg":"Error en la conexión"}
        return {"res":result}, 500

def show(action, data):
    global pf_app
    pf_app.Show()
    result = {"action":action, "msg":"Aplicación de Power Factory Abierta", "data":None}
    return {"res":result}, 200
def hide(action, data):
    global pf_app
    pf_app.Hide()
    result = {"action":action, "msg":"Aplicación de Power Factory Cerrada", "data":None}
    return {"res":result}, 200