variables=0
p=True
q=True

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
    variables=1
    print(variables)

if "and" in proposicion:
    if variables ==1:
        if "p" in proposicion:
            if "not p" in proposicion:
                if "p" and "not p" in proposicion:
                    verdad=p and not p
                    print(verdad)
                elif "not p" and "not p":
                    verdad= not p and not p
                    print(verdad)
                else:
                    verdad= not p


        elif "q" in proposicion:
            if "not q" in proposicion:
                q=False


elif "or" in proposicion:
    pass
elif "not" in proposicion:
    pass
elif "=>" in proposicion:
    pass

