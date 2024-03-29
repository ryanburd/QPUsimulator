# This tutorial shows how to use the Quantum Fourier Transform (QFT) algorithm with the QPU simulator.

################################################################################

# Import the QPU simulator which creates the quantum circuit and contains all gate operations.
# Import QFT from Algorithms if you want to access the algorithm directly, rather than through QPUsimulator. Computationally, using the algorithm through Simulator.py or Algorithms.py is the same. When displaying the circuit, Simulator.py simplifies the diagram to show a general "QFT" block over all the qubits involved to represent the algorithm; Algorithms.py shows all the individual gates completed in the algorithm.
import Simulator as QPU
from Algorithms import QFT

# Create a quantum circuit with a chosen number of qubits. The same number of classica bits will be created for qubit measurement output. The output of each qubit is stored in its similarly indexed classical bit.
numQubits = 3
circuit = QPU.Circuit(numQubits)

# Initialize the circuit to a state of your choosing. For example, the state |5> = |101>
circuit.X([0, 2])

# To apply the algorithm to your circuit, you can apply it just as you would a qubit gate. You may provide the number of qubits to perform the QFT on using numQubits. Note that the qubits involved must be sequential and ordered from least significant (lowest index) to most significant (highest index). To perform QFT on all qubits within the circuit, you may leave this argument as the default by passing nothing, and the function will get the number of qubits in the circuit.
circuit.QFT()

# Measure each input qubit. 
circuit.measure(range(numQubits))

# Display the quantum circuit.
circuit.display_circuit()

# Choose the number of shots for the circuit. Run the circuit 'shots' times and obtain the results as a list. Set hist=True to create a histogram of the results.
shots = 1024
results = circuit.run(shots, hist=True)

# If you would like to see all the gates performed by the algorithm, apply the QFT directly through Algorithms.py. Note: the function QFT was imported from Algorithms.py above, so we can use this function directly now.
# Computatinally, this method and the method above are exactly the same.
numQubits = 3
circuit = QPU.Circuit(numQubits)

circuit.X([0, 2])

QFT(circuit)

for qubit in range(numQubits):
    circuit.measure(qubit)

circuit.display_circuit()

shots = 1024
results = circuit.run(shots, hist=True)