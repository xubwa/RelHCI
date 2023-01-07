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
import x2camf_hf, fcidump_rel
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

mf_x2c = x2camf_hf.X2CAMF_RHF(mol, with_gaunt=True, with_breit=False, prog='sph_atm')
#mf_x2c.nopen = 6
#mf_x2c.nact = 3
e_x2c = mf_x2c.kernel()
fcidump_rel.from_x2c(mf_x2c, 34, 62, filename='FCIDUMP_62')

