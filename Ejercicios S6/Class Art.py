# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:33:57 2021

@author: maril
"""

"""
articulo
cliente
venta
ventadet
"""
class Articulo:
    def __init__(self, cod, des, prec, stop):
        self.codigo= cod
        self.descripcion= des
        self.precio= prec
        self.stop= stop