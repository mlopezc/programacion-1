#declaración directa
es_mayor = True
tiene_permiso = False

print(es_mayor)
print(tiene_permiso)


#Booleanos a partir de comparaciones
edad = 18

es_adulto = edad >= 18
es_menor = edad < 18

print(es_adulto)  # True
print(es_menor)   # False

#Booleanos usando operadores lógicos
tiene_entrada = True
es_vip = False

puede_entrar = tiene_entrada and es_vip
print(puede_entrar)  # True