#!/usr/bin/env python
# coding: utf-8

import sisl
import numpy as np

C60 = sisl.Geometry.read('C60.xyz')

# Calculate the nearest neighbour distance
dist = C60.distance(R=5)

C60.atoms.atom[0] = sisl.Atom(6, R=dist[0] + 0.01)

elec = sisl.Geometry([0] * 3, sisl.Atom(6, R=1.), [1, 1, 10]).tile(2, 0).tile(2, 1)
elec.set_nsc(a=3, b=1)
H_elec = sisl.Hamiltonian(elec)
H_elec.construct(([0.1, 1.1], [0., -1]))
H_elec.write('ELEC.nc')

elec_x = elec.tile(3, 0)

# Translate to origo
C60 = C60.translate(-C60.center(what='xyz'))
C60 = C60.translate([-C60.xyz[:, 0].min(), 0, 0])

# Do trickery to make sure the coordinates are consecutive along x
C60.set_lattice([C60.xyz[:, 0].max() + 1., 1., 1.])
device = elec_x.append(C60, 0).append(elec_x, 0)

H = sisl.Hamiltonian(device)
H.construct(([0.1, 1.1], [0., -1]))
# Correct the C_60 couplings to something different
idx_C60 = np.arange(len(elec_x), len(elec_x) + len(C60), dtype=np.int32)
for ia in idx_C60:
    idx = device.close(ia, R=[0.1, C60.maxR()])[1]
    # On-site is already 0, so don't bother doing anything there
    # Split idx into C60 couplings and chain couplings
    for i in idx:
        if i in idx_C60:
            H[ia, i] = -1.5
        else:
            # Coupling to chain
            # Since we are only looping atoms in C60
            # we have to also set the coupling into C60
            # (to assert Hermiticity)
            H[ia, i] = 0.1
            H[i, ia] = 0.1
H.write('DEVICE.nc')

open('projection.fdf', 'w').write("""
SystemLabel projection
TBT.HS DEVICE.nc

TBT.T.Eig 6
TBT.DOS.Gf true
TBT.DOS.A true

%block TBT.Elec.Left
  HS ELEC.nc
  semi-inf-direction -A1
  electrode-position 1
%endblock TBT.Elec.Left
%block TBT.Elec.Right
  HS ELEC.nc
  semi-inf-direction +A1
  electrode-position end -1
%endblock TBT.Elec.Right

TBT.Atoms.Device [13 -- 72]

%block TBT.Projs
  C60
%endblock

%block TBT.Proj.C60
  atom [13 -- 72]
  proj HOMO
    level -1
  end
  proj LUMO
    level [1, 2]
  end
%endblock

%block TBT.Projs.T
  from Left to
    Right.C60
  end
  from Left.C60 to
    Right.C60
    Right
  end
%endblock
""")

