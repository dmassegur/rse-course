import numpy as np

def energy(density, coeff=1.0):
    """Energy associated with the diffusion model

    Parameters
    ----------

    density: array of positive integers
        Number of particles at each position i in the array
    coeff: float
        Diffusion coefficient.
    """
        
    a = np.zeros((0,0))
    print(density)
    nrg = density * (density - 1)
    nrg = sum(nrg)
    
    return nrg
