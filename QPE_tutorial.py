# This tutorial shows how to use the quantum phase estimation (QPE) algorithm with the QPU simulator. This algorithm estimates the value theta within the eigenvalue problem U|psi> = e^(2pi*i*theta)|psi>.

################################################################################

# Import the QPU simulator which creates the quantum circuit and contains all gate operations.
# Import QPE from Algorithms if you want to access the algorithm directly, rather than through QPUsimulator. Computationally, using the algorithm through Simulator.py or Algorithms.py is the same. When displaying the circuit, Simulator.py simplifies the diagram to show a general "QPE" block over all the qubits involved to represent the algorithm; Algorithms.py shows all the individual gates completed in the algorithm.
# Import numpy for using np.pi.
import Simulator as QPU
from Algorithms import QPE
import numpy as np

# Create a quantum circuit with a chosen number of precision qubits. 1 qubit is automatically added for the the psi vector qubit, where psi is the eigenvector of the phase operation. The same number of classica bits will be created for qubit measurement output. The output of each qubit is stored in its similarly indexed classical bit.
numPrecisionQubits = 4
circuit = QPU.Circuit(numPrecisionQubits+1)

# Apply the QPE algorithm with a chosen value of lambd (defined by theta) for the controlled-P gate.
theta = 1/3
lambd = 2*np.pi*theta
circuit.QPE(lambd)

# Measure each precision qubit.
circuit.measure(range(numPrecisionQubits))

# Display the quantum circuit.
circuit.display_circuit()

# Choose the number of shots for the circuit. Run the circuit 'shots' times and obtain the results as a list. Set hist=True to create a histogram of the results.
shots = 1024
results = circuit.run(shots, hist=True)

# In this tutorial for using QPE, theta is obviously already known since we provided it when defining lambd. In more useful applications of QPE, theta is not known intially.
#
# To estimate theta from our results, we can use the two most probable measurement results. First, convert the binary number encoded by the precision qubits' measurement results into decimal. Divide the decimal by 2^n, where 'n' is the number of precision qubits used in the circuit, to get an estimate of theta. The actual value of theta is bound by the estimates for the two most probable results. We can see that increasing the number of precision qubits reduces the range between these two bounds, improving the accuracy of the theta estimation.
#
# Running this tutorial, you should obtain |00101> and |00110> are the first and second most probable results, respectively. The left most bit is the classical bit that would store the measurement result of the |psi> qubit. Since we have not measured it, it remains in the 0 state. Since we only care about the measurement results of the precision qubits, we can ignore this left most bit value. In decimal, 101 is 5 and 110 is 6. The theta bounds are thus 5/2^4 = 0.3125 and 6/2^4 = 0.375, which differ from the actual value of theta = 1/3 by 6% and 13%, respectively. Notice how the most probable result from our circuit, |00101>, has the lowest error as an estimate of the actual theta value, which makes sense.

lowerBound_binary = '0101'
upperBound_binary = '0110'

lowerBound_decimal = int(lowerBound_binary, base=2)
upperBound_decimal = int(upperBound_binary, base=2)

lowerBound_theta = lowerBound_decimal / 2**numPrecisionQubits
upperBound_theta = upperBound_decimal / 2**numPrecisionQubits

lowerBound_error = abs(theta-lowerBound_theta) / theta * 100
upperBound_error = abs(theta-upperBound_theta) / theta * 100

print('Theta lower bound = %.3f (%.1f %% error)'%(lowerBound_theta, lowerBound_error))
print('Theta upper bound = %.3f (%.1f %% error)'%(upperBound_theta, upperBound_error))

# If you would like to see all the gates performed by the algorithm, apply the QPE directly through Algorithms.py. Note: the function QPE was imported from Algorithms.py above, so we can use this function directly now.
# Computatinally, this method and the method above are exactly the same.
numPrecisionQubits = 4
circuit = QPU.Circuit(numPrecisionQubits+1)

theta = 1/3
lambd = 2*np.pi*theta
QPE(circuit, lambd)

for qubit in range(numPrecisionQubits):
    circuit.measure(qubit)

circuit.display_circuit()

shots = 1024
results = circuit.run(shots, hist=True)