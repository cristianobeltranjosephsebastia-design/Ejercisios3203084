Conn = "MiClave"
longitud_min = 8

print("Contraseña a validar:", Conn)
print("Longitud de contraseña:", len((Conn)))

if len(Conn) >= longitud_min:
    print("La contraseña tiene la longitud correcta")   

if Conn.islower():
    print("")