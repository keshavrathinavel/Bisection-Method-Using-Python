# Bisection-Method-Using-Python
My implementation of the Bisection Method, an iterative numerical method, using Python. Numerial Methods are a popular topic taught in Engineering Mathematics courses. Here, I will be showing you how to use what I learnt in class to find roots of polynomial expressions using simple code.

Bisection method is the simplest among all the numerical schemes to solve the transcendental equations. This scheme is based on the intermediate value theorem for continuous functions .
Consider a transcendental equation f (x) = 0  which has a zero in the interval [a,b] and f (a) * f (b) < 0. Bisection scheme computes the zero, say c, by repeatedly halving the interval [a,b]. That is, starting with 

c = (a+b) / 2

The interval [a,b] is replaced either with [c,b] or with [a,c] depending on the sign of f (a) * f (c) . This process is continued until the zero is obtained. Since the zero is  obtained numerically the value of c may not exactly match with all the decimal places of the analytical solution of f (x) = 0 in the interval [a,b]. Hence any one of the        following mechanisms can be used to stop the bisection iterations :

C1 -> Fixing a priori the total number of bisection iterations N i.e., the length of the interval or the maximum error after N iterations in this case is less than | b-a | / 2N.

C2 -> By testing the condition  | ci - c i-1| (where i are the iteration number) less than some tolerance limit, say epsilon, fixed a priori. 

C3 -> By testing the condition | f (ci ) | less than some tolerance limit alpha again fixed a priori.

	
