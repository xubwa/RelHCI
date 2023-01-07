def write_dice_input(eps_1, eps_2_large, fcidump='FCIDUMP', filename='shci.dat', error=5e-6, eps_2=1e-10):
    with open(filename, 'w+') as f:
        f.write(
'''nocc 14
0 1 2 3 4 5 6 7 8 9 10 11 12 13
end
orbitals {fcidump:}
nroots 1
schedule
0 1000
1 {eps_1}
end
davidsonTol 1e-7
davidsonTolLoose 1e-4
dE 1e-8
maxiter 16
targetError {error}
sampleN 150 
epsilon2Large {eps_2_large}
epsilon2 {eps_2}
noio
readText

'''.format(fcidump=fcidump, eps_1=eps_1, error=error, eps_2_large=eps_2_large, eps_2=eps_2))

def write_sbatch(modules, command, filename='submit.sh', node=1, time=48):
    with open(filename, 'w') as f:
        f.write(
'''#!/bin/bash
#SBATCH -A ucb-summit-sha
#SBATCH --job-name auh2
#SBATCH --time={time:}:00:00
#SBATCH --mem=110G
#SBATCH --nodes={node:}
#SBATCH --exclusive
'''.format(time=time, node=node))
        f.write(modules)
        f.write(command)
        f.write('\n rm core.*')
import os
eps_set=[[2e-4,1e-6],[1e-4,1e-6],[8e-5,1e-6],[5e-5,2e-6],[2e-5,2e-6],[1.e-5,2e-6]]
node_num = [1,1,1,1,4,6]
#eps_set = [[2e-4,2e-6],[1.5e-4,2e-6]]
#node_num = [4,8]
#eps_set=[[1.5e-4,5e-6]]
#node_num=[4]
for eps, node in zip(eps_set, node_num):
    eps1 = eps[0]
    eps2_large = eps[1]
    eps_str = '{:.1e}'.format(eps1)
    if not os.access(eps_str, os.F_OK):
        os.mkdir(eps_str)
    os.chdir(eps_str)
    write_dice_input(eps[0], eps[1], fcidump='../FCIDUMP')
    module='''ml intel impi mkl boost
export I_MPI_FABRICS=shm:tcp\n'''
    command = 'mpirun -np {ncore:} ~/X4C/Dice/ZCDFCI shci.dat > shci.out'.format(ncore=node*24)
    write_sbatch(module, command, node=node, time=120)
    os.system('sbatch submit.sh')
    os.chdir('..')
