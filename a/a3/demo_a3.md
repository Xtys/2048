**Demo 3** 

***Quantum* *Computing*** 

**Name**: Brandon Loh Ming Fong

**ID** : 47754764

---

Q1.

![image-20250527121604224](/home/brandon/.config/Typora/typora-user-images/image-20250527121604224.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(1, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
```

Explanation:

An important step in building qubits is to be able to convert between classical and quantum
states

![image-20250527115600610](/home/brandon/.config/Typora/typora-user-images/image-20250527115600610.png)

![image-20250527132530612](/home/brandon/.config/Typora/typora-user-images/image-20250527132530612.png)

creates superposition. 

This results in a 50% chance of measuring, Drac notation of '0' or '1',  which is key for quantum superposition.

why -1? 

Q2.

![image-20250527134250262](/home/brandon/.config/Typora/typora-user-images/image-20250527134250262.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.x(qreg_q[2])
```

Q3.

![image-20250527134340517](/home/brandon/.config/Typora/typora-user-images/image-20250527134340517.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.x(qreg_q[2])
circuit.h(qreg_q[1])
```

Q4.

![image-20250527134642264](/home/brandon/.config/Typora/typora-user-images/image-20250527134642264.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[1])
circuit.h(qreg_q[2])
circuit.h(qreg_q[0])
```

---

Q5. 

Reference: Modern Computation by S. S. Chandra pg. 65.

A Bell state is a maximally entangled state of two qubits.

![image-20250527135436272](/home/brandon/.config/Typora/typora-user-images/image-20250527135436272.png)

- This state cannot be written as a tensor product of two 1-qubit states

- There is no linear operator that can undo the operation.

- The two qubits will always share the same truth value.

  if we measure one of the states and obtain an outcome, it will also reveal the outcome
  of the other state, i.e. the outcome of one state is the same as the other

  Entangled 2-qubit systems: Bell states

  ![image-20250527135833579](/home/brandon/.config/Typora/typora-user-images/image-20250527135833579.png)

![image-20250527134858446](/home/brandon/.config/Typora/typora-user-images/image-20250527134858446.png)

![image-20250527120226641](/home/brandon/.config/Typora/typora-user-images/image-20250527120226641.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[0])
circuit.x(qreg_q[0])
circuit.z(qreg_q[1])
```

>  building quantum algorithms

---

Q6.

![image-20250527140043372](/home/brandon/.config/Typora/typora-user-images/image-20250527140043372.png)

--Why does this lead to better ‘randomness’ than a normal/classical coin toss? 

In QM, there are one of two consequences of making a measurement. The accepted con-
sequence until recently has been that the wavefunction collapses into one of the outcomes
that is possible according to the probability density. The collapse is the outright destruction
of the quantum state to produce this outcome. This leads to a famous paradox called the
Schrödinger’s cat.

Becasue it consider all state of outcome. so 0 and 1.  Instead of just landing on a random 0 (tails) or 1 (heads), the qubit enters a state called **superposition**. eg . ***Schrödinger’s cat paradox*** 

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(1, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
```



---

--How could you extend this to be a random number generator?

As observered, 4 outcome are shown on the image,eg 00 = 0 , 01 = 1, 10 = 2 , 11= 3 , so number generator. 

and why this would be extended as a number generator?  

A qubit would results in '0' or '1', having that idea you can actually put a large number of output of qubit together this would becomes a string of binaries which could be a number generator.

![image-20250527140135705](/home/brandon/.config/Typora/typora-user-images/image-20250527140135705.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[2])
circuit.h(qreg_q[3])
circuit.h(qreg_q[4])
circuit.measure(qreg_q[0], creg_c[0])
```

---

Q7.

Implement a solution to the Deutsch oracle problem 

![image-20250527141241847](/home/brandon/.config/Typora/typora-user-images/image-20250527141241847.png)

what is Deutsch problem? black box , operations unknown

variable and constant operators. 

The variable type of operator should interact with the output and input bits to
produce a different tensor product state 

**Set |0⟩ (left)**

![image-20250527120917772](/home/brandon/.config/Typora/typora-user-images/image-20250527120917772.png)

![image-20250527140405088](/home/brandon/.config/Typora/typora-user-images/image-20250527140405088.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
```

Essentially, the Set |0⟩ and Set |1⟩ operations pass through without any changes as our previous circuit constructions have shown

probability density of the result becomes 0^2 + (−1)^2

---

**Set |1⟩ (right)**

![image-20250527120939743](/home/brandon/.config/Typora/typora-user-images/image-20250527120939743.png)

![image-20250527140452245](/home/brandon/.config/Typora/typora-user-images/image-20250527140452245.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.x(qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
```

Hence result is always |11⟩.

---

**Identity**

![image-20250527121002697](/home/brandon/.config/Typora/typora-user-images/image-20250527121002697.png)

![image-20250527140545319](/home/brandon/.config/Typora/typora-user-images/image-20250527140545319.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
```

---


 **Negation**

![image-20250527121022547](/home/brandon/.config/Typora/typora-user-images/image-20250527121022547.png)

![image-20250527140841485](/home/brandon/.config/Typora/typora-user-images/image-20250527140841485.png)

```
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.cx(qreg_q[1], qreg_q[0])
circuit.h(qreg_q[1])
circuit.x(qreg_q[0])
circuit.h(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
```

---

Recap Content: 

What is QM? wave function 

Dirac's notation on classical bits

for 1 bit : 4 operators , reversible = identity / negation

for 2 bits on wards, possible states |00⟩, |10⟩, |01⟩ , |11⟩

Tensor product : |00⟩ = |0⟩ ⟨0| , also means |ab⟩ = |a⟩ ⟨b| =  a ⊗ b

CNOT gate is a reversible XOR gate

A qubit is a is a bit that is in a superposition of two states

A qubit still collapses into a binary bit, but
like all quantum systems, the final state has a probabilistic outcome given by its probability
density.

it has probability density of |μ|2 + |ν|2

Operators of Quantum Circuits: Hadamard Operator

![image-20250527133117719](/home/brandon/.config/Typora/typora-user-images/image-20250527133117719.png)

Hadamard operator is unitary and self-adjoint, we can convert a qubit
superposition, like the ones presented in equations (6.48) and (6.49), back into a classical
state simply by applying the operator H again.

Unitary matrices, negative value

Quantum circuit: qubit with a ‘wire’ and the operators as boxes or symbols on these wires.

to flip 0 to 1 use NOT Operator X

identity operation, we require the use of the CNOT 

variable operator: 

![image-20250527141945149](/home/brandon/.config/Typora/typora-user-images/image-20250527141945149.png)

 
