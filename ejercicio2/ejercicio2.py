edades = []
musica = ["rock", "salsa" "rap" "trap" "pop"]

# reto 1 
promedio = sum(edades) / len(edades)
print("promedio de edad:", promedio)

# reto 2
mayores =[edad for edad in edades if edad > 15]
print(" edades > 15:", mayores)

# reto 3 
fans_rock = [gen for gen in musica if gen == "rock"]
print("Total fans rock:", len(fans_rock))