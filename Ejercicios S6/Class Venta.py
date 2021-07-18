# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:34:49 2021

@author: maril
"""

class Venta:
    def __init__(self, fac, fec, tot, cliente, detalleven):
        self.factura= fac
        self.fecha= fec
        self.total= tot
        self.cliente= cliente
        self.detalleVen= detalleven 