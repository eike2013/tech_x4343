Title: Wichtige Formeln zur Vektoranalysis
Date: 2013-11-11 18:00
Category: Maths
Tags: maths, vectoranalysis, differentialequations
Author: x4343
Summary: Vektoranalysis

# #1: Ebene und räumliche Kurven

## 1.1 Vektorielle Darstellung einer Kurve

Darstellung einer Kurve durch einen parameterabhängigen Ortsvektor

Ortsvektor einer ebenen Kurve:

\\[  \vec{r}(t) = x(t) \vec{e}_x + y(t) \vec{e}_y = \left( \begin{array}{c} x(t) \\ y(t) \end{array} \right)  \\]

Ortsvektor einer Raumkurve

\\[  \vec{r}(t) = x(t) \vec{e}_x + y(t) \vec{e}_y + z(t) \vec{e}_z = \left( \begin{array}{c} x(t) \\\ y(t) \\\ z(t) \end{array} \right)  \\]

## 1.2 Differentiation eines Vektors nach einem Parameter

Tangentenvektor einer ebenen Kurve

\\[  \dot{\vec{r}}(t) = \dot{x}(t) \vec{e}_x + \dot{y}(t) \vec{e}_y = \left( \begin{array}{c} \dot{x}(t) \\\ \dot{y}(t) \end{array} \right) \\]

Tangentenvektor einer Raumkurve

\\[ \dot{\vec{r}}(t) = \dot{x}(t) \vec{e}_x + \dot{y}(t) \vec{e}_y + \dot{z}(t) \vec{e}_z = \left( \begin{array}{c} \dot{x}(t) \\\ \dot{y}(t) \\\ \dot{z}_t\end{array} \right) \\]

Wobei $ \dot{\vec{r}}(t) = \frac{d\vec{r}}{dt} $ die 1. Ableitung des Ortsvektors $\vec{r} = \vec{r}(t) $ nach dem Paramter $ t $ ist.

Ableitungsregeln für Summen und Produkte von Vektoren

Summenregel:

\\[ \frac{d}{dt}(\vec{a}+\vec{b}) = \dot{\vec{a}} + \dot{\vec{b}} \\]

Produktregel für ein Skalarprodukt:

\\[ \frac{d}{dt}(\vec{a} \cdot \vec{b}) = \dot{\vec{a}} \cdot \vec{b} + \vec{a} \cdot \dot{\vec{b}} \\]

Produktregel für ein Vektorprodukt:

\\[ \frac{d}{dt}(\vec{a} \times \vec{b}) = \dot{\vec{a}} \times \vec{b} + \vec{a} \times {\vec{b}} \\]

Für ein Produkt aus einer skalaren und einer Vektorfunktion gilt:

\\[  \frac{d}{dt} (\phi\vec{a}) = \dot{\phi}\vec{a} + \phi\dot{\vec{a}} \\]

Geschwindigkeitsvektor (1. Ableitung des Ortsvektors nach der Zeit):

\\[  \vec{v}(t) = \dot{\vec{r}(t)} \\]

Beschleunigungsvektor (2. Ableitung des Ortsvektors nach der Zeit):

\\[  \vec{a}(t) = \dot{\vec{v}(t)} = \ddot{\vec{r}(t)} \\]

## 1.3 Bogenlänge

Bogenlänge einer ebenen Kurve:

\\[  s = \int_{t_1}^{t_2} | \dot{\vec{r}} dt | = \int_{t_1}^{t_2} \sqrt{\dot{x}^2 + \dot{y}^2} dt \\]

Bogenlänge einer Raumkurve:

\\[  s = \int_{t_1}^{t_2} | \dot{\vec{r}} dt | = \int_{t_1}^{t_2} \sqrt{\dot{x}^2 + \dot{y}^2 + \dot{z}^2} dt \\]

## 1.4 Tangenten- und Hauptnormaleneinheitsvektor

Tangenteneinheitsvektor:

\\[  \vec{T} \frac{\dot{\vec{r}}}{|\dot{\vec{r}}|} = \frac{1}{|\dot{\vec{r}}|} \dot{\vec{r}}  \\] mit $ |\vec{T}| = 1 $

Hauptnormaleneinheitsvektor

\\[  \vec{N} \frac{\dot{\vec{T}}}{|\dot{\vec{T}}|} = \frac{1}{|\dot{\vec{T}}|} \dot{\vec{T}}  \\] mit $ |\vec{N}| = 1 $

$ \vec{N} $ zeigt in Richtung der Kurvenkrümmung.

## 1.5 Krümmung einer Kurve

Krümmung einer Raumkurve $ \vec{r} = \vec{r}(s)) $ (s: Bogenlänge)

\\[ \kappa \left|\frac{d\vec{T}}{ds}\right| = |\dot{\vec{T}}(s)|   \\]

Krümmung einer Raumkurve $ \vec{r} = \vec{r}(t) $ (t: belieb. Param.)

\\[ \kappa = \frac{\left|\dot{\vec{r}}\right| \times \ddot{\vec{r}}}{|\dot{\vec{r}}|^3} \forall \dot{\vec{r}} \not 0 \\]

## 1.6 Tangential- und Normalkomponenten

Am Beispiel des Geschwindigkeitsvektors:

\\[ \vec{v} = v_T \vec{T} + v_N \vec{N} = v \vec{T} + 0 \vec{N} = v \vec{T} \\]

... des Beschleunigungsvektors

\\[ \vec{a} = a_T \vec{T} + a_N \vec{N} =  \dot{\vec{v}} \vec{T} + \frac{v^2}{\varrho} \vec{N} = \dot{\vec{v}} + \kappa v^2 \vec{N}  \\]

# #2: Flächen im Raum


# #3: Skalar- und Vektorfelder


# #4: Gradient eines Skalarfeldes


# #5: Divergenz und Rotation eines Vektorfeldes


# #6: Koordinatensysteme


# #7: Linien- und Kurvenintegrale


# #8: Oberflächenintegrale


# #9: Integralsätze von Gauß und Stokes


# Useful Linkx
 
