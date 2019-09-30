from math import sqrt
from matplotlib import pyplot

# A block of mass m_1 slides down a frictionless ramp of height h and
# collides inelastically with a block of m_2 that is initially at rest.
# The solver function uses an energy calculation to find the speed of
# m_1 at the bottom of the ramp, and then uses a momentum calculation to
# find the final speed of the blocks after they stick together.
# Lastly, we can use pyplot to vary one of the parameters (e.g., the
# height of the ramp h, while holding the other parameters constant)
# and see how the ramp height affects the final velocity of the system

def solver(m_1,m_2,h):
    g=9.8
    #first find the speed of a block at the bottom of the ramp
    potential_energy = m_1*g*h
    v_1 = sqrt(2*potential_energy/m_1)

    #now find the final speed of the blocks after the collision and return that value
    total_momentum = m_1*v_1+m_2*0
    total_mass = m_1+m_2
    v_final = total_momentum/total_mass
    return v_final


for h in range(1,100,2):
    pyplot.plot(h,solver(5,5,h),'ro')

for m_2 in range(1,100,2):
    pyplot.plot(m_2,solver(5,m_2,20),'bo')

for m_1 in range(1,100,2):
    pyplot.plot(m_1,solver(m_1,5,20),'go')

pyplot.show()
    
