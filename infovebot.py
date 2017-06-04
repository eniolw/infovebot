# -*- coding: utf-8 -*-
"""
Copyright 2017 Oniel Revilla Morón (eniolw@gmail.com)
Bot de Telegram para la consultar información de servicios de Venezuela.

Este software ha sido liberado bajo los términos de la licencia GNU AGPL 3.0
(véase: https://www.gnu.org/licenses/agpl-3.0.html)

Para la construcción de este bot se han portado y modificado algunos scripts de
https://github.com/willicab/infove-api por William Cabrera
<cabrerawilliam@gmail.com>
"""

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from modelo.infovemodelo import Cantv, ConsultaError
from vista.infovevista import VistaHome, VistaCantv
import re


def start(bot, update):
    """
    Controlador del comando start
    """

    VistaHome.verStart(update)


def help(bot, update):
    """
    Controlador del comando help
    """

    VistaHome.verStart(update)


def consultarCantv(bot, update, args):
    """
    Controlador del comando buscar para consultar datos en Cantv
    """

    cadena = "".join(args)

    if len(cadena) != 10 or not re.match("\d\d\d\d\d\d\d\d\d", cadena):
        VistaCantv.verConsultaErronea(update)
        return

    cantv = Cantv()
    try:
        resultados = cantv.obtenerDeuda(cadena[0:3], cadena[3:10])

    except ConsultaError:
        VistaHome.verError(update)
        return

    VistaCantv.verConsulta(update, resultados)


def inlinequery(bot, update):
    """
    Controlador de las peticiones inline. Por ahora sólo gestiona la consulta
    de información en Cantv
    """

    query = update.inline_query.query

    if not len(query) == 11 or not re.match("\d\d\d\s\d\d\d\d\d\d", query):
        return

    partes = query.split()
    if len(partes) != 2:
        return

    cantv = Cantv()
    try:
        resultados = cantv.obtenerDeuda(partes[0], partes[1])

    except ConsultaError:
        VistaHome.verError()

    VistaCantv.verConsultaInline(update, resultados)


def main():
    """
    Función principal. Crea el bot, asigna los manejadores y lo ejecuta
    """

    updater = Updater("TU_TOKEN")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("buscar", consultarCantv, pass_args=True))
    dp.add_handler(InlineQueryHandler(inlinequery))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()