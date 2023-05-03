from abc import ABC, abstractstaticmethod
import math
import numpy as np

"""
Biblioteca de Integração Numética usando os seguintes métodos:

Newton-Cotes (todos os graus, com intervalos abertos e fechados)
Gauss-Legendre (grau 1 a 4)
Gauss-Hermite
Gauss-Laguerre
Gauss-Chebychev

Autores:
Victor Martins
Luiz Gustavo
"""

class Integracao(ABC):
    @abstractstaticmethod
    def integrar(f, a, b, tol=1e-6):
        pass


class NewtonCotes(Integracao):
    @staticmethod
    def integrar(f, a, b, grau, tipo, tol=1e-6):
        # Indexação
        print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(
            "iteracoes", "particoes", "tamanho particao", "integral", "erro"))

        converge = True
        # Trabalho de início apenas com 1 partição, o próprio intervalo [a,b]
        particoes = 1
        # Iterações
        k = 0
        primeira_iteracao = True

        while converge:
            k += 1
            soma = 0
            tamanho_particao = (b-a)/particoes

            for particao in range(particoes):
                x_inicial = a+particao*tamanho_particao
                x_final = x_inicial+tamanho_particao

                if tipo == 0:
                    try:
                        h = (x_final-x_inicial)/grau
                    except ZeroDivisionError:
                        h = (x_final-x_inicial)/1
                    if grau == 0:
                        soma = soma + \
                            NewtonCotes.__fechada_grau_0(
                                f, x_inicial, x_final, h)
                    elif grau == 1:
                        soma = soma + \
                            NewtonCotes.__fechada_grau_1(f, x_inicial, h)
                    elif grau == 2:
                        soma = soma + \
                            NewtonCotes.__fechada_grau_2(f, x_inicial, h)
                    elif grau == 3:
                        soma = soma + \
                            NewtonCotes.__fechada_grau_3(f, x_inicial, h)
                    elif grau == 4:
                        soma = soma + \
                            NewtonCotes.__fechada_grau_4(f, x_inicial, h)
                    else:
                        print("Grau inválido.")

                elif tipo == 1:
                    h = (x_final-x_inicial)/(grau+2)
                    if grau == 0:
                        soma = soma + \
                            NewtonCotes.__aberta_grau_0(f, x_inicial, h)
                    elif grau == 1:
                        soma = soma + \
                            NewtonCotes.__aberta_grau_1(f, x_inicial, h)
                    elif grau == 2:
                        soma = soma + \
                            NewtonCotes.__aberta_grau_2(f, x_inicial, h)
                    elif grau == 3:
                        soma = soma + \
                            NewtonCotes.__aberta_grau_3(f, x_inicial, h)
                    elif grau == 4:
                        soma = soma + \
                            NewtonCotes.__aberta_grau_4(f, x_inicial, h)
                    else:
                        print("Grau inválido.")
                        return
                else:
                    print("Tipo inválido. A escolha era entre 0 (fechada) e 1 (aberta)")
                    return

            if primeira_iteracao:
                soma_anterior = 0
                primeira_iteracao = False
            else:
                soma_anterior = soma_atual

            soma_atual = soma
            erro = abs(soma_atual-soma_anterior)
            print("{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}".format(
                k, particoes, tamanho_particao, soma_atual, erro))

            if erro < tol:
                return soma_atual
            
            # Multiplico as partições por 2, pois assim corto pela metade cada 
            # vez mais o problema e somo tudo, procurando manter a simetria dos 
            # subproblemas e aumentando a precisão
            particoes *= 2

    # Soma de Riemann Fechada
    @staticmethod
    def __fechada_grau_0(f, x_inicial, x_final, h):
        return h*(f((x_inicial+x_final)/2))

    # Regra do Trapézio Fechada
    @staticmethod
    def __fechada_grau_1(f, x_inicial, h):
        # x_i = a + i*h (esse é o motivo de dentro de f() ser assim)
        return (1/2)*h*(f(x_inicial+0*h)+f(x_inicial+1*h))

    # Simpson 1/3
    @staticmethod
    def __fechada_grau_2(f, x_inicial, h):
        return (1/3)*h*(f(x_inicial+0*h)+4*f(x_inicial+1*h)+f(x_inicial+2*h))

    # Simpson 3/8
    @staticmethod
    def __fechada_grau_3(f, x_inicial, h):
        return (3/8)*h*(f(x_inicial+0*h)+3*f(x_inicial+1*h)+3*f(x_inicial+2*h)+f(x_inicial+3*h))

    # Regra de Boole
    @staticmethod
    def __fechada_grau_4(f, x_inicial, h):
        return (2/45)*h*(7*f(x_inicial+0*h)+32*f(x_inicial+1*h)+12*f(x_inicial+2*h)+32*f(x_inicial+3*h)+7*f(x_inicial+4*h))

    ####################

    # Soma de Riemann Aberta
    @staticmethod
    def __aberta_grau_0(f, x_inicial, h):
        return 2*h*(f(x_inicial+(0+1)*h))

    # Regra do Trapézio Aberta
    @staticmethod
    def __aberta_grau_1(f, x_inicial, h):
        return (3/2)*h*(f(x_inicial+(0+1)*h)+f(x_inicial+(1+1)*h))

    # Regra de Milne
    @staticmethod
    def __aberta_grau_2(f, x_inicial, h):
        return (4/3)*h*(2*f(x_inicial+(0+1)*h)-f(x_inicial+(1+1)*h)+2*f(x_inicial+(2+1)*h))

    # Sem nome especial
    @staticmethod
    def __aberta_grau_3(f, x_inicial, h):
        return (5/24)*h*(11*f(x_inicial+(0+1)*h)+f(x_inicial+(1+1)*h)+f(x_inicial+(2+1)*h)+11*f(x_inicial+(3+1)*h))

    # Sem nome especial
    @staticmethod
    def __aberta_grau_4(f, x_inicial, h):
        return (6/20)*h*(11*f(x_inicial+(0+1)*h)-14*f(x_inicial+(1+1)*h)+26*f(x_inicial+(2+1)*h)-14*f(x_inicial+(3+1)*h)+11*f(x_inicial+(4+1)*h))


