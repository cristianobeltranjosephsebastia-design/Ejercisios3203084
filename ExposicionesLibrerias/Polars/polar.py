import polars as pl


data = {
    "Nombre": ["Ana", "Carlos", "Luisa", "Marcos", "Laura"],
    "Edad": [28, 45, 33, 26, 39],
    "Salario": [3500, 4800, 4100, 3200, 4500],
    "Departamento": ["IT", "Ventas", "IT", "RRHH", "Ventas"]
}


df = pl.DataFrame(data)


print("  Datos de empleados:")
print(df)


filtro = df.filter(df["Salario"] > 4000)
print("\n Empleados con salario mayor a 4000:")
print(filtro)

promedio_por_area = (
    df.group_by("Departamento")
      .agg(pl.col("Salario").mean().alias("Promedio_Salarial"))
)
print("\n Promedio salarial por departamento:")
print(promedio_por_area)


ordenado = df.sort("Salario", descending=True)
print("\n Empleados ordenados por salario:")
print(ordenado)
