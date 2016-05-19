#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('pos_empresa.db')

print "--------------------"
print "--------------------"

#CONSULTA 1

cur = con.execute("SELECT COUNT(*) FROM sale WHERE date LIKE \"2013%\"")
for row in cur:
	print"Cantidad total de ventas en el anio 2013", row[0]

print "--------------------"
print "--------------------"

#CONSULTA 2

cur = con.execute("SELECT product.name, AVG(sale_product.net_unit_price) FROM sale_product JOIN product ON product.id = sale_product.product_id GROUP BY product_id LIMIT 15")
for row in cur:
	print "Producto: ",row[0]
	print "Precio venta promedio: ",row[1]
	print "--------------------"

print "--------------------"

#CONSULTA 3

print "Total de ventas por cliente:"

cur = con.execute("SELECT entity.names, entity.surnames, entity.company_name, SUM(sale.gross_total) AS total_ventas FROM sale JOIN entity ON sale.entity_id = entity.id GROUP BY sale.entity_id LIMIT 15")
for row in cur:
	print "Nombre: ",row[0]
	print "Apellido: ",row[1]
	print "Nombre compania: ",row[2]
	print "Total ventas: ",str(row[3])
	print "--------------------"

print "--------------------"

#CONSULTA 4

print "Total de ventas por cliente el año 2014:"
cur = con.execute("SELECT entity.names, entity.surnames, entity.company_name, SUM(sale.gross_total) AS total_ventas FROM sale JOIN entity ON sale.entity_id = entity.id WHERE date LIKE \"2014%\" GROUP BY sale.entity_id LIMIT 15")
for row in cur:
	print "Nombre: ",row[0]
	print "Apellido: ",row[1]
	print "Nombre compania: ",row[2]
	print "Total ventas: ",str(row[3])
	print "--------------------"

print "--------------------"

#CONSULTA 5

print "Total de ventas por fecha en noviembre del 2013:"
cur = con.execute("SELECT date, COUNT(*), SUM(gross_total) FROM sale WHERE date LIKE \"2013-11%\" GROUP BY date;")
for row in cur:
	print "Fecha: ",row[0]
	print "Cantidad de ventas: ",row[1]
	print "Total ventas: ",row[2]
	print "--------------------"

print "--------------------"

#CONSULTA 6

print "Cantidad y montos totales por producto:"
cur = con.execute("SELECT product.name, sale_product.quantity, sale_product.gross_total FROM sale_product JOIN product ON sale_product.product_id = product.id ORDER BY sale_product.quantity DESC LIMIT 15;")
for row in cur:
	print "Producto: ",row[0]
	print "Cantidad: ",row[1]
	print "Total ventas: ",row[2]
	print "--------------------"

print "--------------------"


