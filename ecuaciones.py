import numpy as np
import matplotlib.pyplot as plt

# Definimos la ecuación diferencial: dy/dt = y
def f(t, y):
    return y

# Solución exacta
def solucion_exacta(t):
    return np.exp(t)

# Método de Euler
def euler(f, t0, y0, h, t_final):
    t_values = [t0]
    y_values = [y0]
    
    t = t0
    y = y0
    
    while t < t_final:
        y = y + h * f(t, y)
        t = t + h
        
        t_values.append(round(t, 2))
        y_values.append(y)
    
    return np.array(t_values), np.array(y_values)

# Parámetros
t0 = 0
y0 = 1
h = 0.2
t_final = 1

# Euler
t_euler, y_euler = euler(f, t0, y0, h, t_final)

# Solución exacta
t_exact = np.linspace(0, 1, 100)
y_exact = solucion_exacta(t_exact)

# Mostrar resultados
print("t (Euler):", t_euler)
print("y (Euler):", y_euler)

# Gráfica
plt.plot(t_exact, y_exact, label="Solución exacta", linewidth=2)
plt.plot(t_euler, y_euler, 'o--', label="Euler")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Método de Euler vs Solución Exacta")
plt.legend()
plt.grid()
plt.show()
