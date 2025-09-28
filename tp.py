variables = 0
proposicion = ""
print(f'\nOperadores soportados:'
      f'\nConjunción (∧): and'
      f'\nDisyunción (∨): or'
      f'\nNegación (¬): not'
      f'\nImplicación (⇒): =>"'
      f'\nVariables aceptadas: p, q'
      )

while proposicion == "":
    proposicion = input("Ingrese la proposición compuesta que desea clasificar: ")

if "p" and "q" in proposicion:
    variables = 2
    print(variables)
    print("Se detectaron dos variables")
elif "p" or "q" in proposicion:
    variables = 1
    print(variables)
    print("Se detecto una variable.")
if "and" in proposicion:
    if variables ==1:
        if "p" in proposicion:
            if "not p" in proposicion:
                p=False

        elif "q" in proposicion:
            if "not q" in proposicion:
                q=False


elif "or" in proposicion:
    pass
elif "not" in proposicion:
    pass
elif "=>" in proposicion:
    pass

