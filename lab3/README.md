# Lab 3: Policy Search

- lab did with [AleTola](https://github.com/AleTola)

## Task

Write agents able to play Nim, with an arbitrary number of rows and an upper bound  on the number of objects that can be removed in a turn (a.k.a., subtraction game).

The player taking the last object wins.

- Task3.1: An agent using fixed rules based on nim-sum (i.e., an expert system)

- Task3.2: An agent using evolved rules

# My approach

In my approach I have implemeneted 5 simple strategies using the data about the "state" of the board in each moment the startegy has to be used (_shortest row_, _longest row_, _active number of objescts_).

In these 5 startegies I have inserted a probability "p" that have to be tuned by the Evolution Algorithm in order to achieve the maximum fitness possible.

The fitness function calculate the "winrate" taking into account 4 matches versus 4 different strategies:

- _PURE RANDOM_ : we choose a random row and a random number of objects to remove from that row
- _DUMB_ : remove always only one object from the longest row
- _GOOD_ : remove all the objects from the longest row
- _OPTIMAL_ : the nim-sum

A mutation consists in increasing or decreasing (depending on the mutation rate m1) the probability associated to the strategy of the individual subjected to the mutation.

The Evolution Algortihm starts with a population of 15 individuals, 3 for each strategy, with probability asscoiated to each strategy equal to 0.5.
