# Discrete Random Walks
In the repo, I cover my analysis of a few different computational results of discrete random walks in 2D and 3D.

# 2D Discrete Random Walk
For a 2D Discrete random walk, I kept track of a variable for the x and y axes. Using numpy random, a direction was chosen from +x,-x,+y,-y. Meaning the path was allowed to overlap. The goal was to find the diffusion constant D using the following equation <x<sup>2</sup>> = 4Dt. 
<ul>
  <li><x<sup>2</sup>> is the mean-square displacement and x is the displacement from starting point.</li>
  <li>qi - numerical constant which depends on dimensionality: qi = 2, 4, or 6, for 1, 2, or 3 dimensional diffusion.</li>
  <li>D - diffusion coefficient (usual units are cm<sup>2</sup> s<sup>-1</sup> but in this case, the length unit is arbitrary).<li>
  <li>t - time</li>
</ul>
Below is an example of one random walk with 1000 steps.
![](images/2D_RW2.gif)