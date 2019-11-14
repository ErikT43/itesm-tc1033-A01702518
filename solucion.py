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
            matriculas = matricula.split(";")
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

def totalmeses():
    porcentajes,lineas=construir_diccionario()
    total ={}
    for mes in lineas.keys():
        total[mes]={}
        for matricula in lineas[mes].keys():
            porcentaje=((lineas[mes][matricula]/porcentajes[mes])*100)
            if porcentaje>=20:
                total[mes][matricula]=porcentaje
    
    return total,mes,matricula

def escribir():
    archivo=open("resultados.csv","w+")
    archivo.write("Mes, País, Total ")
    for mes in total:
        archivo.write(mes)
        archivo.write("\n")

def predecir(matricula):
    diccionario=construir_diccionario()

