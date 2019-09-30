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
    #first find the speed of a block at the bottom of the ramp


    #now find the final speed of the blocks after the collision, and return that value



#here's one way you could plot final velocity vs. initial height
#reuse/alter this code to investigate how varying m_1, m_2, or h
#changes the final velocity of the blocks 
for h in range(1,100,2):
  pyplot.plot(h,solver(5,5,h),'ro')


pyplot.show()
    