class GaussLegendre(Integracao):
    @staticmethod
    def integrar(f, a, b, grau, tol=1e-6):
        print("{:^15}{:^15}{:^15}{:^15}{:^15}".format("iteracoes",
              "particoes", "tamanho particao", "integral", "erro"))
        converge = True
        # Trabalho de início apenas com 1 partição, o próprio intervalo [a,b]
        particoes = 1
        # Iterações
        k = 0
        primeira_iteracao = True
        while converge:
            k += 1
            soma = 0
            tamanho_particao = (b-a)/particoes
            for particao in range(particoes):
                x_inicial = a+particao*tamanho_particao
                x_final = x_inicial+tamanho_particao

                if grau == 1:
                    soma = soma + GaussLegendre.__grau_1(f, x_inicial, x_final)
                elif grau == 2:
                    soma = soma + GaussLegendre.__grau_2(f, x_inicial, x_final)
                elif grau == 3:
                    soma = soma + GaussLegendre.__grau_3(f, x_inicial, x_final)
                elif grau == 4:
                    soma = soma + GaussLegendre.__grau_4(f, x_inicial, x_final)
                else:
                    print("Grau inválido.")
                    return

            if primeira_iteracao:
                soma_anterior = 0
                primeira_iteracao = False
            else:
                soma_anterior = soma_atual

            soma_atual = soma
            erro = abs(soma_atual-soma_anterior)
            print("{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}{:^15.8f}".format(
                k, particoes, tamanho_particao, soma_atual, erro))

            if erro < tol:
                return soma_atual
            particoes *= 2

    # Função x(a_k)
    @staticmethod
    def __x(x_inicial, x_final, raiz_a_k):
        return ((x_inicial+x_final)/2) + ((x_final-x_inicial)/2) * raiz_a_k

    # Gauss-Legendre grau 1
    @staticmethod
    def __grau_1(f, x_inicial, x_final):
        x_1 = 0
        w_1 = 1
        return 2*(((x_final-x_inicial)/2)*(f(GaussLegendre.__x(x_inicial, x_final, x_1))*w_1))

    # Gauss-Legendre grau 2
    @staticmethod
    def __grau_2(f, x_inicial, x_final):
        x_1 = -np.sqrt(1/3)
        x_2 = +np.sqrt(1/3)
        w_1 = w_2 = 1
        return ((x_final-x_inicial)/2)*((f(GaussLegendre.__x(x_inicial, x_final, x_1))*w_1)+(f(GaussLegendre.__x(x_inicial, x_final, x_2))*w_2))

    # Gauss-Legendre grau 3
    @staticmethod
    def __grau_3(f, x_inicial, x_final):
        x_1 = -np.sqrt(3/5)
        x_2 = 0
        x_3 = +np.sqrt(3/5)
        w_1 = w_3 = 5/9
        w_2 = 8/9
        return ((x_final-x_inicial)/2)*((f(GaussLegendre.__x(x_inicial, x_final, x_1))*w_1)+(f(GaussLegendre.__x(x_inicial, x_final, x_2))*w_2)+(f(GaussLegendre.__x(x_inicial, x_final, x_3))*w_3))

    # Gauss-Legendre grau 4
    @staticmethod
    def __grau_4(f, x_inicial, x_final):
        x_1 = -np.sqrt((3+2*np.sqrt(6/5))/7)
        x_2 = -np.sqrt((3-2*np.sqrt(6/5))/7)
        x_3 = np.sqrt((3-2*np.sqrt(6/5))/7)
        x_4 = np.sqrt((3+2*np.sqrt(6/5))/7)
        w_1 = w_4 = (1/2)-((np.sqrt(5/6)/6))
        w_2 = w_3 = (1/36)*(18+np.sqrt(30))
        return ((x_final-x_inicial)/2)*((f(GaussLegendre.__x(x_inicial, x_final, x_1))*w_1)+(f(GaussLegendre.__x(x_inicial, x_final, x_2))*w_2)+(f(GaussLegendre.__x(x_inicial, x_final, x_3))*w_3) + (f(GaussLegendre.__x(x_inicial, x_final, x_4))*w_4))


