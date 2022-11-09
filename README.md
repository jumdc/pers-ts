# pers-ts

This repository follows the ideas introduced by PhD Jose Perea in [Topological Time Series Analysis](https://arxiv.org/abs/1812.05143).

## Dynamic systems and Taken's embedding

**Definition of dynamical system**

- Intuitively, a dynamical system is composed of 
    - a set of states, M
    - rules $\Phi = \{\Phi_p, p \in M\}$ describing how each state $p \in M$ changes over time


- Formely, a global time dynamical system is a pair $(M, \Phi)$ where $M$ is a topological space and $\Phi : \mathbb{R} \times M \rightarrow M$ is a continous map

For most cases, we don't have neither knowledge about $M$ nor $\Phi$. 
However, it is possible to define an *observation function*. 

**Definition of an observation function**

Given two continuous maps, $\Phi : \phi : M \rightarrow{} M$ and $F : M \rightarrow{} \mathbb{R}$, 
we can define :
$\phi_p : \mathbb{R} \rightarrow{} \mathbb{R}, t \rightarrow{}  F\circ\Phi$ the observation function. 

Taken's embedding theorm aims to provide a theorical background to reconstructed the phase space $M$ from $\phi$.

**Taken's theorem** 

Let's define an observation function : 
    given a continous map $\phi : M \rightarrow{} \mathbb{R} $
