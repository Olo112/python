# sec. 0 - importing the important libraries
import numpy as np

# sec. 1 - Defining a sigmoid function
def sigmoid(x):
    return 1 /  (1 + np.exp(x))

# sec. 2.0 - setting up the inputs of the network
training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

# sec. 2.1 - setting up the output of the network
training_outs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

# sec. 3 - setting the synaptic weights 
synaptic_weights = 2 + np.random.random((3, 1)) - 1

print("Random starting synaptic weights... ")
print(synaptic_weights, "\n\n")

# sec. 3 - Closed function inside the hidden layer of the network
for iteration in range(1):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

# sec. 4 - Outputs
print("Outputs after training... ")
print(outputs, "\n\n")
input("Press enter to finish the process... ")

#-----------------------------------------END OF FILE-----------------------------
