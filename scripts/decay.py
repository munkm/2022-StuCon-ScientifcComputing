import numpy as np
import matplotlib.pyplot as plot

def plotdecay(initial_amount, half_life, time):
    """
    Plots the decay of an isotope, if given the half-life, decay, and initial
    number of atoms

    Parameters:
    initial_amount: initial number of atoms
    half_life: half-life of isotope, in seconds
    time: time isotope is decaying, in seconds

    Returns:
    none
    """

    time_steps = np.linspace(0,time, time)

    isotope_atom = initial_amount*np.exp(-half_life*time_steps)

    plot.plot(time_steps,isotope_atom)

    return
