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
from uuid import uuid4


class VistaHome(object):

    @classmethod
    def verStart(self, update):
        """
        Vista del comando start
        """

        m = '¡Hola! Soy un bot para consultar información de algunos servicios de Venezuela. Por ahora sólo consulto datos en CANTV.'
        m += "\nUsa el comando buscar así: <code>/buscar código número </code>"
        m += "\n\nEjemplo: <i>/buscar 268 5552525</i>"
        m += "\n\nEn modo inline, se usa con esta sintaxis: "
        m += "@infovebot <code>código número</code>"
        m += "\n\nEjemplo: <i>@infovebot 268 5552525</i>"
        update.message.reply_text(m, parse_mode="HTML")

    @classmethod
    def verError(self, update):
        """
        Vista de error en el sistema
        """

        update.message.reply_text("Se produjo un error en el sistema. Intente luego", parse_mode="HTML")


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
        Vista de la validación de la entrada (caso Cantv->buscar)
        """

        update.message.reply_text("<b>Consulta inválida</b>\nDeben ser números compuestos por 10 dígitos.\nLa sintaxis debe ser: XXX XXXXXXX siendo 'X' cualquier dígito. Ejemplo: 268 5552525",
                                  parse_mode="HTML")