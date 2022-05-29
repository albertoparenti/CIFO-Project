# CIFO - Final Project

Final project for the *Computational Intelligence for Optimization* class at NOVA IMS, in S12022.

## The problem

Our objective is to use genetic algorithms to solve the [route inspection problem](https://en.wikipedia.org/wiki/Route_inspection_problem), also known as the Chinese postman problem.

Given a graph of nodes and edges, the route inspection problem involves finding the shortest closed path that visits every edge. That is, starting from an origin node, we must traverse the graph and visit every edge at least once, finishing back at the origin.

Assumptions:

- We are dealing with an unidrected graph.
- We start at node A and must end back at A.

## Technicalities

You can recreate the conda environment used to delevop the project using the file in `env/conda_environment.txt`.

Use `route_inspection_problem.ipynb` to run the solution to the problem.

