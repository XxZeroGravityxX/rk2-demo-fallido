#! /usr/bin/env python

'''
Este script resuelve el pendulo simple usando RK2.
'''

import numpy as np
import matplotlib.pyplot as plt


A = np.pi / 30
w = np.sqrt(10)

plt.figure(1)
plt.clf()
#primero se hacen float los int (np.pi es un float por defecto)
t = np.linspace(0, 5 * 2 * np.pi / w, 400)

plt.plot(t, A * np.cos(w * t)) #Se cambia sen por cos debido a que sino, no se satisfacen las condiciones iniciales


def f(phi, w):
    return w, -10 * np.sin(phi)

def get_k1(phi_n, w_n, h, f):
    f_eval = f(phi_n, w_n)
    return h * f_eval[0], h * f_eval[1]

def get_k2(phi_n, w_n, h, f):
    k1 = get_k1(phi_n, w_n, h, f)
    f_eval = f(phi_n + k1[0]/2.0, w_n + k1[1]/2.0)#se coloca un float, para entregar numeros con decimales y no solo enteros
    return h * f_eval[0], h * f_eval[1]

def rk2_step(phi_n, w_n, h, f):
    k2 = get_k2(phi_n, w_n, h, f)
    '''Aqui ya se multiplico en la funcion get_k2 y get_k1 por h las variables k1 y k2, por lo que es erroneo volver a hacerlo'''
    phi_n1 = phi_n + k2[0]
    w_n1 = w_n + k2[1]
    return phi_n1, w_n1

N_steps = 40000
h = 10. / N_steps
phi = np.zeros(N_steps)
w = np.zeros(N_steps)

phi[0] = A
w[0] = 0
for i in range(1, N_steps):
    phi[i], w[i] = rk2_step(phi[i-1], w[i-1], h, f)



t_rk = [h * i for i in range(N_steps)]

plt.plot(t_rk, phi, 'g')




plt.xlabel('tiempo')
plt.ylabel('$\phi(t)$', fontsize=18)
plt.show()
plt.draw()
