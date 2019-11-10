# Efficient-Ready-Queue-for-EDF-Sheduler

A ready queue of EDF scheduler is generally implemented as
a priority queue, for example, using a binary min-heap data structure in which
(insertion/deletion) operation cannot be done in constant time. This report re-iterates a new
design of ready queue for EDF scheduler: a simple data structure for the ready queue
and efficient operations to insert and remove task control blocks (TCBs) to and from the
ready queue are shown. Insertion of a TCB of a newly released job (that cannot pre-empt the
currently-executing job) is done in non-constant time. However, insertion of a TCB of a pre-
empted job or the removal of the TCB of job having the highest EDF priority
from the ready queue can be done in constant time. The implementation of the EDF algorithm
is then enhanced with the adoption of a multi-processing system. Simulation using randomly
generated task sets shows that the overhead of managing jobs in our proposed ready queue
for EDF scheduler is significantly lower than that of other approaches. It is believed that the
theoretically optimal EDF algorithm implemented based on the proposed ready-queue data
structure will make EDF popular in industry.
