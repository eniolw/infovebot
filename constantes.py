# -*- coding: utf-8 -*-
# 
# Copyright (C) 2017-2018 Oniel Revilla Morón <eniolw@gmail.com>
# 
# Este software ha sido liberado bajo los términos de la licencia GNU AGPL 3.0
# (véase: https://www.gnu.org/licenses/agpl-3.0.html)
# 
"""Bot de Telegram para la consulta información de servicios públicos 
de Venezuela."""


START_TXT = "¡Hola! Soy un bot para consultar información de algunos servicios " \
            "de Venezuela. Por ahora sólo consulto datos en CANTV y en el IVSS" \
            "\n\nPara CANTV usa el comando /cantv así:\n<code>/cantv " \
            "[código_de_área] [número]</code>\n\nEjemplo: <i>/cantv 268 " \
            "5552525</i>\n\nPara IVSS usa el comando /ivss así:\n<code>/ivss " \
            "[nacionalidad][numero_de_cédula] [dd]/[mm]/[aaaa]</code>" \
            "\n\nEjemplo: <i>/ivss v15000111 01/12/1990</i>" \
            "\n\nEn modo inline Infovebot soporta por ahora la consulta del " \
            "servicio de CANTV con esta sintaxis: " \
            "@infovebot <code>[código_de_área] [número]</code>" \
            "\n\nEjemplo: <i>@infovebot 268 5552525</i>"

ERROR_TXT = "Se produjo un error. Intente luego"

NO_RESULTADO_TXT = "No produjo ningún resultado"

CANTV_INVALIDO_TXT = "<b>Consulta inválida</b>\nDeben ser números compuestos por 10 " \
                     "dígitos.\nLa sintaxis debe ser: XXX XXXXXXX siendo 'X' cualquier " \
                     "dígito. Ejemplo: 268 5552525"

IVSS_INVALIDO_TXT = "<b>Consulta inválida</b>\nLa sintaxis debe ser:\n<code>/ivss " \
                    "[nacionalidad][numero_de_cédula] [dd]/[mm]/[aaaa]</code>\n\nPor " \
                    "ejemplo:\n<i>/ivss v15000111 01/12/1982 </i>"
