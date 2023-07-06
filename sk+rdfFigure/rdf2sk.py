#!/usr/bin/env python3
import numpy as np
import argparse

##############################
parser = argparse.ArgumentParser()
parser.add_argument(
            "--file",
            required = True,
            type = str,
            help = 'file with RDF with distance in column 0 and <RDF> in column 1',
            )
parser.add_argument(
            "--density",
            required = True,
            type = float,
            help = 'density of particles',
            )
parser.add_argument(
            "--minq",
            default = 1,
            type = float,
            help = 'the smallest k vector',
            )
parser.add_argument(
            "--maxq",
            default = 8.0,
            type = float,
            help = 'the largest k vector',
            )
parser.add_argument(
            "--Nqs",
            default = 25,
            type = int,
            help = 'number of k vectors within the boundaries',
            )
args = parser.parse_args()

##############################
data = np.loadtxt(args.file)
rs, dr = data[:,0], (data[1,0] - data[0,0])
RDFs = data[:,1] - np.ones_like(rs)

qs = np.linspace(args.minq, args.maxq, num = args.Nqs)
Sqs = np.zeros_like(qs)

for qind, q in enumerate(qs):
  s = 0
  for rind, r in enumerate(rs):
    s += dr * r * np.sin(q * r) * RDFs[rind]
  Sqs[qind] = 1 + 4 * np.pi * args.density * s / q

##############################
with open(args.file + '.SQ.dat', 'w') as out_f:
  out_f.write('q | S(q)\n')
  for i in range(args.Nqs):
    out_f.write('{:} {:}\n'.format(qs[i], Sqs[i]))
out_f.close()

exit()
