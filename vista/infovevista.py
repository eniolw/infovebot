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

from telegram import InlineQueryResultArticle, InputTextMessageContent
from util.util import aUnicode
from uuid import uuid4


class VistaHome(object):

    @classmethod
    def verStart(self, update):
        """
        Vista del comando start
        """

        m = "¡Hola! Soy un bot para consultar información de algunos servicios "
        m += "de Venezuela. Por ahora sólo consulto datos en CANTV y en el IVSS"
        m += "\n\nPara CANTV usa el comando /cantv así:\n<code>/cantv "
        m += "[código_de_área] [número]</code>\n\nEjemplo: <i>/cantv 268 "
        m += "5552525</i>\n\nPara IVSS usa el comando /ivss así:\n<code>/ivss "
        m += "[nacionalidad][numero_de_cédula] [dd]/[mm]/[aaaa]</code>"
        m += "\n\nEjemplo: <i>/ivss v15000111 01/12/1990</i>"
        m += "\n\nEn modo inline Infovebot soporta por ahora la consulta del "
        m += "servicio de CANTV con esta sintaxis: "
        m += "@infovebot <code>[código_de_área] [número]</code>"
        m += "\n\nEjemplo: <i>@infovebot 268 5552525</i>"

        update.message.reply_text(m, parse_mode="HTML")

    @classmethod
    def verError(self, update):
        """
        Vista de error en el sistema
        """

        update.message.reply_text("Se produjo un error. Intente luego",
                                  parse_mode="HTML")


class VistaCantv(object):

    @classmethod
    def verConsultaInline(self, update, data):
        """
        Vista de la búsqueda en CANTV por petición inline
        """

        men = "Consulta del servicio telefónico CANTV"

        if data["respuesta"]:
            men += "\n\nSaldo actual Bs. %s" % data["saldo"]
            men += "\nFecha de última facturación: %s" % data["ultimaFacturacion"]
            men += "\nFecha de corte: %s" % data["fechaCorte"]
            men += "\nFecha de vencimiento: %s" % data["fechaVencimiento"]
            men += "\nSaldo vencido: %s" % data["saldoVencido"]
            men += "\nÚltimo pago realizado: %s" % data["ultimoPago"]
        else:
            men += "\n\nNo produjo ningún resultado"

        results = list()
        results.append(InlineQueryResultArticle(id=uuid4(),
                                                title="Consulta CANTV",
                                                input_message_content=InputTextMessageContent(men)))
        update.inline_query.answer(results, parse_mode="HTML")

    @classmethod
    def verConsulta(self, update, data):
        """
        Vista de la búsqueda en CANTV por el comando buscar
        """

        men = "<b>Consulta del servicio telefónico CANTV</b>"

        if data["respuesta"]:
            men += "\n\nSaldo actual Bs. <b>%s</b>" % data["saldo"]
            men += "\nFecha de última facturación: <b>%s</b>" % data["ultimaFacturacion"]
            men += "\nFecha de corte: <b>%s</b>" % data["fechaCorte"]
            men += "\nFecha de vencimiento: <b>%s</b>" % data["fechaVencimiento"]
            men += "\nSaldo vencido: <b>%s</b>" % data["saldoVencido"]
            men += "\nÚltimo pago realizado: <b>%s</b>" % data["ultimoPago"]
        else:
            men += "\n\nNo produjo ningún resultado"

        update.message.reply_text(men, parse_mode="HTML")

    @classmethod
    def verConsultaErronea(self, update):
        """
        Vista de la validación de la entrada (caso Cantv->/cantv)
        """

        m = "<b>Consulta inválida</b>\nDeben ser números compuestos por 10 "
        m += "dígitos.\nLa sintaxis debe ser: XXX XXXXXXX siendo 'X' cualquier "
        m += "dígito. Ejemplo: 268 5552525"

        update.message.reply_text(m, parse_mode="HTML")


class VistaIvss(object):

    @classmethod
    def verConsultaInline(self, update, data):
        """
        Vista de la búsqueda en IVSS por petición inline
        Por implementar
        """

        return

    @classmethod
    def verConsulta(self, update, data):
        """
        Vista de la búsqueda en IVSS por el comando buscar
        """

        men = "<b>Consulta del Seguro Social</b>"

        if data["respuesta"]:
            men += "\n\nCédula: <b>%s</b>" % aUnicode(data["cedula"])
            men += "\nNombre: <b>%s</b>" % aUnicode(data["nombre"])
            men += "\nSexo: <b>%s</b>" % aUnicode(data["sexo"])
            men += "\nFecha de nacimiento: <b>%s</b>" % aUnicode(data["nacimiento"])
            men += "\n\nNúmero patronal: <b>%s</b>" % aUnicode(data["numeropatronal"])
            men += "\nEmpresa: <b>%s</b>" % aUnicode(data["empresa"])
            men += "\nIngreso: <b>%s</b>" % aUnicode(data["ingreso"])
            men += "\nEstatus del asegurado: <b>%s</b>" % aUnicode(data["estatus"])
            men += "\nPrimera afiliación: <b>%s</b>" % aUnicode(data["afiliacion"])
            men += "\nContingencia: <b>%s</b>" % aUnicode(data["contingencia"])
            men += "\nSemanas cotizadas: <b>%s</b>" % aUnicode(data["semanas"])
            men += "\nTotal salarios cotizados: <b>Bs. %s</b>" % aUnicode(data["salarios"])

        else:
            men += "\n\nNo produjo ningún resultado"

        update.message.reply_text(men, parse_mode="HTML")

    @classmethod
    def verConsultaErronea(self, update):
        """
        Vista de la validación de la entrada (caso Ivss->/ivss)
        """

        m = "<b>Consulta inválida</b>\nLa sintaxis debe ser:\n<code>/ivss "
        m += "[nacionalidad][numero_de_cédula] [dd]/[mm]/[aaaa]</code>\n\nPor "
        m += "ejemplo:\n<i>/ivss v15000111 01/12/1982 </i>"

        update.message.reply_text(m, parse_mode="HTML")