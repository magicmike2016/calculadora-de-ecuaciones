# calculadora-de-ecuaciones
resuleve ecuaciones por el método de Eulier
# Solución de una ecuación diferencial usando el método de Euler

## 📌 Descripción

En este proyecto se resuelve una ecuación diferencial ordinaria separable:

dy/dt = y

Primero se obtiene la solución analítica usando el método de separación de variables, y después se aproxima la solución usando el método numérico de Euler.

---

## ✏️ Solución analítica

Separando variables:

(1/y) dy = dt

Integrando:

ln(y) = t + C

Solución general:

y(t) = Ce^t

Con condición inicial y(0) = 1:

y(t) = e^t

---

## 🧮 Método de Euler

Se utiliza la fórmula:

y_{n+1} = y_n + h f(t_n, y_n)

Parámetros:
- Intervalo: [0,1]
- Paso: h = 0.2
- Condición inicial: y(0) = 1

---

## 📊 Resultados

Se comparan:
- Solución exacta: y = e^t
- Aproximación por Euler

Se incluye una gráfica para visualizar la diferencia.

---

## ▶️ Cómo ejecutar

1. Instalar dependencias:

pip install numpy matplotlib

2. Ejecutar:

python main.py

---

## 📁 Archivos

- main.py → código principal
- README.md → explicación del problema
