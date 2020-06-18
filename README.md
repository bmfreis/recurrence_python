# recurrence_python

This scientific software written in Python 3 computes Recurrence Plot (RP), Cross Recurrence Plot (CRP), Joint Recurrence Plot (JRP) and Recurrence Quantification Analysis.

## Cross Recurrence Plot (CRP)

*Cross Recurrence Plot (CRP)* is a graph which shows all those times at which a state in one dynamical system occurs simultaneously in a second dynamical system. With other words, the CRP reveals all the times when the phase space trajectory of the first system visits roughly the same area in the phase space where the phase space trajectory of the second system is. [3]

cross_recurrence.py computes:
  * Distance matrix (Manhattan, Euclidean or Supremum distance)
  * Cross recurrence matrix


## Joint Recurrence Plot (JRP)

*Joint Recurrence Plot (JRP)* is a graph which shows all those times at which a recurrence in one dynamical system occurs simultaneously with a recurrence in a second dynamical system. [3]

joint_recurrence.py computes:
  * Distance matrix (Manhattan, Euclidean or Supremum distance)
  * Joint recurrence matrix


## Recurrence Plot (RP)

*Recurrence Plot (RP) * is a visualisation of a square matrix, in which the matrix elements correspond to those times at which a state of a dynamical system recurs. The RP reveals all the times when the phase space trajectory of the dynamical system visits roughly the same area in the phase space. [1,3]

recurrence.py computes:
  * Distance matrix (Manhattan, Euclidean or Supremum distance)
  * Recurrence matrix


## Recurrence Quantification Analysis (RQA)

*Recurrence Quantification Analysis (RQA)* is a method which quantifies the number and duration of recurrences of a dynamical system presented by its state space trajectory. [2,3,4,5]

recurrence_analysis.py computes:
* Frequency distribution of diagonal lines P(l)
* Frequency distribution of vertical lines P(v)
* Frequency distribution of white vertical lines P(w) 
* Recurrence rate (RR)
* Determinism (DET)
* Average diagonal line length (L)
* Longest diagonal line length (L_max)
* Divergence (DIV)
* Entropy diagonal lines (L_entr)
* Laminarity (LAM)
* Average diagonal line length (V) or Trapping time (TT)
* Longest vertical line length (V_max)
* Entropy vertical lines (V_entr)
* Average white vertical line length (W)
* Longest white vertical line length (W_max)
* Entropy white vertical lines (W_entr)
* Ratio determinism / recurrence rate (DET/RR)
* Ratio laminarity / determinism (LAM/DET)


## References

[1](https://www.doi.org/10.1209/0295-5075/4/9/004) J.-P. Eckmann, S. Oliffson Kamphorst, D. Ruelle: Recurrence Plots of Dynamical Systems, Europhysics Letters, 4(9), 973–977p. (1987)

[2](https://www.doi.org/10.1103/PhysRevE.66.026702) N. Marwan, N. Wessel, U. Meyerfeldt, A. Schirdewan, J. Kurths: Recurrence Plot Based Measures of Complexity and its Application to Heart Rate Variability Data, Physical Review E, 66(2), 026702p. (2002)

[3](http://www.recurrence-plot.tk) N. Marwan, M. C. Romano, M. Thiel, J. Kurths: Recurrence Plots for the Analysis of Complex Systems, Physics Reports, 438(5-6), 237-329p. (2007)

[4](https://www.doi.org/10.1152/jappl.1994.76.2.965) C. L. Webber, Jr., J. P. Zbilut: Dynamical assessment of physiological systems and states using recurrence plot strategies, Journal of Applied Physiology, 76(2), 965-973p. (1994)

[5](https://www.doi.org/10.1016/0375-9601(92)90426-M) J. P. Zbilut, C. L. Webber, Jr.: Embeddings and delays as derived from quantification of recurrence plots, Physics Letters A, 171(3–4), 199–203p. (1992)