# Hermite: a = -inf, b = +inf
class GaussHermite(Integracao):
    @staticmethod
    def integrar(f, grau):
        print("{:^15}".format("integral"))
        soma = 0

        if grau == 2:
            soma = GaussHermite.__grau_2(f)
        elif grau == 3:
            soma = GaussHermite.__grau_3(f)
        elif grau == 4:
            soma = GaussHermite.__grau_4(f)
        else:
            print("Grau inválido.")
            return
        print("{:^15.8f}".format(soma))
        return soma

 
    # Gauss-Hermite grau 2
    @staticmethod
    def __grau_2(f):
        x_1 = -1/np.sqrt(2)
        x_2 = +1/np.sqrt(2)

        w_1 = w_2 = np.sqrt(np.pi)/2

        return f(x_1)*w_1+f(x_2)*w_2

    # Gauss-Hermite grau 3
    @staticmethod
    def __grau_3(f):
        x_1 = -(np.sqrt(3/2))
        x_2 = 0
        x_3 = +(np.sqrt(3/2))

        w_1 = w_3 = np.sqrt(np.pi)/6
        w_2 = (2*np.sqrt(np.pi))/3

        return f(x_1)*w_1+f(x_2)*w_2+f(x_3)*w_3

    # Gauss-Hermite grau 4
    @staticmethod
    def __grau_4(f):
        x_1 = -(np.sqrt(3/2 + np.sqrt(3/2)))
        x_2 = -(np.sqrt(3/2 - np.sqrt(3/2)))
        x_3 = +(np.sqrt(3/2 - np.sqrt(3/2)))
        x_4 = +(np.sqrt(3/2 + np.sqrt(3/2)))

        w_1 = w_4 = np.sqrt(np.pi)/(4*(3 + np.sqrt(6)))
        w_2 = w_3 = -np.sqrt(np.pi)/(4*(np.sqrt(6) - 3))

        return f(x_1)*w_1+f(x_2)*w_2+f(x_3)*w_3+f(x_4)*w_4


