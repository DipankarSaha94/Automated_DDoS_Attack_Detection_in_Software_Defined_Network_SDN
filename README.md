# Automated DDoS Attack Detection in Software Defined Network(SDN)

## Course: Advanced Computer Networks

### Overview:  
We implement a machine-learning based approach to detect Distributed Denial of Service (DDoS) attacks in the Software Defined Networking (SDN) paradigm. The network configuration has been customized using `mininet` and `pox` controller. Below topologies have been used for dataset creation.  
<img src="/Images/Topology1.JPG" alt="Topology 1" style="height: 200px; width:300px;"/> <img src="/Images/Topology2.JPG" alt="Topology 1" style="height: 200px; width:300px;"/> <img src="/Images/Topology3.JPG" alt="Topology 1" style="height: 200px; width:300px;"/>  

### Simulation of DDoS Attack using mininet
#### Mininet Installation:
- We have installed mininet on Ubuntu 20.04 VM.
- Get the source code of Mininet using: `git clone git://github.com/mininet/mininet`
- Go to the mininet folder: `cd mininet`
- Get all the versions: `git tag`
- Select the version you prefer: `git checkout -b mininet-2.3.0 2.3.0`
- Come out of the current folder and Install Mininet: 
    - `cd ..`
    - `mininet/util/install.sh -a` 

#### POX Controller Installation:
- Get the source code: `git clone http://github.com/noxrepo/pox`
- Go to the pox folder: `cd pox`
- Run the Controller: `sudo python3 pox.py forwarding.l3_learning openflow.of_01 --port=6666`
    - Default port is *6633*

#### Creating and Running our Topology Using `miniedit.py`:
- Run the command: `sudo python3 mininet/mininet/examples/miniedit.py`
- It will open a GUI window where we can create our own topology by *drag and drop* method and also configure all its components.
- Before running the topology, go to: ***Edit -> Preferences***. Select ***Start CLI*** and click ***OK***.
- Run the topology by clicking on *RUN* and go to the terminal window where we have run the *miniedit* program.
- The terminal has already started the **Mininet CLI**.
- Test your network by using *ping* and *pingall* commands.
- Open one of the host's terminal using **xterm**. Sample command: `xterm h1`
- Run the **hping3 flooding** program on the host terminal: `sudo python3 pox/ext/hping3_flood.py 10.0.0.31`
    - Here, *10.0.0.31* is the Host IP.
    - This program will flood the network with high volumes of random ICMP packets at regular intervals, hence creating a DDoS attack.

### Classification
We classify the traffic into benign (labelled as "0") and malicious (labelled as "1").  We have trained a total of 7 different classifier models, viz. Gaussian Naive Bayes (GNB), Logistic Regression (LR), Support Vector Classifier(SVC), Ensemble Classifier(GBC), Decision Tree (DT), Artificial Neural Network (ANN) and Deep Learning (LSTM) to identify the incoming traffic as Normal (benign) or Attack (malicious). Further details about the models and the analysis have been provided in the notebook.    

### Observations
The following table shows the observed results for all the classifiers:  

N: Normal   
A: Attack  

| Algo     |   Acc |   N Prec |   A Prec |   N Rec |   A Rec |   N F-score |   A F-score |   FPR |   FNR |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
| GNB      |  0.7  |     0.7  |     0.7  |    0.76 |    0.64 |        0.73 |        0.67 | 0.24  | 0.36  |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
| LR       |  0.84 |     0.84 |     0.84 |    0.86 |    0.82 |        0.85 |        0.83 | 0.14  | 0.18  |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
| SVC      |  0.98 |     0.98 |     0.97 |    0.98 |    0.98 |        0.98 |        0.97 | 0.023 | 0.024 |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
| Ensemble |  0.99 |     0.99 |     0.99 |    0.99 |    0.99 |        0.99 |        0.99 | 0.001 | 0.001 |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
| DT       |  1    |     1    |     1    |    1    |    1    |        1    |        1    | 0     | 0     |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
| ANN      |  0.99 |     0.99 |     0.99 |    0.99 |    0.99 |        0.99 |        0.99 | 0.001 | 0.001 |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
| DL       |  0.99 |     0.99 |     0.99 |    0.99 |    0.99 |        0.99 |        0.99 | 0.001 | 0.001 |
|----------|-------|----------|----------|---------|---------|-------------|-------------|-------|-------|
  


