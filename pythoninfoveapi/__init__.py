# -*- coding: utf-8 -*-
# 
# Este archivo es parte del módulo infove-api.
# Copyright (C) 2017-2018 Oniel Revilla Morón <eniolw@gmail.com>
# 
# Este software ha sido liberado bajo los términos de la licencia GNU AGPL 3.0
# (véase: https://www.gnu.org/licenses/agpl-3.0.html)
# 
"""Un módulo para el acceso a la data de servicios públicos como Cantv e Ivss.
Emula el funcionamiento de una API para estos sitios aplicando web scrapping. 
Algunas clases de este módulo contienen porting a Python de algunos scripts 
escritos por William Cabrera <cabrerawilliam@gmail.com> en PHP. Para más 
información, véase: https://github.com/willicab/infove-api."""


__author__ = "Oniel Revilla"

__email__ = "eniolw@gmail.com"

__version__ = "1.0"

from .clases import InfoVeApi