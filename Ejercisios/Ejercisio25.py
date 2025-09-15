Students = [] # Lista global para almacenar estudiantes
def Add_student(nombre, edad, grado):
    """Agrega un nuevo estudiante al sistema"""
    Student = {
    "nombre": nombre,
    "edad": edad,
    "grado": grado,
    "calificaciones": []
}
    Students.append(Student)
    print(f"7 Estudiante {nombre} agregado exitosamente")
def Search_student(nombre):
    """Busca un estudiante por nombre"""
    for i, Student in enumerate(Students):
        if Student["nombre"].lower() == nombre.lower():
            return i # Retorna la posición
    return -1 # No encontrado

def Add_Qualification(nombre, materia, nota):
    """Agrega una calificación a un estudiante"""
    Position = Search_student(nombre)
    if Position != -1:
        Qualification = {"materia": materia, "nota": nota}
        Students[Position]["calificaciones"].append(Qualification)
        print(f"7 Calificación agregada a {nombre}: {materia} = {nota}")
    else:
        print(f"Estudiante {nombre} no encontrado")
def Calc_prom(nombre):
    """Calcula el promedio de un estudiante"""
    Position = Search_student(nombre)
    if Position != -1:
        Qualifications = Students[Position]["calificaciones"]
    if Qualifications:
        suma = sum(cal["nota"] for cal in Qualifications)
        prom = suma / len(Qualifications)
        return round(prom, 2)
    else:
        return 
    return None

def mostrar_reporte():
    """Muestra un reporte completo de todos los estudiantes"""
    print("\n" + "="*50)
    print("REPORTE DE ESTUDIANTES")
    print("="*50)
    for Student in Students:
        print(f"\nNombre: {Student['nombre']}")
        print(f"Edad: {Student['edad']} años")
        print(f"Grado: {Student['grado']}")
    if Student["calificaciones"]:
        print("Calificaciones:")
    for cal in Student["calificaciones"]:
        print(f" - {cal['materia']}: {cal['nota']}")
        promedio = Calc_prom(Student['nombre'])
        print(f"Promedio general: {promedio}")
    else:
        print("Sin calificaciones registradas")
        print("-" * 30)
        print("SISTEMA DE REGISTRO DE ESTUDIANTES")
Add_student("Ana García", 16, "10°")
Add_student("Carlos López", 15, "9°")
Add_student("María Rodríguez", 17, "11°")

Add_Qualification("Ana García", "Matemáticas", 9.2)
Add_Qualification("Ana García", "Historia", 8.8)
Add_Qualification("Ana García", "Ciencias", 9.5)
Add_Qualification("Carlos López", "Matemáticas", 7.5)
Add_Qualification("Carlos López", "Historia", 8.2)
Add_Qualification("Pedro Martín", "Matemáticas", 8.0)
mostrar_reporte()