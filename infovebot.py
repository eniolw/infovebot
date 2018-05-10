# -*- coding: utf-8 -*-
# 
# Copyright (C) 2017-2018 Oniel Revilla Morón <eniolw@gmail.com>
# 
# Este software ha sido liberado bajo los términos de la licencia GNU AGPL 3.0
# (véase: https://www.gnu.org/licenses/agpl-3.0.html)
# 
"""Bot de Telegram para la consulta información de servicios públicos 
de Venezuela."""


import re
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

import constantes
from infoveapi import infove_api
from util import a_unicode, fecha_valida


def comando_start(bot, update):
    """
    Controlador del comando start
    """

    update.message.reply_text(constantes.START_TXT, parse_mode="HTML")


def comando_help(bot, update):
    """
    Controlador del comando help
    """

    update.message.reply_text(constantes.START_TXT, parse_mode="HTML")


def comando_cantv(bot, update, args):
    """
    Controlador del comando para consultar datos en Cantv
    """

    cadena = "".join(args)

    if not re.match("^[0-9]{3}[0-9]{7}$", cadena):
        update.message.reply_text(constantes.CANTV_INVALIDO_TXT, parse_mode="HTML")
        return

    try:
        data = infove_api.cantv.obtener_deuda(cadena[0:3], cadena[3:10])

    except ConsultaError:
        update.message.reply_text(constantes.ERROR_TXT, parse_mode="HTML")
        return

    men = "<b>Consulta del servicio telefónico CANTV</b>"

    if data.get("respuesta"):
        men += "\n\nSaldo actual Bs. <b>%s</b>" % data.get("saldo")
        men += "\nFecha de última facturación: <b>%s</b>" % data.get("ultima_facturacion")
        men += "\nFecha de corte: <b>%s</b>" % data.get("fecha_corte")
        men += "\nFecha de vencimiento: <b>%s</b>" % data.get("fecha_vencimiento")
        men += "\nSaldo vencido: <b>%s</b>" % data.get("saldo_vencido")
        men += "\nÚltimo pago realizado: <b>%s</b>" % data.get("ultimo_pago")
    else:
        men += "\n\nNo produjo ningún resultado"

    update.message.reply_text(men, parse_mode="HTML")


def comando_ivss(bot, update, args):
    """
    Controlador del comando para consultar datos en Ivss
    """

    if not len(args) == 2 \
    or not re.match("^[V|E|T|v|e|t][0-9]{6,8}$", args[0]) \
    or not fecha_valida(args[1]):

        update.message.reply_text(constantes.IVSS_INVALIDO_TXT, parse_mode="HTML")
        return

    try:
        data = infove_api.ivss.obtener_cuenta(args[0][0],
                                              args[0][1:],
                                              args[1][0:2],
                                              args[1][3:5],
                                              args[1][6:10])

    except ConsultaError:
        update.message.reply_text(constantes.ERROR_TXT, parse_mode="HTML")
        return

    men = "<b>Consulta del Seguro Social</b>"

    if data.get("respuesta"):
        men += "\n\nCédula: <b>%s</b>" % a_unicode(data.get("cedula"))
        men += "\nNombre: <b>%s</b>" % a_unicode(data.get("nombre"))
        men += "\nSexo: <b>%s</b>" % a_unicode(data.get("sexo"))
        men += "\nFecha de nacimiento: <b>%s</b>" % a_unicode(data.get("nacimiento"))
        men += "\n\nNúmero patronal: <b>%s</b>" % a_unicode(data.get("numero_patronal"))
        men += "\nEmpresa: <b>%s</b>" % a_unicode(data.get("empresa"))
        men += "\nIngreso: <b>%s</b>" % a_unicode(data.get("ingreso"))
        men += "\nEstatus del asegurado: <b>%s</b>" % a_unicode(data.get("estatus"))
        men += "\nPrimera afiliación: <b>%s</b>" % a_unicode(data.get("afiliacion"))
        men += "\nContingencia: <b>%s</b>" % a_unicode(data.get("contingencia"))
        men += "\nSemanas cotizadas: <b>%s</b>" % a_unicode(data.get("semanas"))
        men += "\nTotal salarios cotizados: <b>Bs. %s</b>" % a_unicode(data.get("salarios"))

    else:
        men += "\n\nNo produjo ningún resultado"

    update.message.reply_text(men, parse_mode="HTML")


def inlinequery(bot, update):
    """
    Controlador de las peticiones inline. Por ahora sólo gestiona la consulta
    de información en Cantv
    """

    query = update.inline_query.query

    if not re.match("^[0-9]{3} [0-9]{7}$", query):
        return

    partes = query.split()

    try:
        resultados = infove_api.cantv.obtener_deuda(partes[0], partes[1])

    except ConsultaError:
        return

    men = "Consulta del servicio telefónico CANTV"

    if data.get("respuesta"):
        men += "\n\nSaldo actual Bs. %s" % data.get("saldo")
        men += "\nFecha de última facturación: %s" % data.get("ultima_facturacion")
        men += "\nFecha de corte: %s" % data.get("fecha_corte")
        men += "\nFecha de vencimiento: %s" % data.get("fecha_vencimiento")
        men += "\nSaldo vencido: %s" % data.get("saldo_vencido")
        men += "\nÚltimo pago realizado: %s" % data.get("ultimo_pago")
    else:
        men += "\n\nNo produjo ningún resultado"

    results = list()
    results.append(InlineQueryResultArticle(id=uuid4(),
                                            title="Consulta CANTV",
                                            input_message_content=InputTextMessageContent(men)))
    update.inline_query.answer(results, parse_mode="HTML")


def main():
    """
    Función principal. Crea el bot, asigna los manejadores y lo ejecuta
    """

    updater = Updater("330833589:AAGRpbSzReUnVgqjUrTxpsrv4jbJ8oRhtf0")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", comando_start))
    dp.add_handler(CommandHandler("help", comando_help))
    dp.add_handler(CommandHandler("cantv", comando_cantv, pass_args=True))
    dp.add_handler(CommandHandler("ivss", comando_ivss, pass_args=True))
    dp.add_handler(InlineQueryHandler(inlinequery))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()