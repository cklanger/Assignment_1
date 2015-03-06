from math import pi

G=6.67e-11
M=5.97e24
R=6.371e6

T=float(input("Enter the period T of the orbit: T="))

h=((G*M*T*T)/(4*pi*pi))**(1/3)-R

print("The altitude above the Earth's surface is h=",h)


# result for T=24 hr is h(24hr)~3.5856e7 m
# result for T=90 min is h(90min)~2.7932e5 m
# result for T=45 min is h(45min)~-2.1816e6 m
# so, T=45 min cannot happen because h<0,
# which corresponds to an orbit lying inside the Earth.
# the difference between altitudes for T=24 hr and
# T=23.93 hr is approximately delta(h)~8.2147e4 m
# or about 82 km (a significant difference!)