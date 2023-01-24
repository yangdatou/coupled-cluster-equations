
from numpy import einsum

def gccsd_eom_ea_h1e(h1e, h2e, t1e, t2e, r1e, r2e):
    res = 0.0
    res +=     1.000000 * einsum('ab,b->a'           , h1e.vv, r1e, optimize = False)
    res +=     1.000000 * einsum('ib,abi->a'         , h1e.ov, r2e, optimize = False)
    res +=     0.500000 * einsum('iabc,cbi->a'       , h2e.ovvv, r2e, optimize = False)
    res +=    -1.000000 * einsum('ib,ai,b->a'        , h1e.ov, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('iabc,ci,b->a'      , h2e.ovvv, t1e, r1e, optimize = True)
    res +=     0.500000 * einsum('ijbc,ai,cbj->a'    , h2e.oovv, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('ijbc,ci,abj->a'    , h2e.oovv, t1e, r2e, optimize = True)
    res +=     0.500000 * einsum('ijbc,acji,b->a'    , h2e.oovv, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('ijbc,ai,cj,b->a'   , h2e.oovv, t1e, t1e, r1e, optimize = True)
    return res



from numpy import einsum

def gccsd_eom_ea_h2e(h1e, h2e, t1e, t2e, r1e, r2e):
    res = 0.0
    res +=    -1.000000 * einsum('ai,b->abi'         , h1e.vo, r1e, optimize = False)
    res +=     1.000000 * einsum('bi,a->abi'         , h1e.vo, r1e, optimize = False)
    res +=     1.000000 * einsum('ji,baj->abi'       , h1e.oo, r2e, optimize = False)
    res +=    -1.000000 * einsum('ac,bci->abi'       , h1e.vv, r2e, optimize = False)
    res +=     1.000000 * einsum('bc,aci->abi'       , h1e.vv, r2e, optimize = False)
    res +=     1.000000 * einsum('baic,c->abi'       , h2e.vvov, r1e, optimize = False)
    res +=     1.000000 * einsum('jaic,bcj->abi'     , h2e.ovov, r2e, optimize = False)
    res +=    -1.000000 * einsum('jbic,acj->abi'     , h2e.ovov, r2e, optimize = False)
    res +=     0.500000 * einsum('bacd,dci->abi'     , h2e.vvvv, r2e, optimize = False)
    res +=     1.000000 * einsum('ji,aj,b->abi'      , h1e.oo, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('ji,bj,a->abi'      , h1e.oo, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('ac,ci,b->abi'      , h1e.vv, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('bc,ci,a->abi'      , h1e.vv, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jc,aj,bci->abi'    , h1e.ov, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jc,bj,aci->abi'    , h1e.ov, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jc,ci,baj->abi'    , h1e.ov, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jc,acji,b->abi'    , h1e.ov, t2e, r1e, optimize = True)
    res +=     1.000000 * einsum('jc,baji,c->abi'    , h1e.ov, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jc,bcji,a->abi'    , h1e.ov, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jaic,bj,c->abi'    , h2e.ovov, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jaic,cj,b->abi'    , h2e.ovov, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jbic,aj,c->abi'    , h2e.ovov, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jbic,cj,a->abi'    , h2e.ovov, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('bacd,di,c->abi'    , h2e.vvvv, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jkic,aj,bck->abi'  , h2e.ooov, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jkic,bj,ack->abi'  , h2e.ooov, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jkic,cj,bak->abi'  , h2e.ooov, t1e, r2e, optimize = True)
    res +=    -0.500000 * einsum('jkic,ackj,b->abi'  , h2e.ooov, t2e, r1e, optimize = True)
    res +=    -0.500000 * einsum('jkic,bakj,c->abi'  , h2e.ooov, t2e, r1e, optimize = True)
    res +=     0.500000 * einsum('jkic,bckj,a->abi'  , h2e.ooov, t2e, r1e, optimize = True)
    res +=    -0.500000 * einsum('jacd,bj,dci->abi'  , h2e.ovvv, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jacd,di,bcj->abi'  , h2e.ovvv, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jacd,dj,bci->abi'  , h2e.ovvv, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jacd,bdji,c->abi'  , h2e.ovvv, t2e, r1e, optimize = True)
    res +=     0.500000 * einsum('jacd,dcji,b->abi'  , h2e.ovvv, t2e, r1e, optimize = True)
    res +=     0.500000 * einsum('jbcd,aj,dci->abi'  , h2e.ovvv, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jbcd,di,acj->abi'  , h2e.ovvv, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jbcd,dj,aci->abi'  , h2e.ovvv, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jbcd,adji,c->abi'  , h2e.ovvv, t2e, r1e, optimize = True)
    res +=    -0.500000 * einsum('jbcd,dcji,a->abi'  , h2e.ovvv, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,adji,bck->abi', h2e.oovv, t2e, r2e, optimize = True)
    res +=    -0.500000 * einsum('jkcd,adkj,bci->abi', h2e.oovv, t2e, r2e, optimize = True)
    res +=    -0.500000 * einsum('jkcd,baji,dck->abi', h2e.oovv, t2e, r2e, optimize = True)
    res +=    -0.250000 * einsum('jkcd,bakj,dci->abi', h2e.oovv, t2e, r2e, optimize = True)
    res +=     1.000000 * einsum('jkcd,bdji,ack->abi', h2e.oovv, t2e, r2e, optimize = True)
    res +=     0.500000 * einsum('jkcd,bdkj,aci->abi', h2e.oovv, t2e, r2e, optimize = True)
    res +=    -0.500000 * einsum('jkcd,dcji,bak->abi', h2e.oovv, t2e, r2e, optimize = True)
    res +=     1.000000 * einsum('jc,ci,aj,b->abi'   , h1e.ov, t1e, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jc,ci,bj,a->abi'   , h1e.ov, t1e, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jkic,aj,ck,b->abi' , h2e.ooov, t1e, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jkic,bj,ak,c->abi' , h2e.ooov, t1e, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jkic,bj,ck,a->abi' , h2e.ooov, t1e, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jacd,di,bj,c->abi' , h2e.ovvv, t1e, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jacd,di,cj,b->abi' , h2e.ovvv, t1e, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jbcd,di,aj,c->abi' , h2e.ovvv, t1e, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jbcd,di,cj,a->abi' , h2e.ovvv, t1e, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jkcd,aj,dk,bci->abi', h2e.oovv, t1e, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jkcd,aj,bdki,c->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=     0.500000 * einsum('jkcd,aj,dcki,b->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=     0.500000 * einsum('jkcd,bj,ak,dci->abi', h2e.oovv, t1e, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,bj,dk,aci->abi', h2e.oovv, t1e, t1e, r2e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,bj,adki,c->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=    -0.500000 * einsum('jkcd,bj,dcki,a->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,di,aj,bck->abi', h2e.oovv, t1e, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jkcd,di,bj,ack->abi', h2e.oovv, t1e, t1e, r2e, optimize = True)
    res +=     1.000000 * einsum('jkcd,di,cj,bak->abi', h2e.oovv, t1e, t1e, r2e, optimize = True)
    res +=     0.500000 * einsum('jkcd,di,ackj,b->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=     0.500000 * einsum('jkcd,di,bakj,c->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=    -0.500000 * einsum('jkcd,di,bckj,a->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,dj,acki,b->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,dj,baki,c->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=     1.000000 * einsum('jkcd,dj,bcki,a->abi', h2e.oovv, t1e, t2e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,di,aj,ck,b->abi', h2e.oovv, t1e, t1e, t1e, r1e, optimize = True)
    res +=    -1.000000 * einsum('jkcd,di,bj,ak,c->abi', h2e.oovv, t1e, t1e, t1e, r1e, optimize = True)
    res +=     1.000000 * einsum('jkcd,di,bj,ck,a->abi', h2e.oovv, t1e, t1e, t1e, r1e, optimize = True)
    return res


