import matplotlib.pyplot as plt

#Script that implements a basic Euler's forward method
def euler(y,t0,tf,h,f):
    n = int((tf-t0)/h)
    tx = [t*h for t in range(n+1)]
    yx = []
    yy = y
    for i in range(len(tx)):
        yx.append(yy + h*tx[i]*f(yy,tx[i]))
        yy = yx[i]
    return tx, yx 

def dy(y, t):
    #return 0-10*y
    return 0.5*y*(1-y)


y0 = 0.004
tt, yt = euler(y0,0.0,13.0,0.1,dy)

plt.plot(tt,yt)
plt.show()
