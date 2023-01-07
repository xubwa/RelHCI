import numpy as np

pt_ene = np.loadtxt("pt.dat")
var_ene = np.loadtxt("var.dat")

e2_ene = pt_ene - var_ene

nroots = pt_ene.shape[1] - 1

with open("extrapolate.dat", "w") as f:
    for iroot in range(nroots):
        pt = pt_ene[:,iroot+1]
        e2 = e2_ene[:,iroot+1]
        fitted_ene = np.polyfit(e2, pt, deg=1)[-1]
        error_est = (fitted_ene - pt[-1]) / 5.
        f.write(f'Root {iroot}: extrapolated energy is {fitted_ene:16.8f} Hartree, estimated error is {error_est:8.4e} Hartree, {error_est*27.2114:6.4g} eV\n')

