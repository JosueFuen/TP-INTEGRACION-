import itertools

def evaluar_proposicion(expr, variables, valores):
    contexto = {}
    for var, val in zip(variables, valores):
        contexto[var] = val
    try:
        return eval(expr, {}, contexto)
    except Exception as e:
        print(f"Error al evaluar la expresión: {e}")
        return None

def clasificar(expr):
    variables = sorted(set(filter(str.isalpha, expr)))
    resultados = []
    combinaciones = list(itertools.product([False, True], repeat=len(variables)))

    print("Tabla de verdad:")
    for valores in combinaciones:
        resultado = evaluar_proposicion(expr, variables, valores)
        if resultado is None:
            return
        resultados.append(resultado)
        print(f"{dict(zip(variables, valores))} => {resultado}")

    if all(resultados):
        print("Clasificación: Tautología")
    elif not any(resultados):
        print("Clasificación: Contradicción")
    else:
        print("Clasificación: Contingencia")

# Ejemplo de uso
entrada = input("Ingrese una proposición (use and, or, not): ")
clasificar(entrada)

#Creo que deberiamos quitar las funciones como 
