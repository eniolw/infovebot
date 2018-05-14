# -*- coding: utf-8 -*-
# 
# Copyright (C) 2017-2018 Oniel Revilla Morón <eniolw@gmail.com>
# 
# Este software ha sido liberado bajo los términos de la licencia GNU AGPL 3.0
# (véase: https://www.gnu.org/licenses/agpl-3.0.html)
# 
"""Bot de Telegram para la consulta información de servicios públicos 
de Venezuela."""


START_TXT = "😃 ¡Hola! Soy un bot para consultar información de algunos servicios" \
            " de Venezuela. Por ahora sólo consulto datos de facturación en CANTV" \
            " y los datos de la cuenta individual en el IVSS." \
            " Para más información usa el comando /help o /ayuda."

HELP_TXT = "📌 Por ahora soporto los siguientes <b>comandos</b>:" \
           "\n<code>/cantv &#60;código_de_área&#62; &#60;número&#62;" \
           "</code>\nEjemplo: <i>/cantv 268 5552525</i>" \
           "\n\n<code>/ivss &#60;nacionalidad&#62;&#60;numero_de_cédula&#62;" \
           " &#60;dd&#62;/&#60;mm&#62;/&#60;aaaa&#62;</code>" \
           "\nEjemplo: <i>/ivss v15000111 01/12/1990</i>" \
           "\n\n<code>/start</code> o <code>/inicio</code>:" \
           " muestra un mensaje de presentación." \
           "\n\n<code>/help</code> o <code>/ayuda</code>: muestra este mensaje." \
           "\n\nEn modo inline InfoVeBot soporta por ahora la consulta del" \
           " servicio de CANTV con esta sintaxis:" \
           " @infovebot <code>&#60;código_de_área&#62; &#60;número&#62;</code>" \
           "\númeroEjemplo: <i>@infovebot 268 5552525</i>"

ERROR_TXT = "😅 Se produjo un error. Intente luego"

NO_RESULTADO_TXT = "😢 No produjo ningún resultado"

CANTV_INVALIDO_TXT = "❌ <b>Consulta inválida</b>\nDeben ser números compuestos por 10" \
                     " dígitos.\nLa sintaxis debe ser: XXX XXXXXXX siendo 'X' cualquier" \
                     " dígito. Ejemplo: 268 5552525"

IVSS_INVALIDO_TXT = "❌ <b>Consulta inválida</b>\nLa sintaxis debe ser:\n<code>/ivss" \
                    " &#60;nacionalidad&#62;&#60;numero_de_cédula&#62; " \
                    "&#60;dd&#62;/&#60;mm&#62;/&#60;aaaa&#62;</code>\n\nPor" \
                    " ejemplo:\n<i>/ivss v15000111 01/12/1982 </i>"
