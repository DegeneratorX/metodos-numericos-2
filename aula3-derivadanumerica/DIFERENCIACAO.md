# Ementa

- Unidade 1: Diferenciação
- Unidade 2: Integração
- Unidade 3: Autovalores e Autovetores
- Unidade 4: Problemas de Valores Iniciais
- Unidade 5: Problemas de Valores de Contorno

- Prova 1: Unidade 1 e 2
- Prova 2: Unidade 3
- Prova 3: Unidades 4 e 5

# Diferenciação 1

Existem 3 tipos de filosofias para fazer o cálculo de derivadas. A **Forward**, a **Backward** e a **Central**.

![](2023-03-28-16-42-11.png)

A forward tenta aproximar a reta secante para a tangente pela direita.

A backward tenta aproximar a reta secante para a tangente pela esquerda.

A central tenta aproximar pelos dois lados a reta secante para a tangente no exato ponto médio.

## Forward

Seja f(x) uma função sobre x.

A derivada de f(x) em **Forward** é:

$$\boxed{\Large f'(x) = \frac{df(x_0)}{dx} \cong \lim_{\Delta x \to 0} \frac{f(x_0-\Delta x)-f(x_0)}{\Delta x}}$$

![](2023-03-15-10-34-57.png)

É chamado de forward, pois pega um ponto da frente de distância $\Delta x$, e se diminuirmos $\Delta x$ tendendo a zero, então a reta $r$ secante se aproxima pra trás e vira a inclinação da reta tangente.

> Nota: esse é o tipo mais utilizado no cálculo diferencial e integral.

> Nota 2: a derivada é aproximada ($\cong$), ou seja, existe um erro numérico na operação. Será explicado mais tarde.

## Backward

Seja f(x) uma função sobre x.

A derivada de f(x) em **Backward** é:

$$\boxed{\Large f'(x_f) \cong \lim_{\Delta x \to 0} \frac{f(x_f)-f(x_f - \Delta x)}{\Delta x}}$$

![](2023-03-15-11-55-08.png)

É chamado de backward, pois pega um ponto de trás de distância $\Delta x$ em relação ao ponto principal, e se diminuirmos $\Delta x$ tendendo a zero, então a reta $r$ secante se aproxima pra trás e vira a inclinação da reta tangente.

## Central

Seja f(x) uma função sobre x.

A derivada de f(x) em **Central** é:

$$\boxed{\Large f'(x_0) \cong \lim_{\Delta x \to 0} \frac{f(x_0+\Delta x)-f(x_0 - \Delta x)}{2\Delta x}}$$

![](2023-03-15-12-02-23.png)

É chamado de central, pois pega dois pontos, na frente e trás de distância $\Delta x$ em relação ao ponto principal, e se diminuirmos $\Delta x$ tendendo a zero, então a reta $r$ secante se aproxima pelos dois lados (vai pra baixo) e vira a inclinação da reta tangente.

### Exemplo: aplicação em fórmula trigonométrica

Vamos calcular: $f(1)$, $f(1+0.001)$ e $f(1-0.001)$ para a seguinte função $f$:

$\Large f(x) = \frac{\sinh x}{2 + \ln x}$

Resolvendo, temos:

$f(1) = \frac{\sinh 1}{2+\ln 1} = 0.5876$

$f(1+0.001) = \frac{\sinh 1.001}{2+\ln 1.001} = 0.58808$

$f(1-0.001) = \frac{\sinh 0.999}{2+\ln 0.999} = 0.58712$

Portanto, temos resultados bem próximos. Qual o mais preciso?

O que sabemos é que pegamos um ponto a frente e atrás, de distância $\Delta x$.

Usando as fórmulas de derivada para cada filosofia e substituindo nos pontos, temos:

Forward: $f'(1) \cong \frac{f(1+0.001) - f(1)}{\Delta x} = \frac{0.58808 - 0.5876}{0.001} = 0.47794$

Backward: $f'(1) \cong \frac{f(1) - f(1-0.001)}{\Delta x} = \frac{0.5876-0.58712}{0.001} = 0.47754$

Central: $f'(1) \cong \frac{f(1+0.001) - f(1-0.001)}{2\cdot \Delta x} = \frac{0.58808 - 0.58712}{2\cdot 0.001} = 0.47774$

Se fizermos o cálculo analítico de f'(1), resulta em 0.47774, muito próximo da filosofia Central. O que nos indica que a Central é muito mais precisa, justamente por trabalhar com dois pontos vizinhos.

## Derivada segunda de todas as filosofias

O algebrismo que prova as derivadas segunda estará no final desse arquivo. As fórmulas de derivada segunda são essas:

### Forward

$$\Large f''(x_0) = \frac{d^2 f(x_0)}{dx^2} = \boxed{\frac{f'(x_0 + 2\Delta x)- 2f'(x_0 + \Delta x) + f'(x_0)}{(\Delta x)^2}}$$

### Backward

$$\Large f''(x_0) =  \frac{d^2 f(x_0)}{dx^2} = \boxed{\frac{f'(x_0)-2f'(x_0-\Delta x)+f'(x_0-2\Delta x)}{(\Delta x)^2}}$$

### Central

$$\Large f''(x_0) =  \frac{d^2 f(x_0)}{dx^2} = \boxed{\frac{f'(x_0 + 2\Delta x) - 2f'(x_0) + f'(x_0 - 2\Delta x)}{4(\Delta x)^2}}$$

> Nota: se eu chamar $2\Delta x$ de $\Delta\overline{x}$, então a segunda derivada ficaria $f''(x) = \boxed{\frac{f'(x_0 + 2\Delta x) - 2f'(x_0) + f'(x_0 - 2\Delta x)}{(\Delta\overline{x})^2}}$.

## Derivada de ordem $n$ de todas as filosofias

### Forward

$$\boxed{f^{(k)}(x_i) \cong \frac{f^{(k-1)}(x_i-\Delta x) - f^{(k-1)}(x_i)}{\Delta x}}$$

## Derivada Parcial

A derivada parcial serve para derivar funções em relação a uma ou mais variáveis.

### Exemplo:

Seja essa função f(x,y):

$f(x,y) = x^4 + 3x^3y + 4x^2y^2+6xy^3+10y^4$

Derivando sobre x, temos...

$\frac{\partial f}{\partial x} = 4x^3+9x^2y+8xy^2+6y^3$

E sobre y...

$\frac{\partial f}{\partial y} = 3x³+8x²y+18xy²+40y³$

Também é possível derivar parcialmente em função de $x^2$ e por aí em diante.

$\frac{\partial^2 f}{\partial x^2} = 12x^2 + 18xy + 8y^2$

$\frac{\partial^2 f}{\partial y^2} = 8x^2+36xy + 120y^2$

$\frac{\partial^2 f}{\partial x\partial y} = 9x^2 + 16xy + 18y^2$

$\frac{\partial^2 f}{\partial y\partial x} = 9x^2 + 16xy + 18y^2$

Perceba que os dois últimos casos são equivalentes.

## Série de Taylor

É uma expansão da função em torno de um ponto usando uma série de polinômio com infinitos termos.

Ou seja, a série pode dizer sobre o comportamento de uma função ao redor de um ponto particular. A série é essencialmente uma aproximação de um polinômio de uma função. Então olhando para os termos da série, você pode ter uma ideia de como a função se comporta enquanto você se afasta do ponto central.

![](2023-04-02-15-32-49.png)

Suponha uma função $f$ como na imagem acima. Suponha um $\bar{x}$ e uma distância vizinha $\bar{x} + \Delta x$. Ora, sabemos que  se o ponto $\bar{x}$ for próximo de $\bar{x} + \Delta x$, podemos fazer um chute inicial:

$$f(\bar{x} + \Delta x) = f(\bar{x})$$

Esse chute faria muito sentido se $Delta x$ fosse muito pequeno. Mas supondo que não, e que precisamos de mais um pouco de precisão. Podemos obter um termo a mais e que nos dará uma maior precisão do quão "alto" é $f(\bar{x} + \Delta x)$

Pra isso, traço uma tangente ao ponto $(\bar{x}, f(\bar{x}))$. Obtemos um ângulo $\alpha$, que é justamente o coeficiente angular, a tangente, ou seja, a derivada naquele ponto. Com esse ângulo, calculamos o cateto oposto sobre o adjacente. Assim:

$$\tan \alpha = f'(\bar{x}) = \frac{segundo termo}{\Delta x} \implies segundotermo = f'(\bar{x})\cdot \Delta x$$

Então somamos o segundo termo ao primeiro termo, e temos uma precisão maior desse $f(\bar{x} + \Delta x)$. Ficará assim:

$$f(\bar{x} + \Delta x) = f(\bar{x}) + f'(\bar{x})\cdot \Delta x$$

Já temos o segundo termo do que chamamos de série de Taylor. A série para provar o terceiro termo em diante exige mais cálculos, portanto basta saber que quanto mais termos a série tem, mais preciso o cálculo de $f(\bar{x} + \Delta x)$. Os outros termos são esses:

**Série de Taylor**

$$\boxed{\Large f(\bar{x} + \Delta x) = f(\bar{x}) + \left(\frac{1}{1!}\right)f'(\bar{x})\cdot \Delta x + \frac{1}{2!}f''(\bar{x})(\Delta x)^2 + \frac{1}{3!}f''1(\bar{x})(\Delta x)^3 + ... + \frac{1}{n!}f^{(n)}(\bar{x})(\Delta x)^n}$$

### Exemplo: Seno

Sabendo que o seno de 0 é 0, deseja-se saber o seno de 0.1 rad. É possível usar regra de três para descobrir, mas o número $\pi$ no final das contas é uma aproximação que também pode ser descoberta por meio de séries.

Sem o uso de regra de três, é possível encontrar o seno de diversos ângulos próximos dos já conhecidos com bastante precisão utilizando a série de Taylor. Nesse caso irei usar 5 termos:

$f(x + \Delta x) = \sin(x + \Delta x) = \cancel{\sin 0} + \cos 0\cdot 0.1 - \cancel{\frac{1}{2}\sin 0\cdot 0.1^2} - \frac{1}{3!}\cos 0\cdot 0.1^3 + \cancel{\frac{1}{4!}\sin 0\cdot 0.1^4} + \frac{1}{5!}\cos 0\cdot 0.1^5$

$f(x + \Delta x) = \sin(x + \Delta x) = 0.1 - 0.16667\cdot 0.001 + 0.00833\cdot 0.00001 = \boxed{0.0998}$

Se colocar na calculadora, verá que o seno de 0.1 é muito próximo de 0.0998. E quanto mais termos na série, mais preciso o resultado fica.

Já deu pra ver onde isso vai parar, né? Em um método numérico.

### Exemplo 2: Exponencial

Suponha $f(x) = e^{-x}$. Suas derivadas analíticas são:

$f'(x) = -e^{-x}$

$f''(x) = +e^{-x}$

$f'''(x) = -e^{-x}$

Quando eu avalio essas derivadas em um ponto $x_0$, fica assim:

$f'(x_0) = -e^{-x_0}$

$f''(x_0) = +e^{-x_0}$

$f'''(x_0) = -e^{-x_0}$

Eu posso pegar as derivadas e substituir na série de Taylor.

$$f(x) = f(x_0) + (-e^{-x_0})(x-x_0) + \frac{e^{-x_0}}{2!}(x-x_0)^2 + \frac{e^{-x_0}}{3!}(x-x_0)^3+...$$

E se eu substituir, por exemplo, $x_0$ por 1, fica:

$$f(x) = e^{-1} - (-e^{-1})(x-1) + \frac{e^{-1}}{2!}(x-1)^2 - \frac{e^{-1}}{3!}(x-1)^3+...$$

Ou seja, isso é um polonômio, e quanto mais eu expando os termos, extremamente menor vai ficando eles, pois é dividido por fatorial, que é um operador mais crescente que exponencial quanto ao seu comportamento assintótico, o que exigiria um custo computacional maior de análise de precisão.

Com $e^{-1} = 0.3678$, temos:

$$f(x) = 0.3678 - 0.3678(x-1) + \frac{0.3678}{2!}(x-1)^2-\frac{0.3678}{3!}(x-1)^3+...$$

Perceba de fato o comportamento polinomial dessa função. Ou seja, pra um dado $x$, eu obtenho $y$ pra qualquer ponto, desde que seja próximo do ponto $x_0 = 1$. E quanto mais termos, mais preciso o $y$ será em relação a $x$. E assim analiso o comportamento da função ponto a ponto do gráfico ao redor de $x_0$, de tal forma que consigo desenhar o gráfico da função em questão iterativamente. Se ficar longe demais de $x_0$ ou usar poucos termos, a imprecisão para $y$ aumentará.

![](2023-04-03-15-36-23.png)

# Derivada Primeira Numérica

Pegando o exemplo da função exponencial $e^{-x}$ e expandindo no ponto $x = 1$. Perceba que a série de Taylor é uma função que possui termos com derivadas. Se eu quiser obter a derivada ao invés da função polinomial, eu isolo o termo de derivada. Assim:

$$f(x) = e^{-1} - (-e^{-1})(x-1) + \frac{e^{-1}}{2!}(x-1)^2 - \frac{e^{-1}}{3!}(x-1)^3+...$$

$$-e^{-1}(x-1) = f(x) - e^{-1} - \frac{e^{-1}}{2!}(x-1)^2 + \frac{e^{-1}}{3!}(x-1)^3+...$$

Aqui eu isolei o termo de derivada primeira.

Perceba que eu multipliquei tudo por -1 para trabalhar melhor. Agora isolo apenas o termo da derivada primeira no lado esquerdo ($f'(x) = -e^{-1}$), passando (x-1) dividindo:

$$-e^{-1} = \frac{1}{(x-1)} \left(f(x) + e^{-1} - \frac{e^{-1}}{2!}(x-1)^2 + \frac{e^{-1}}{3!}(x-1)^3+...\right)$$

Aqui não faz muito sentido fazer isso se eu conheço as derivadas analíticas. Mas pra exemplificar, estou trabalhando com esse exemplo simples.

Agora vou voltar com as notações de funções genéricas:

$$f'(x_0) = \frac{1}{(x-1)} \left(f(x) + f(x_0) - \frac{f''(x_0)}{2!}(x-1)^2 + \frac{f'''(x_0) }{3!}(x-1)^3+...\right)$$

Basicamente essa é a maneira que fazemos para achar derivações numéricas. **Isolamos a derivada desejada**.

## Forward

Resgatando a série de Taylor expandindo $f(x)$, temos:

$$\boxed{\Large f(x) = f(x_0) + f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\frac{f'''(x_0)}{3!}(x-x_0)^3+...}$$

Considere a perturbação positiva como sendo $x = x_0 + \Delta x \implies x-x_0 = \Delta x$.

$$f(x_0+\Delta x) = f(x_0) + f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\frac{f'''(x_0)}{3!}(x-x_0)^3+...$$

Como $x - x_0 = \Delta x$, temos:

**Eq 1**
$$f(x_0+\Delta x) = f(x_0) + f'(x_0)\Delta x+\frac{f''(x_0)}{2!}\Delta x^2+\frac{f'''(x_0)}{3!}\Delta x^3+...$$

Se isolarmos a derivada $f'(x_0)$ como já fizemos em operações passadas para achar derivada, temos:

## Backward

Considere a perturbação negativa como sendo $x = x_0 - \Delta x \implies x-x_0 = -\Delta x$.

$$f(x_0-\Delta x) = f(x_0) + f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\frac{f'''(x_0)}{3!}(x-x_0)^3+... $$ 

Como $x - x_0 = -\Delta x$, temos:

**Eq 2**
$$f(x_0-\Delta x) = f(x_0) - f'(x_0)\Delta x+\frac{f''(x_0)}{2!}\Delta x^2-\frac{f'''(x_0)}{3!}\Delta x^3+...$$

Perceba que $-\Delta x$ faz alguns termos ficarem negativos quando o grau do expoente é ímpar. Qualquer termo elevado a um número par sempre será positivo.

## Central

Para $\Delta x$ muito menor que 1 (próximo do ponto de $x$), na medida que o $\Delta x$ vai sendo elevado a números maiores, os termos vão ficando menores, principalmente por conta da divisão por fatorial. Assim:

$$\left|f'(x_0)\Delta x\right| >> \left|\frac{f''(x_0)}{2!}\Delta x^2\right| >> \left|\frac{f'''_0}{3!}\Delta x^3\right| >> ...$$

Ou seja, os termos de maior ordem são os que mais dominam.

# Algebrismos Diversos

## 1 - Derivação Segunda das filosofias

- **Forward**

$\Large f''(x_0) \cong \frac{f'(x_0 + \Delta x) - f'(x_0)}{\Delta x}$

$\Large= \frac{\frac{f'(x_0 + 2\Delta x) - f'(x_0 + \Delta x)}{\Delta x} - \frac{f'(x_0 + \Delta x) - f'(x_0)}{\Delta x}}{\Delta x}$

$\Large\cong \frac{f'(x_0 + 2\Delta x)- 2f'(x_0 + \Delta x) + f'(x_0)}{(\Delta x)^2}$


- **Backward**

$\Large f''(x_0) = \frac{f'(x_0) - f'(x_0 - \Delta x)}{\Delta x}$

$\Large= \frac{\frac{f(x_0) - f'(x_0 - \Delta x)}{\Delta x} - \frac{f'(x_0 - \Delta x) - f'(x_0 - 2\Delta x)}{\Delta x}}{\Delta x}$

$\Large= \frac{1}{(\Delta x)^2}[f'(x_0)-2f(x_0-\Delta x)+f'(x_0-2\Delta x)]$


- **Central**

$\Large f''(x_0) = \frac{f'(x_0 + \Delta x) - f'(x_0 - \Delta x)}{2\Delta x}$

$\Large= \frac{\frac{f'(x_0 + 2\Delta x) - f'(x_0)}{2\Delta x} - \frac{f(x_0) - f'(x_0 - 2\Delta x)}{2\Delta x}}{2\Delta x}$

$\Large= \frac{1}{4(\Delta x)^2}[f'(x_0 + 2\Delta x) - 2f'(x_0) + f'(x_0 - 2\Delta x)]$

## 2 - Derivação Terceira das filosofias

- **Forward**

$\Large f'''(x_0) = \frac{f''(x_0 + \Delta x)- f''(x_0)}{\Delta x}$

$\Large= \frac{\frac{1}{(\Delta x)^2}[f''(x_0 + 3\Delta x) - 2f''(x_0+2\Delta x) + f''(x_0 + \Delta x) - f''(x_0 + 2x_0) + 2f''(x_0 + \Delta x) - f''(x_0)]}{\Delta x}$

$\Large= \frac{1}{(\Delta x)^3}(f''(x_0+3\Delta x)-3f''(x_0 + 2\Delta x)+ 3f''(x_0 + \Delta x) - f''(x_0))$

- **Backward**

>TODO

- **Central**

>TODO