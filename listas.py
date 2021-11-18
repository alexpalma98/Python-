#EJERCICIO DEL CURSO FUNDAMENTOS DE PROGRAMACIÓN

texto = ''' por que es hermoso ser joven? ¿Por que el sueño de la juventud perenne? Me parece que son dos los elementos determinantes. La juventud tiene todavia el futuro por delante; todo es futuro, tiempo de esperanza. El futuro esta lleno de promesas.Para ser sinceros, debemos decir que para muchos el futuro también se presenta oscuro, sembrado de amenazas. Hay incertidumbre: ¿encontrare un puesto de trabajo?, ¿encontrare una vivienda?, ¿encontrare el amor?, ¿cual sera mi verdadero futuro? Y ante estas amenazas, el futuro tambien puede presentarse como un gran vacio. Por eso, hoy muchos quieren detener el tiempo, por miedo a un futuro en el vacio. Quieren aprovechar al maximo inmediatamente todas las bellezas de la vida. Y asi el aceite en la lampara se consuma cuando la vida deberia comenzar. Por eso es importante elegir las verdaderas promesas, que abren al futuro, incluso con renuncias'''

#La siguiente función retorna una lista de las palabras del mensaje y otras cuyos valores son los número de veces
#de cada palabra se repite en el texto.
#Convierte todas las palabras a minúsculas (Ignore la diferencia entre mayúsculas y minúsculas)

def contar_ocurrencias(mensaje):
  mensaje.lower()
  lista=mensaje.split(" ")
