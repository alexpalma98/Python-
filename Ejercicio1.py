#EJERCICIO DEL CURSO FUNDAMENTOS DE PROGRAMACIÓN


texto = '''por que es hermoso ser joven? ¿Por que el sueño de la juventud perenne? Me parece que son dos los elementos determinantes. La juventud tiene todavia el futuro por delante; todo es futuro, tiempo de esperanza. El futuro esta lleno de promesas.Para ser sinceros, debemos decir que para muchos el futuro también se presenta oscuro, sembrado de amenazas. Hay incertidumbre: ¿encontrare un puesto de trabajo?, ¿encontrare una vivienda?, ¿encontrare el amor?, ¿cual sera mi verdadero futuro? Y ante estas amenazas, el futuro tambien puede presentarse como un gran vacio. Por eso, hoy muchos quieren detener el tiempo, por miedo a un futuro en el vacio. Quieren aprovechar al maximo inmediatamente todas las bellezas de la vida. Y asi el aceite en la lampara se consuma cuando la vida deberia comenzar. Por eso es importante elegir las verdaderas promesas, que abren al futuro, incluso con renuncias'''

#La siguiente función retorna una lista de las palabras del mensaje y otras cuyos valores son los número de veces
#de cada palabra se repite en el texto.
#Convierte todas las palabras a minúsculas (Ignore la diferencia entre mayúsculas y minúsculas)

def contar_ocurrencias(mensaje):
  #LA SIGUIENTE ESTRUCTURA PERMITE ELIMINAR
  #VARIOS CARACTERES NO DESEADOS DE UN STRING
  mensaje2=mensaje.lower()
  for ch in ["?","¿",".",",",";"]:
    if ch in mensaje2:
      mensaje2=mensaje2.replace(ch,"") #ACTUALIZA EL STRING
  lista=mensaje2.split(" ") #CONVIERTE EL STRING EN LISTA
  #CREACION DE UNA LISTA UNICA
  lista_unica=[]
  for palabra in lista:
    if palabra not in lista_unica:
      lista_unica.append(palabra)
  #CREACION DE UN CONTADOR DE PALABRAS
  cont_palabras=[]
  for palabra in lista_unica:
    cantidad=lista.count(palabra)
    cont_palabras.append(cantidad)
  return lista_unica,cont_palabras,len(lista_unica),len(cont_palabras)

tupla_inf=contar_ocurrencias(texto)


#LA SIGUIENTE FUNCION RETORNA UNA LISTA CON TUPLAS
#DONDE LA CANTIDAD DE TUPLAS VIENE DETERMINADA POR EL USUARIO
#Y CONTIENE LAS PALABRAS MÁS REPETIDAS EN EL TEXTO

def top(LPal,LVces,k):
  posiciones=list(range(len(LVces)))
  listaNum=[]
  listaPal=[]
  listaTupla=[]
  for numero in range(max(LVces)-k,max(LVces)+1):
    


  return posiciones

print(tupla_inf[0])
print(tupla_inf[1])
lista=top(tupla_inf[0],tupla_inf[1],5)
print(lista)




