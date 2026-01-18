x = None
print(x)        # None
print(type(x))  # <class 'NoneType'>


#para comparar siempre usa is o is not, no ==.
dato = None
es_none = dato is None
print(es_none) #true

#Diferencia entre None, False y 0
print(None == False)  # False
print(None == 0)      # False
print(None == "")     # False