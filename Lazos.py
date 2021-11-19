#La compañía ACME S.A. está desarrollando un nuevo método para detectar especies en base a su ADN. 
#Para representar una especie por su ADN se utiliza una secuencia S compuesta únicamente de las letras A, C, G y T.
#La inversa de una secuencia S se determina con los símbolos en orden inverso a lo presentado. 
#Ejemplo:
#>>> inversa('GATACA') = 'ACATAG'
#Se tienen como datos:
#Un listado L de secuencias S y
#Una cadena de referencia R que identifica de forma única a la especie buscada. R no tiene letras repetidas.
#Implemente un programa que muestre todas las secuencias S que pertenecen a la especie buscada y los índices en la inversa de S  donde aparece la cadena de referencia R .

#Para realizar esta tarea, por cada secuencia S en listado L :

#1. Forme la cadena inversa de la secuencia S

#2. La secuencia S pertenece a la especie buscada si:

    #a) la cadena de referencia R aparece exactamente dos veces en la segunda mitad de inversa y
     #b) al menos 4 veces en total.

#3. Si S pertenece a la especie buscada, muestre la secuencia S y los índices.

#L = ['ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC', 
#     'ATTAGCCGCTATCGA', 
#     '…']
#R = 'CG'

#SALIDA para Secuencia L[0]:
#Secuencia: ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC
#Inversa:   CGCGATACGTATTGGCCAAATTTATCGTTCGTTTA
#Índices:   [0, 2, 7, 25, 29]

#SALIDA para Secuencia L[1]:
#Secuencia: ...
#Índices:   ...

