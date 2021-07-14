import re 
#en este apartado se definen las expresiones regulares de las diferentes expreciones que se esperan
#que el usuario ingrese los cules se definen como patrones 
#los cuales serviran para identificar en que parte del codigo se tratara dicha exprecion
patron1=r"^\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+$" 
patron2=r"^\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+$"
patron3=r"^\w+\s\=\s[(]\s\w+\s[+-/]\s\w+\s[)]\s\/\s\w+\s[+-/]\s\w+$|^\w+\s\=\s\w+\s[+-/]\s\w+\s[+-/]\s[(]\s\w+\s[+-/]\s\w+\s[)]$|^\w+\s\=\s\w+\s[+-/]\s[(]\s\w+\s[+-/]\s\w+\s[)]\s[+-/]\s\w+$|^\w+\s\=\s[(]\s\w+\s[+-/]\s\w+\s[)]\s[+-/]\s\w+\s[+*-/]\s\w+$"
patron4 = r"^\w+\s\=\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s[+*-/]\s[(]\s\w+\s[+*-/]\s\w+\s[)]$"
patron5 = r"^\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s[(]\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s[+*-/]\s\w+\s[)]$"
cont=0
cont1=0
cont2=0
cont3=0
dato=input("ingrese la expresion: ")#se solicita y se alamcena la exprecion

#codigo para buscar divicion o multiplicacion
concidencias=len(re.findall(patron1,dato))#con esta linea de codigo se verifica si es la expresion que se debe trabajar en te bloque de codigo
if concidencias>=1:
  dato_div=dato.split()
  #en este caso se maneja por for separados tomando en cuneta las primera operacion de la jerarquia de operaciones
  #en este for se trata de buscar una multiplicacion o divicion 
  #se emplean ifs para poder determinar los diferentes escenarios posibles que se podrian ingresar 
  #es decir la pocicion en que se encuentra la divicion o multiplicacion ya que la posicion aecta lo que es la imprecion de..
  #los o del codigo intermedio que se genera.
  #este forma no se le aplico alas demas expreciones ya que implicaria mas codigo ya se estarian realisando las 
  #diferentes conparaciones con if, lo cual nos ahoraria codigo con la implementacion de varios for.
  for i in dato_div:
    cont=cont+1
    if i=="/":
        print("_t1= "+dato_div[cont-2]+" / "+dato_div[cont])
    if i=="*":
        print("_t1= "+dato_div[cont-2]+" * "+dato_div[cont])

#codigo para buscar suma o resta una ves que se alla realisado el proceso anterior
concidencias=len(re.findall(patron1,dato))#con esta linea de codigo se verifica si es la expresion que se debe trabajar en te bloque de codigo
if concidencias>=1:
  dato_div=dato.split()#sementacion o separacion por partes de la exprecion en partes mediante un el metodo split()
  #en este for se trata de buscar una suma o resta 
  #se emplean ifs para poder determinar los diferentes escenarios posibles que se podrian ingresar 
  #es decir la pocicion en que se encuentra la suma o resta ya que la posicion aecta lo que es la imprecion de..
  #los o del codigo intermedio que se genera.
  for i in dato_div:
    cont1=cont1+1
    if i=="+":
        if cont1==4:
            print("_t2= "+dato_div[cont1-2]+" + "+"_t1")
            print("x = _t2")
        if cont1==6:
            print("_t2= "+"_t1 "+" + "+dato_div[6])
            print("x = _t2")
    if i=="-":
        if cont1==4:
            print("_t2= "+dato_div[cont1-2]+" - "+"_t1")
            print("x = _t2")
        if cont1==6:
            print("_t2= "+"_t1 "+" - "+dato_div[6])
            print("x = _t2")
        
coincidencias1 = len(re.findall(patron2, dato))#con esta linea de codigo se verifica si es la expresion que se debe trabajar en te bloque de codigo
if coincidencias1 >= 1:
    dato_div = dato.split() #sementacion o separacion por partes de la exprecion en partes mediante un el metodo split
    #manejo de for anidados para recorrer todo la lista generada de la exprecion ingresada
    #para poder ordenar y realisar imprecion en base a las reglas o las jerarquias de operaciones
    for i in dato_div:
        cont = cont + 1
        if i == "/": 
            print("_t1 = "+dato_div[cont-2]+" "+dato_div[cont-1]+" "+dato_div[cont])
            for i in dato_div:
                cont2 = cont2 + 1
                if i == "*": 
                    print("_t2 = "+dato_div[cont2-2]+" "+dato_div[cont2-1]+" "+dato_div[cont2])
                    for i in dato_div:
                        cont3 = cont3 + 1
                        if i == "+" or i == "-":
                            print("_t3 = _t1 "+dato_div[cont3-1]+" _t2")
                            break
            break
        elif i == "*": 
            print("_t1 = "+dato_div[cont-2]+" "+dato_div[cont-1]+" "+dato_div[cont])
            for i in dato_div:
                cont2 = cont2 + 1
                if i == "/":
                    print("_t2 = "+dato_div[cont2-2]+" "+dato_div[cont2-1]+" "+dato_div[cont2])
                    for i in dato_div:
                        cont3 = cont3 + 1
                        if i == "+" or i == "-":
                            print("_t3 = _t1 "+dato_div[cont3-1]+" _t2")
                            break
            break
    print("X = _t3")


