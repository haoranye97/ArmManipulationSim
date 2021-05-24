import numpy as np
import matplotlib.pyplot as plt

def rand(mu, sigma):
    return np.random.beta(mu, sigma)

def ucb(t, me, T, sigma, mi, tp):
    return me + 3 * sigma * np.sqrt(np.log(T)/t)

def ts(t, me, T, sigma, mi, tp):
    return np.random.normal(me, 1.0 / t)

def gr(t, me, T, sigma, mi, tp):
    if(tp == 1):
        return np.random.random()
    return me

def find(n, b, m, f, i, mi, T, sigma, t):
    ep = min(1, 20/i)
    tp = 1
    #print(np.random.random(), ep,i, tp)
    if(np.random.random()> ep):
        tp = 0
    ret = 0
    ma = -1000000
    for j in range(m):
        me = t[j] / n[j]
        tmp = f(n[j], me, T, sigma, mi, tp)
        #print(tmp)
        if(tmp > ma):
            ret = j
            ma = tmp
    return ret
def work(bb, mf, nb):
    print(bb)
    sigma = 1
    mu = [1, 2, 3]
    m = 3
    ep = 100
    T = 10000
    avreg = [0 for i in range(T+1)]
    for qq in range(ep):
        b = []
        for j in bb:
            b.append(j)
        n = [1 for i in range(m)]
        t = []
        for i in range(m):
            tmp = rand(mu[i], sigma)
            t.append(min(1, tmp + b[i]));
            b[i] -= min(b[i], 1 - tmp);
        ma = 1 - 1 / (1 + max(mu))
        mi = 0
        k = 0
        for i in range(m):
            #print(1 - 1 / (1 + mu[i]) )
            if(1 - 1 / (1 + mu[i]) == ma):
                k = i
        for i in range(m):
            if(i != k and 1 - 1 / (1 + mu[i]) > mi):
                mi = 1 - 1 / (mu[i] + 1)
        mi = ma - mi
        #print(ma, mi)
        reg = [ma * m - sum([1 - 1 / (1 + i) for i in mu])]
        xx = [np.log(m)]
        for i in range(T):
            #print(bb)
            j = find(n, b, m, mf, i + m + 1, mi, T, sigma, t)
            #if(i % 100 == 0):
            #    print(i, j)
            #    print([t[q] / n[q] for q in range(m)])
            #    print(n)
            reg.append(reg[-1] +  ma - (1 - 1/ (1 + mu[j])))
            n[j] += 1
            tmp = rand(mu[j], sigma)
            t[j] += min(1, tmp + b[j])
            b[j] -= min(1 - tmp, b[j])
            xx.append(np.log(i + m + 1))
        for i in range(T+1):
            avreg[i] += reg[i] / ep
    return avreg[-1]
    #plt.subplot(1,3,nb)
    #plt.plot(xx, avreg)
if __name__ == '__main__':
    plt.subplot(1,3,1);
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb/2,bb/2,0],ucb,1))
    plt.plot(x,y,label='B1=B2=B/2,B3=0')
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb,0,0],ucb,1))
    plt.plot(x,y,label='B1=B,B2=B3=0')
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb/2,bb/2,bb/2],ucb,1))
    plt.plot(x,y,label='B1=B2=B3=B/2')
    plt.ylabel('Regret')
    plt.xlabel('B')
    plt.legend()
    plt.subplot(1,3,2);
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb/2,bb/2,0],gr,1))
    plt.plot(x,y,label='B1=B2=B/2,B3=0')
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb,0,0],gr,1))
    plt.plot(x,y,label='B1=B,B2=B3=0')
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb/2,bb/2,bb/2],gr,1))
    plt.plot(x,y,label='B1=B2=B3=B/2')
    plt.ylabel('Regret')
    plt.xlabel('B')
    plt.legend()   
    plt.subplot(1,3,3);
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb/2,bb/2,0],ts,1))
    plt.plot(x,y,label='B1=B2=B/2,B3=0')
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb,0,0],ts,1))
    plt.plot(x,y,label='B1=B,B2=B3=0')
    x = []
    y = []
    for bb in range(0, 105, 5):
        x.append(bb)
        y.append(work([bb/2,bb/2,bb/2],ts,1))
    plt.plot(x,y,label='B1=B2=B3=B/2')
    plt.ylabel('Regret')
    plt.xlabel('B')
    plt.legend() 
    #work(0,gr,2)
    #work(10,gr,2)
    #work(100,gr,2)
    print(1)
    plt.show()
     

