Title: Einige Mathematik Definitionen
Date: 2013-11-11 16:10
Category: Maths
Tags: maths, vectoranalysis, differentialequations
Author: x4343
Summary: Some important math definitions for my study

Hier eine zusammenhanglose Ansammlung an Definitionen, die mir im Laufe des Studiums über den Weg gelaufen sind.

Viele davon werden sicher nicht allzu oft angewandt, trotzdem - oder gerade deshalb - schreibe ich sie mal auf.
Wer weiß, wo die entsprechenden Zettel mit den Definitonen und ihren Erklärungen gelandet sind, falls man sie mal braucht...

# #1: Definition: Sternförmig

Die Sternförmigkeit kommt u.a. in der Vektoranalysis vor.

$ \exists a \in \forall x \in M : \left\\{ y: y = x+t(a-x), t \in [0,1] \right\\} \subseteq M $

Grob gesagt drückt die Definition folgendes aus: 

Jeder Punkt $\vec{x} \in M$ lässt sich durch eine Strecke mit $\vec{x_0}$ verbinden. Die Strecke verlässt $M $ nicht.

Das trivialste Beispiel für eine sternförmige Menge ist der 3 dimensionale Raum $ \mathbb{R} $ an sich.

[![Zeichnung_sternförmig](/static/pictures/maths/sternfoermig.png)](/static/pictures/maths/sternfoermig.svg)

# #2: Definition: Lipschitz-stetig

Die Funktion $f: I \rightarrow \mathbb{R} $  ist Lipschitz-stetig auf $I$, falls gilt:

$ \exists L > 0 \forall x, y \in I : |f(x) - f(y)| \le L |x-y|	$
 
