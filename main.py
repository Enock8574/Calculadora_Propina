print("----------Enoc Carrera ©2021----------")
print("Este Software le ayudara a calcular la propina a dar")
#Variables para recoger los datos de la cantidad de la factura , el porcentaje que escogio el cliente y la cantidad de personas que pagaron la factura
factura = input("Ingrese la cantidad total de la factura: \n")
porcentaje = input("Que porcentaje desea dar para propina. Sugerido:10, 12 o 15%: \n")
personas = input("Cuantas Personas pagaron la factura?: \n")
#Primero Transforme el porcentaje que el cliente ingreso de manera entera , converti el porcentaje en flotante
trans_porc = int(porcentaje)/100
#Sacamos el total de la factura junto con el porcentaje que ingreso el cliente
factura_porcentaje = float(factura)*float(trans_porc)
#Luego ejecutamos la operacion para sacar el resultado de las propinas.
propina = (float(factura)+factura_porcentaje)/int(personas)
#Esta Variable redondea el total de la factura a 2 decimales
prop_redondeado = round(propina,2)
#Se utiliza la funcion fstring para conbinar diferentes tipos de datos
print(f"Ustedes {personas} deben dar ${prop_redondeado} como propina")
