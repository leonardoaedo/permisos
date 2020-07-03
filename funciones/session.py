def estaLogeado(request):
        if request.session.get('usuario',False):
                #Una vez que sepas lo del tiempo de session, aca debes pisar la "ultima actividad"
                return True
        else:
                return False
