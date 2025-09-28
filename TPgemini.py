# Variables y contadores simples
proposicion_usuario = ""
variables_encontradas = 0
resultado_final_es_True = 0
resultado_final_es_False = 0

# --- Entrada de la Proposición y Determinación de Variables ---
print("Operadores soportados:")
print("  Conjunción (∧): and")
print("  Disyunción (∨): or")
print("  Negación (¬): not")
print("  Implicación (⇒): =>")
print("  Doble Implicación (⇔): <=>")
print("Variables aceptadas: p, q")

proposicion_usuario = input("Ingrese la proposición compuesta (ej: p or not p): ")
proposicion_evaluar = proposicion_usuario

# Simulación básica de búsqueda de variables
if "q" in proposicion_usuario:
    variables_encontradas = 2
elif "p" in proposicion_usuario:
    variables_encontradas = 1

# Simulación de sustitución de operadores especiales
proposicion_evaluar = proposicion_evaluar.replace("=>", "IMPLICA")
proposicion_evaluar = proposicion_evaluar.replace("<=>", "DOBLE_IMPLICA")

# --- Evaluación de la Tabla de Verdad ---

if variables_encontradas == 1:
    print("\n--- Tabla de Verdad (Variable: p) ---")
    print(" p | Resultado")
    print("---|-----------")
    
    # Valores de verdad para una variable (p)
    valores_p = (True, False)
    
    for p in valores_p:
        # Sustitución básica para p
        eval_p = "True"
        if not p:
            eval_p = "False"
            
        proposicion_temp = proposicion_evaluar.replace("p", eval_p)

        # Reemplazo de operadores de implicación por equivalencia
        # p => p equivale a (not p) or p
        proposicion_temp = proposicion_temp.replace("IMPLICA", "((not ")
        proposicion_temp = proposicion_temp.replace("IMPLICA", " and ")

        # Evaluación forzada de la expresión simple (NO USAR EVAL EN PRODUCCIÓN)
        resultado = eval(proposicion_temp)

        # Impresión de la fila
        print(f"{'T' if p else 'F'} | {'T' if resultado else 'F'}        ")
        
        # Conteo para la clasificación
        if resultado:
            resultado_final_es_True = resultado_final_es_True + 1
        else:
            resultado_final_es_False = resultado_final_es_False + 1

elif variables_encontradas == 2:
    print("\n--- Tabla de Verdad (Variables: p, q) ---")
    print(" p | q | Resultado")
    print("---|---|-----------")
    
    # Valores de verdad para dos variables (p, q)
    valores_pq = (True, False)
    
    for p in valores_pq:
        for q in valores_pq:
            # Sustitución básica de p y q
            eval_p = "True"
            if not p:
                eval_p = "False"
            
            eval_q = "True"
            if not q:
                eval_q = "False"

            proposicion_temp = proposicion_evaluar.replace("p", eval_p)
            proposicion_temp = proposicion_temp.replace("q", eval_q)

            # Reemplazo de operadores de implicación por equivalencia
            # p => q equivale a (not p) or q
            proposicion_temp = proposicion_temp.replace("IMPLICA", "or")
            proposicion_temp = "(not " + proposicion_temp + ")"

            # p <=> q equivale a (p and q) or (not p and not q)
            # Esto es complejo de sustituir sin funciones o estructuras avanzadas para un caso general.
            # En el siguiente ejemplo se ASUME que la implicación/doble implicación se ingresa en el formato correcto para ser evaluada directamente por eval
            # (ej. p IMPLICA q), y es reemplazada después de la sustitución de T/F.
            # Un manejo *simple* y *básico* sin funciones/clases/diccionarios, asumiendo un solo operador IMPLICA o DOBLE_IMPLICA:
            
            p_val = p
            q_val = q
            resultado = False # Valor por defecto.

            if "IMPLICA" in proposicion_evaluar:
                # p => q  equivale a (not p) or q
                if (not p_val) or q_val:
                    resultado = True
                else:
                    resultado = False
            elif "DOBLE_IMPLICA" in proposicion_evaluar:
                # p <=> q equivale a (p and q) or (not p and not q)
                if (p_val and q_val) or (not p_val and not q_val):
                    resultado = True
                else:
                    resultado = False
            else: # Usar eval para los operadores and, or, not
                # Se utiliza el eval forzado para simplificar la evaluación de and, or, not
                resultado = eval(proposicion_temp)

            # Impresión de la fila
            print(f"{'T' if p else 'F'} | {'T' if q else 'F'} | {'T' if resultado else 'F'}        ")
            
            # Conteo para la clasificación
            if resultado:
                resultado_final_es_True = resultado_final_es_True + 1
            else:
                resultado_final_es_False = resultado_final_es_False + 1

else:
    print("Proposición no válida o no soportada (solo se permiten proposiciones de p y/o q).")
    # Para evitar clasificar sin resultados
    exit()


# --- Clasificación ---
print("\n--- Clasificación ---")

# En total hay 2^variables_encontradas filas
total_filas = 0
if variables_encontradas == 1:
    total_filas = 2
elif variables_encontradas == 2:
    total_filas = 4

if total_filas == resultado_final_es_True:
    print("La proposición es una *TAUTOLOGÍA* (Todos los resultados son Verdaderos).")
elif total_filas == resultado_final_es_False:
    print("La proposición es una *CONTRADICCIÓN* (Todos los resultados son Falsos).")
else:
    print("La proposición es una *CONTINGENCIA* (Hay resultados Verdaderos y Falsos).")