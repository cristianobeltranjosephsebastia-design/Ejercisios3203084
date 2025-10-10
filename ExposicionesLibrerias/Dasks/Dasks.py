import dask.array as da


x = da.random.randint(1, 11, size=10, chunks=5)


print("Números generados:")
print(x.compute())


media = x.mean()


print("Promedio:")
print(media.compute())