# Laguerre: a = 0, b = inf
class GaussLaguerre(Integracao):
    @staticmethod
    def integrar(f, grau):
        print("{:^15}".format("integral"))
        soma = 0

        if grau == 2:
            soma = GaussLaguerre.__grau_2(f)
        elif grau == 3:
            soma = GaussLaguerre.__grau_3(f)
        elif grau == 4:
            soma = GaussLaguerre.__grau_4(f)
        else:
            print("Grau inválido.")
            return
        print("{:^15.8f}".format(soma))
        return soma

 
    # Gauss-Laguerre grau 2
    @staticmethod
    def __grau_2(f):
        x_1 = 2-np.sqrt(2)
        x_2 = 2+np.sqrt(2)

        w_1 = (1/4)*(2+np.sqrt(2))
        w_2 = (1/4)*(2-np.sqrt(2))

        return f(x_1)*w_1+f(x_2)*w_2

    # Gauss-Laguerre grau 3
    @staticmethod
    def __grau_3(f):
        x_1 = 0.4157745568
        x_2 = 2.2942803603
        x_3 = 6.2899450829

        w_1 = 0.7110930099
        w_2 = 0.2785177336
        w_3 = 0.0103892565

        return f(x_1)*w_1+f(x_2)*w_2+f(x_3)*w_3

    # Gauss-Laguerre grau 4
    @staticmethod
    def __grau_4(f):
        x_1 = 0.32255
        x_2 = 1.7458
        x_3 = 4.5366
        x_4 = 9.3951

        w_1 = 0.603115
        w_2 = 0.357347
        w_3 = 0.0388894
        w_4 = 0.000539278

        return f(x_1)*w_1+f(x_2)*w_2+f(x_3)*w_3+f(x_4)*w_4


# Chebychev: a = -1, b = +1
class GaussChebychev(Integracao):
    @staticmethod
    def integrar(f, grau):
        print("{:^15}".format("integral"))
        soma = 0

        if grau == 2:
            soma = GaussChebychev.__grau_2(f)
        elif grau == 3:
            soma = GaussChebychev.__grau_3(f)
        elif grau == 4:
            soma = GaussChebychev.__grau_4(f)
        else:
            print("Grau inválido.")
            return
        print("{:^15.8f}".format(soma))
        return soma

 
    # Gauss-Chebychev grau 2
    @staticmethod
    def __grau_2(f):
        x_1 = -1/np.sqrt(2)
        x_2 = +1/np.sqrt(2)

        w_1 = w_2 = np.pi/2

        return f(x_1)*w_1+f(x_2)*w_2

    # Gauss-Chebychev grau 3
    @staticmethod
    def __grau_3(f):
        x_1 = -(np.sqrt(3)/2)
        x_2 = 0
        x_3 = +(np.sqrt(3)/2)

        w_1 = w_2 = w_3 = np.pi/3

        return f(x_1)*w_1+f(x_2)*w_2+f(x_3)*w_3

    # Gauss-Chebychev grau 4
    @staticmethod
    def __grau_4(f):
        x_1 = -(np.sqrt(2 + np.sqrt(2))/2)
        x_2 = -(np.sqrt(2 - np.sqrt(2))/2)
        x_3 = +(np.sqrt(2 - np.sqrt(2))/2)
        x_4 = +(np.sqrt(2 + np.sqrt(2))/2)

        w_1 = w_2 = w_3 = w_4 = np.pi/4

        return f(x_1)*w_1+f(x_2)*w_2+f(x_3)*w_3+f(x_4)*w_4


def h(x):
    return 2*(math.sqrt(x)+np.cos(x/2))


def f(x):
    return (np.sin(2*x)+4*x**2+3*x)**2

if __name__ == '__main__':
    # NewtonCotes.integrar(f, a=0, b=1, grau=1, tipo=0)
    #GaussLegendre.integrar(f, a=0, b=1, grau=1)
    GaussChebychev.integrar(f,grau=4)
