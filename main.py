import matplotlib.pyplot as plt
import numpy

#Function Definitions
#Question 1
def plot_quadratic(a , b , c , clr):
  x = list(range(-10 , 11))
  y = [ (a * i ** 2 + b * i + c) for i in x]
  plt.plot(x, y, label = 'linear', linestyle="-" , color = clr)
  plt.show(block = 0)
  plt.pause(5)
  plt.close()

#Question 2
def plot_linear(a, b, clr):
  x = list(range(-10 , 11))
  y = [ (a*i + b) for i in x]
  plt.plot(x, y, label = 'linear', linestyle="-" , color = clr)
  plt.show(block = 0)
  plt.pause(5)
  plt.close()

#Question 3
def plot_me(a,b,c,d,clr):
  x = numpy.arange(-3.0, 3.0, 0.05)
  y = [(a * i ** 3 + b * i ** 2 + c * i + d) for i in x]
  plt.plot(x, y, label = 'cubic', linestyle="-" , color = clr)
  plt.grid(1)
  plt.show(block = 0)
  plt.pause(25)
  plt.close()

# Function Callings
plot_quadratic(1 , 2 , 5 , 'r') # Question 1
plot_linear(6, 7, 'r') # Question 2
plot_me(1 , 1 , 4 , 4 , 'r') # Question 3