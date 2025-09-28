variables=0

print("Operadores soportados:")
print("  Conjunción (∧): and")
print("  Disyunción (∨): or")
print("  Negación (¬): not")
print("  Implicación (⇒): =>")
print("Variables aceptadas: p, q")
proposicion=input("Ingrese la proposición compuesta que desea clasificar: ")
if "p" and "q" in proposicion:
    variables=2
    print(variables)
elif "p" or "q" in proposicion:
    variable=1
    print(variable)

if "and" in proposicion:
    pass
elif "or" in proposicion:
    pass
elif "not" in proposicion:
    pass
elif "=>" in proposicion:
    pass

