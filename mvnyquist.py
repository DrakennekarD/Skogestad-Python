import numpy
import numpy.linalg
import matplotlib.pyplot as plt

w = numpy.logspace(-2, 2, 1000)
alls = 1j*w
I = numpy.eye(2, 2)


def G(s):
    G = (1/((s + 1)*(s + 2)*(s - 1)) *
         numpy.matrix([[(s-1)*(s+2), (s-1)**2], [-(s+1)*(s+2), (s-1)*(s+1)]]))
    return G


def K(s):
    return I

image = numpy.array([numpy.linalg.det(I + G(s)*K(s)) for s in alls])

plt.plot(numpy.real(image), numpy.imag(image))
plt.show()
