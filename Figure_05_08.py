import matplotlib.pyplot as plt
import utilsplot

from utils import tf

s = tf([1, 0])

G = (-s + 1)/(s + 1)
Kc = [0.1, 0.5, 0.9]
K = -1*s/((1 + 0.02*s)*(1 + 0.05*s))

plt.figure('Figure 5.8')
utilsplot.freq_step_response_plot(G, K, Kc, 0.2, 'S')
plt.show()
