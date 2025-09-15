
class Vehiculo: 
    def __init__(self, Motor, Llantas, Luces, Capacidad, Frenos):

        self.Motor = Motor
        self.Llantas = Llantas
        self.Luces = Luces
        self.Capacidad = Capacidad
        self.Frenos = Frenos

   
Mi_Vehiculo = Vehiculo ("1300cm", "Radial R15", "Led", "4 pasajeros", "Disco")
Otro_Vehiculo = Vehiculo("1200cm", "Radial R15", "Led Delanteras", "5 pax", "Disco")


print(Mi_Vehiculo.Motor, Mi_Vehiculo.Llantas, Mi_Vehiculo.Luces, Mi_Vehiculo.Capacidad, Mi_Vehiculo.Frenos)
