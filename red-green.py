from random import random, sample, choice

nchannels = 20
nunits = 200
cpu = 5
nsteps = 200

us = []
cs = []

class channel():
    def __init__(s, n):
        s.n,s.s,s.ns=n,0,0
        cs.append(s)
    def p(s):
        print "\033[96mPC%02d"%s.n, "ns=%5.04f"%s.ns,
        s.s=s.ns
        s.ns = 0
        print "\033[0m"

class unit():
    def __init__(s, t, oc, st, ics):
        us.append(s)
        s.id = us.index(s)
        s.t, s.oc, s.st, s.ics = t, oc, st, ics
        print "\033[92mIU%04d"%s.id,"t=%.4f"%t,"st=%.4f"%s.st, "oc=%03d"%oc.n,"ics:",
        for ic in ics: print "%03d"%ic.n,
        print "\033[0m"
    def p(s):
        sm = sum([c.s for c in s.ics])
        if sm > s.t:
            s.oc.ns+=s.st
            print "\033[93mPU%04d"%s.id,"sum_i-t=\033[92m%5.04f"%(sm-s.t),
        else: print "\033[93mPU%04d"%s.id,"sum_i-t=\033[91m%5.04f"%(sm-s.t),
        print "\033[0m"

for n in range(nchannels): c = channel(n)
for _ in range(nunits): u = unit(random(), choice(cs), random(), sample(cs,cpu))
def step():
    for u in us: u.p()
    for c in cs: c.p()

def flash(cn, s): [c for c in cs if c.n==cn][0].s = s
