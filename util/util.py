# -*- coding: utf-8 -*-


def fechaValida(fecha):
    """
    Para validar la fecha ingresada
    """

    from datetime import datetime

    formato = "%d/%m/%Y"
    try:
        fecha = datetime.strptime(str(fecha), formato)

    except:
        return False

    return True