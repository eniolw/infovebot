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

import pycurl


class Error(Exception):
    """
    Para buenas práticas
    """

    pass


class ConsultaError(Error):
    """
    Para lanzar excepciones de usuario
    """

    pass


class Cantv(object):

    def __init__(self):
        self.html = ""
        self.consulta = {}

    def obtenerDeuda(self, area, telefono):
        """
        Consulta datos en CANTV mediante pyCURL y técnicas de scrapping
        """

        url = "http://www.cantv.com.ve/seccion.asp?pid=1&sid=450"
        parametros = "sarea=%s&stelefono=%s" % (area, telefono)

        try:
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.POSTFIELDS, parametros)
            c.setopt(c.REFERER, "http://www.cantv.com.ve")
            c.setopt(c.USERAGENT, 'Mozilla/5.0 (X11; Linux i686; rv:32.0) Gecko/20100101 Firefox/40.0')
            c.setopt(pycurl.WRITEFUNCTION, self.setHTML)
            c.setopt(c.FRESH_CONNECT, 1)
            c.setopt(c.CONNECTTIMEOUT, 50)
            c.setopt(c.TIMEOUT, 300)
            c.perform()

        except pycurl.error:
            raise ConsultaError

        try:
            pos1 = self.html.index("Saldo actual Bs.") + 118
            self.consulta["saldo"] = self.html[pos1:self.html.find("</font>", pos1)]

            pos1 = self.html.index("Fecha de &uacute;ltima facturaci&oacute;n:") + 132
            self.consulta["ultimaFacturacion"] = self.html[pos1:self.html.find("</font>", pos1)]

            pos1 = self.html.index("Fecha corte:") + 102
            self.consulta["fechaCorte"] = self.html[pos1:self.html.find("</font>", pos1)]

            pos1 = self.html.index("Fecha de vencimiento:") + 111
            self.consulta["fechaVencimiento"] = self.html[pos1:self.html.find("</font>", pos1)]

            pos1 = self.html.index("Saldo vencido:") + 116
            self.consulta["saldoVencido"] = self.html[pos1:self.html.find("</font>", pos1)]

            pos1 = self.html.index("Monto del &uacute;ltimo pago realizado:") + 130
            self.consulta["ultimoPago"] = self.html[pos1:self.html.find("</font>", pos1)]

        except ValueError:
            return {"respuesta": False}

        for valor in self.consulta.values():
            if valor == "":
                return {"respuesta": False}

        self.consulta["respuesta"] = True
        return self.consulta

    def setHTML(self, data):
        """
        Método privado. Hacia acá se redirige la escritura del buffer
        """

        self.html += data