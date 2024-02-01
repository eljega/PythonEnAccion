import numpy as np
from sympy import symbols, Eq, solve, diff, integrate

def resolver_sistema_ecuaciones_lineales(coeficientes, resultados):
    """
    antes de comenzar recuerda instalas numpy y sympy en tu entorno virtual 

    resuelve un sistema de ecuaciones lineales representado por Ax = B.

    Args:
        coeficientes (list): Lista de listas con los coeficientes del sistema.
        resultados (list): Lista con los resultados de cada ecuación.

    Returns:
        ndarray: solucion del sistema de ecuaciones.
    """
    A = np.array(coeficientes)
    B = np.array(resultados)
    solucion = np.linalg.solve(A, B)
    return solucion

def diferenciacion_simbolica(funcion, variable):
    """
    realiza la diferenciacion simbolica de una funcion.

    Args:
        funcion: Funcion simbolica a diferenciar.
        variable: Variable respecto a la cual se diferenciará la funcion.

    Returns:
        Expr: Derivada de la funcion.
    """
    derivada = diff(funcion, variable)
    return derivada

def integracion_simbolica(funcion, variable):
    """
    Realiza la integracion simbolica de una funcion.

    Args:
        funcion: Funcion simbolica a integrar.
        variable: Variable respecto a la cual se integrara la funcion.

    Returns:
        Expr: Integral indefinida de la funcion.
    """
    integral = integrate(funcion, variable)
    return integral

#este es un ejemplo para resolver ecuaciones lineales
coeficientes = [[2, 1], [1, -1]]
resultados = [0, 3]
solucion = resolver_sistema_ecuaciones_lineales(coeficientes, resultados)
print(f"Solucion del sistema de ecuaciones lineales: {solucion}")

# ejemplo de diferenciación e integracion simbolica
x = symbols('x')
funcion = x**2 + 3*x + 2
derivada = diferenciacion_simbolica(funcion, x)
integral = integracion_simbolica(funcion, x)
print(f"La derivada de {funcion} respecto a x es: {derivada}")
print(f"La integral de {funcion} respecto a x es: {integral}")
