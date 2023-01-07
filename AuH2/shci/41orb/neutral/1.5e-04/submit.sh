#!/bin/bash
#SBATCH -A ucb-summit-sha
#SBATCH --job-name auh2
#SBATCH --time=72:00:00
#SBATCH --mem=100G
#SBATCH --nodes=6
#SBATCH --exclusive
ml intel impi mkl boost
mpirun -np 144 ~/X4C/Dice/ZCDFCI shci.dat > shci.out
rm core.*