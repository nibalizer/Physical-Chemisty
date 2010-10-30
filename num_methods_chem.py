
from scipy.integrate import trapz, simps

def trap(func, a, b, n):
    step = (b-a)/n
    y = []
    while a <= b:
        y.append(func(a))
        a += step
    area = trapz(y)
    return area
