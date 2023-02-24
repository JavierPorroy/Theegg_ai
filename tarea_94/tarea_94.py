import tiempo as t

x = float(input("Introduce los segundos que tarda el objeto en llegar al suelo: "))
print()
print()
print()
print("En La Tierra, un objeto que tarda",x, " segundos en llegar al suelo, se encuentra a una altura de ",(t.tierra(x,9.8))," metros.")

print()
print()
print()
print("En Marte, un objeto que tarda",x, " segundos en llegar al suelo, se encuentra a una altura de ",(t.marte(x,3.7))," metros.")

print()
print()
print()
print("En Jupiter, un objeto que tarda",x, " segundos en llegar al suelo, se encuentra a una altura de ",(t.jupiter(x,24.8))," metros.")
