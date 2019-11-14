# -*- coding: utf-8 -*-

def construir_diccionario():
    lineas = {}
    porcentajes = {}
    with open('datos_vuelos.csv', 'r+') as datos:
        lines = datos.readlines()
        lines.pop(0)
        for l in lines:
            datos = l.split(",")#[matrícula, salida, llegada, pasajeros[]]
            matricula = datos[1]
            matriculas = linea.split(";")
            mes = datos[2].replace("[", "")
            mes=str(mes[3:5])
            
            if mes not in porcentajes:
                porcentajes[mes]=1
            else:
                porcentajes[mes]+=1

            if mes not in lineas:
                lineas[mes]={}
            else:
                if matricula not in lineas:
                    lineas[mes][matricula]= 1
                else : 
                    lineas[mes][matricula]+=1

    print(porcentajes)
    print (lineas)
    return porcentajes,lineas

   



#Codigo Principal#
