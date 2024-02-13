import numpy as np
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg before importing pyplot
import matplotlib.pyplot as plt
from qiskit import *
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

def check_norm(prob_0, prob_1):
    '''
    Checks whether input probabilities corresponds to valid quantum state of not.
    
    Inputs:
        prob_0, prob_1 --> (int) Probabilities corresponding to |0> and |1>.
    
    Output:
        msg --> (string) Message indicating whether the input probabilities sum up to 1 or not.
    '''
    amp_0 = np.sqrt(prob_0)
    amp_1 = np.sqrt(prob_1)
    
    norm = Statevector([amp_0, amp_1]).is_valid()   # checking whether norm is equal to 1.
    
    return norm

def qt(prob_0, prob_1):
    '''
    Saves images of final circuit and qsphere of result.
    
    Inputs:
        prob_0, prob_1 --> (int) Probabilities corresponding to |0> and |1>.

    '''
    if check_norm(prob_0, prob_1) == False:
        return "Incorrect inputs! Probabilities do not sum upto 1! Enter valid probabilities!"

    else:
        ## Convert probabilities to Amplitudes
        amp_0 = np.sqrt(prob_0)
        amp_1 = np.sqrt(prob_1)

        state = Statevector([amp_0, amp_1])
        
        phi = QuantumRegister(1, 'phi')
        alice = QuantumRegister(1, 'alice')
        bob = QuantumRegister(1, 'bob')
        
        qc = QuantumCircuit(phi, alice, bob)
        
        # user state initialized
        qc.initialize(state, phi)
        qc.barrier()
        
        # entanglement between Alice's and Bob's qubits
        qc.h(alice)
        qc.cx(alice, bob)
        qc.barrier()
        
        # teleportation process
        qc.cx(phi, alice)
        qc.h(phi)
        qc.barrier()
        
        # operation on Bob's end
        qc.cx(alice, bob)
        qc.cz(phi, bob)
        qc.barrier()
        
        # to get state from circuit and save circuit image and qsphere image
        state_1 = Statevector(qc)
        
        circuit_image_path = 'H:\GitHub\Quantum-Teleportation-Protocol\static\circuit_image.png'
        qc.draw('mpl').savefig('circuit_image.png')
        
        qsphere_image_path = 'H:\GitHub\Quantum-Teleportation-Protocol\static\qsphere_image.png'
        plot_state_qsphere(state_1).savefig('qsphere_image.png')
        
        return circuit_image_path, qsphere_image_path 