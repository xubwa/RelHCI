import zquatev
import time
from functools import reduce
import numpy
import scipy.linalg
from pyscf import lib
from pyscf import gto
from pyscf.lib import logger
from pyscf.scf import hf
from pyscf.scf import _vhf
from pyscf.scf import chkfile
from pyscf.data import nist
from pyscf import __config__
from pyscf import scf
from pyscf import lib
from pyscf import x2c
from zccsd import zccsd
import x2camf, fcidump_rel
import copy
from pyscf import lib
lib.num_threads(28)
numpy.set_printoptions(suppress=True, linewidth=200)
c = nist.LIGHT_SPEED
mol = gto.M(atom='''
Au 0 0 0
H 0.0 0.0 1.647
H 0.0 0.0 -1.647
''', 
basis='dyallv3z', 
charge = -1, verbose=4)
#mf = scf.DHF(mol)
#mf.nopen = 2
#mf.nact = 1
#e_dhf = mf.kernel()

mf_x2c = x2camf.X2CAMF_RHF(mol, with_gaunt=True, with_breit=False, prog='sph_atm')
#mf_x2c.nopen = 6
#mf_x2c.nact = 3
e_x2c = mf_x2c.kernel()
core = numpy.arange(68)
virt = numpy.arange(68+124, mol.nao_2c())
mycc = zccsd.ZCCSD(mf_x2c, frozen=numpy.hstack((core, virt)))
mycc.kernel()
e_56 = mycc.ipccsd(nroots=12)
exit()
virt = numpy.arange(68+82, mol.nao_2c())
mycc = zccsd.ZCCSD(mf_x2c, frozen=numpy.hstack((core, virt)))
mycc.kernel()
e_56 = mycc.ipccsd(nroots=12)
nvirt = 0
for ene in mf_x2c.mo_energy:
    if ene < 10.0:
        nvirt += 1 
virt = numpy.arange(nvirt,mol.nao_2c())
for mo_occ, mo_ene in zip(mf_x2c.mo_occ, mf_x2c.mo_energy):
    print(mo_occ, mo_ene)
mycc = zccsd.ZCCSD(mf_x2c, frozen=numpy.hstack((core,virt)))
mycc.kernel()
e_full, v = mycc.ipccsd(nroots=12)
print(e_full)
print(e_56)
exit()
for mo_occ, mo_ene in zip(mf_x2c.mo_occ, mf_x2c.mo_energy):
    print(mo_occ, mo_ene)
fcidump_rel.from_x2c(mf_x2c, 34, 56, filename='FCIDUMP')

exit(0)
#fcidump_rel.from_dhf(mf, 1, 4, filename='FCIDUMP')
import os
os.system('~/X4C/Dice/ZDice2 input.dat')
