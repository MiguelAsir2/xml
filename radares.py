from lxml import etree
doc=etree.parse('Radares.xml')
from funcionesradares import provincias,contaradar,carretera,contarcarretera,longitud,latitud
#Menu
while True:
    print('''
                                        Menú
    ***********************************************************************************- 
    1. Lista Todas las Provincias.
    2. Cuenta Número Total de Radares.
    3. Introduce Provincia y Muestra las Carreteras y el Número de Radares.
    4. Introduce Carretera y Muestra Provincias y Radares. 
    5. Introduce Carretera Cuenta los Radares y muestra las Coordenadas de los Radares.
    0. Salir
    ''')
    opcion=int(input("Introduce el número de la opción: "))
    if opcion==1:
#1.Muestra el nombre de todas las provincias
        for i in provincias(doc):
            print(i)
#2.Cuenta el número total de los radares
    if opcion==2:
        print("Hay %d radares"%(int(contaradar(doc))))
#3.Pide una provincia y muestra nombre carretera y numero de radares
    if opcion==3:
        prov=input('Introduce el nombre de una provincia: ')
        if prov in provincias(doc):
            print("Las carreteras de %s son: "%prov)
            for i in doc.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()'%prov):
                print(i," | ",end="")
            print()
            print("El numero de radares es: ",end="")
            print(int(doc.xpath(('count(//PROVINCIA[NOMBRE="%s"]/CARRETERA/RADAR)'%prov))))
        else:
            print("La provincia introducida no existe")
#4. Pide una carretera y muestra las provincias y los radares
	if opcion==4:
        carretera=input("Introduce una carretera: ")
        print("La carretera %s pasa por: "%carretera)
        for provincia in doc.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera):
            print(provincia)
            for i in doc.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA[DENOMINACION="%s"]/RADAR/text()'%(provincia,carretera)):
                print(i)
#5. Pedir por teclado una carretera
    if opcion==5:
        carretera=input("Introduce una carretera: ")
        if carretera in doc.xpath('//CARRETERA/DENOMINACION/text()'):
# cuenta los radares que tiene y 
            print("La carretera %s tiene %d radares"%(carretera,(int(contarcarretera(carretera,doc)))))
# muestra las coordenadas de los radares
            print()
            print("Los radares se encuentran en los siguientes puntos:")
            for i,j in zip(longitud(carretera,doc),latitud(carretera,doc)):
                print("https://www.openstreetmap.org/#map=19/%s/%s"%(i,j))
        else:
            print("Esa carretera no existe")
    if opcion==0:
        break
    if opcion>5 or opcion<0:
        print("Opcion Incorrecta")
