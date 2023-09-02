import math 

simbolos=['s1','s2', 's3', 's4']
probabilidades=[0.1,0.4,0.3,0.2]
diccionario=dict(zip(simbolos,probabilidades))

def entropia(diccionario):
      entropia=0
      for i in diccionario.values():
         entropia+=i*math.log(i,2)
      return -entropia
#Vamos a ordenar los simbolos de mayor a menor probabilidad
def ordenar_mayor_menor(dic):
     #ordenamos de mayor a menor
   diccionario_ordenado=sorted(dic.items(), key=lambda x: x[1], reverse=True)
   return diccionario_ordenado

def restar_dos_menores(diccionario):
   resul=diccionario[-2][-1]+diccionario[-1][-1]
   del diccionario[-1]
   del diccionario[-1]
   return resul,diccionario

if __name__ == "__main__":
   dic_ordenado=ordenar_mayor_menor(diccionario)
   print(dic_ordenado)
   print(restar_dos_menores(dic_ordenado))