coincidencias2 = len(re.findall(patron3, dato))#con esta linea de codigo se verifica si es la expresion que se debe trabajar en te bloque de codigo
if coincidencias2 >= 1:
    dato_div = dato.split() #sementacion o separacion por partes de la exprecion en partes mediante un el metodo split()
    #manejo de for anidados para recorrer todo la lista generada de la exprecion ingresada
    #para poder ordenar y realisar imprecion en base a las reglas o las jerarquias de operaciones
    for i in dato_div:
        cont = cont + 1
        if i == "(": 
            print("_t1 = "+dato_div[cont]+" "+dato_div[cont+1]+" "+dato_div[cont+2]) 
            
        if i == ")": 
            cont2 = cont
            cont3 = cont - 4
            if cont > 10:
                for i in (dato_div[cont3],-1,-1):
                    cont3 = cont3 - 1
                    if dato_div[cont3] == "+" or dato_div[cont3] == "-":
                        print("_t2 = "+dato_div[cont3-3]+" "+dato_div[cont3-2]+" "+dato_div[cont3-1])
                        print("_t3 = "+"_t1 "+dato_div[cont3]+" _t2")
                        cont4 = cont3
                        for i in (dato_div[cont4],-1,-1):
                            if dato_div[cont3] == "*" or dato_div[cont3] == "/": 
                                print("_t2 = "+"_t1 "+dato_div[cont3]+" "+dato_div[cont3-1])
                                print("_t3 = "+"_t2 "+dato_div[cont3-2]+" _t2")
                    elif dato_div[cont3] == "*" or dato_div[cont3] == "/":
                        print("_t2 = "+"_t1 "+dato_div[cont3]+" "+dato_div[cont3-1])
                        print("_t3 = "+"_t2 "+dato_div[cont3-2]+" "+dato_div[cont3-3])
                        cont4 = cont3
                        for i in (dato_div[cont4],-1,-1):
                            if dato_div[cont3] == "+" or dato_div[cont3] == "-":
                                print("_t2 = "+dato_div[cont3-3]+" "+dato_div[cont3-2]+" "+dato_div[cont3-1])
                                print("_t3 = "+"_t1 "+dato_div[cont3]+" _t2")
            else:
                for i in dato_div[cont2]:
                    cont2 = cont2 + 1
                    if i == "/" or i == "*":
                        print("_t2 = "+"_t1 "+dato_div[cont2-1]+" "+dato_div[cont2])
                        print("_t3 = "+"_t2 "+dato_div[cont2+1]+" "+dato_div[cont2+2])
                    elif i == "-" or i == "+":
                        print("_t2 = "+dato_div[cont2]+" "+dato_div[cont2+1]+" "+dato_div[cont2+2])
                        print("_t3 = "+"_t1 "+dato_div[cont2-1]+" _t2")
    print("X = _t3")


coincidencias3 = len(re.findall(patron4, dato)) #verificacion de la concidencia unaves verificado entra al if si es la exprecion corespondiente
if coincidencias3 >=1:
    dato_div = dato.split() ##sementacion o separacion por partes de la exprecion en partes mediante un el metodo split()
     #manejo de for anidados para recorrer todo la lista generada de la exprecion ingresada
    #para poder ordenar y realisar imprecion en base a las reglas o las jerarquias de operaciones
    #en este caso al tratarse de una exprecion de dos parantesis se trata de realisar las operaciones qun estan dentro del los parantesis 
    #para continuar con la divicion
    for i in dato_div:
        cont = cont + 1
        if i =="(": 
            if cont < 4:
                print("_t1 = "+dato_div[cont]+" "+dato_div[cont+1]+" "+dato_div[cont+2])
        if i ==")": 
            if cont > 12:
                break
            elif dato_div[cont+1] == "(":
                cont2 = cont + 3
                print("_t2 = "+dato_div[cont2-1]+" "+dato_div[cont2]+" "+dato_div[cont2+1])
                print("_t3 = _t1 "+dato_div[cont2-3]+" _t2")
    print("X = _t3")

