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


def aUnicode(obj):
    """
    Para facilitar la conversión a utf-8 en python 2.7
    """

    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            try:
                obj = obj.decode('iso-8859-1').encode('utf8')

            except:
                obj = obj.encode('utf8')

    return obj