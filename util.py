# -*- coding: utf-8 -*-
# 
# Copyright (C) 2017-2018 Oniel Revilla Morón <eniolw@gmail.com>
# 
# Este software ha sido liberado bajo los términos de la licencia GNU AGPL 3.0
# (véase: https://www.gnu.org/licenses/agpl-3.0.html)
# 
"""Bot de Telegram para la consulta información de servicios públicos 
de Venezuela."""


def fecha_valida(fecha):
    """
    Para validar la fecha ingresada
    """

    from datetime import datetime

    formato = "%d/%m/%Y"
    try:
        fecha = datetime.strptime(str(fecha), formato)

    except:
        return False

    else:
        return True


def a_unicode(obj):
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