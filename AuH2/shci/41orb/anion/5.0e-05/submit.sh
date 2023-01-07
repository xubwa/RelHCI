#!/bin/bash
#SBATCH -A ucb-summit-sha
#SBATCH --job-name auh2
#SBATCH --time=120:00:00
#SBATCH --mem=110G
#SBATCH --nodes=1
#SBATCH --exclusive
ml intel impi mkl boost
export I_MPI_FABRICS=shm:tcp
mpirun -np 24 ~/X4C/Dice/ZCDFCI shci.dat > shci.out
 rm core.*