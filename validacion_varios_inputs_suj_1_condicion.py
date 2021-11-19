#ESTA FUNCIÓN VALIDA EL INGRESO DE TRES INPUTS
#SUJETO A QUE LA CANTIDAD DE PALABRAS SEA MENOR O IGUAL QUE 20

def validation_inputs():
  user1=input("Write information A:" )
  new_user1_list=user1.split(" ")
  while len(new_user1_list)<=20:
    user1=input("Re-write information A: ")
  user2=input("Write information B: ")
  new_user2_list=user2.split(" ")
  while len(new_user2_list)<=20:
    user2=input("Re-write information B: ")
  user3=input("Write information C: ")
  new_user3_list=user3.split(" ")
  while len(new_user2_list)<=20:
    user3=input("Re-write information C: ")
  return tuple(new_user1_list),tuple(new_user2_list),tuple(new_user3_list)
    
  

