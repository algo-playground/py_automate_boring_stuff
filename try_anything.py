import theano.tensor as T
from theano import function
x = T.wscalar('x')
y = T.wscalar('y')
z = x + y
f = function([x, y], z)

print(f(2,3))