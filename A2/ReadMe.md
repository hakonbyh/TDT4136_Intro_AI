# Acknowledgement
A lot of this code is influenced heavily by patrikkj on GitHub.

# Requirements for running code:
Python 3.6.4 64-bit
liberaries: numpy, pandas, pillow

# Architecture:

Class Node
Needs to denote one state with all nessecary info.

Class Map
Contains the problem and the end state.

Class Min_heap
Should keep a min heap of the nodes based on expected cost

Class A_star
Implements the a* algorithm with a given heap object and nodeobjects.
