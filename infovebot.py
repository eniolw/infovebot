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
from modelo.infovemodelo import Cantv, Ivss, ConsultaError
from vista.infovevista import VistaHome, VistaCantv, VistaIvss
from util.util import fechaValida
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

    if not re.match("^[0-9]{3}[0-9]{7}$", cadena):
        VistaCantv.verConsultaErronea(update)
        return

    cantv = Cantv()
    try:
        resultados = cantv.obtenerDeuda(cadena[0:3], cadena[3:10])

    except ConsultaError:
        VistaHome.verError(update)
        return

    VistaCantv.verConsulta(update, resultados)


def consultarIvss(bot, update, args):
    """
    Controlador del comando buscar para consultar datos en Ivss
    """

    if not len(args) == 2 \
    or not re.match("^[V|E|T|v|e|t][0-9]{6,8}$", args[0]) \
    or not fechaValida(args[1]):

        VistaIvss.verConsultaErronea(update)
        return

    ivss = Ivss()

    try:
        resultados = ivss.obtenerCuenta(args[0][0],
                                        args[0][1:],
                                        args[1][0:2],
                                        args[1][3:5],
                                        args[1][6:10])

    except ConsultaError:
        VistaHome.verError(update)
        return

    VistaIvss.verConsulta(update, resultados)


def inlinequery(bot, update):
    """
    Controlador de las peticiones inline. Por ahora sólo gestiona la consulta
    de información en Cantv
    """

    query = update.inline_query.query

    if not re.match("^[0-9]{3} [0-9]{7}$", query):
        return

    partes = query.split()

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
    dp.add_handler(CommandHandler("cantv", consultarCantv, pass_args=True))
    dp.add_handler(CommandHandler("ivss", consultarIvss, pass_args=True))
    dp.add_handler(InlineQueryHandler(inlinequery))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()