import pyscf
from pyscf import gto,x2c
import x2camf, fcidump_rel
mol = gto.M(atom=[['Np',[0, 0, 0]],['O', [0, 0, 1.70]],['O',[0,0,-1.70]]], 
basis={'O':'unc-cc-pvtz','Np':'unc-ano'}, 
spin = 1, 
verbose=4, 
charge=2)
mf2 = x2camf.X2CAMF_RHF(mol,nopen=8, nact=1, with_gaunt=True,with_breit=True,prog="sph_atm")
mf2.chkfile='breit.chk'
mf2.max_cycle=200
mf2.scf()
for mo_occ, mo_ene in zip(mf2.mo_occ, mf2.mo_energy):
    print(mo_occ, mo_ene)
fcidump_rel.from_x2c(mf2, 47, 60, filename='FCIDUMP_60')
exit()
