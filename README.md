# Bongo Written Test
This repository contains the solution for three problems for BongoBD written test. The codes are commented for explaining the appoach. 

## Usage
First 3 folders contains the codes for three problem. `test` folder contains the unit tests for the three problems.   
The test can be run using the following command from the terminal which runs unit tests for all three solutions. 
```
python -m unittest discover -s tests
```

## Space and Time Complexity
### Q1: Printing Depth of keys:
**Time**: O(N), where N is the total number of key present in the nested dictionary.  
We are visiting those key only once.    
**Space**: O(N^2), here we are creating new dictionary each time.  
In worst case if the input is nested one after another ex:{'a':{'b':'c':{'d':1}}} then we n,n-1,n-2 dictionary are created, which equals to n*(n-1)/2, means O(N^2)
  
### Q2: Printing Depth of keys and object members  
**Time:** O(N), where N is the total number of key present in the nested dictionary and total member variables present.
We are visiting those key only once.    

**Space:** O(N^2), here we are creating new dictionary each time.  
In worst case if the input is nested one after another ex:{'a':{'b':'c':{'d':1}}} then we n,n-1,n-2 dictionary are created, which equals to n*(n-1)/2, means O(N^2)

### Q3: Least Common Ancestor  
**Time:** O(N), where N is the total number of nodes present in the tree. We are traversing the tree two times.  
2*N in total so the complexity is linear and checking if a item is present in the set is constant time.  

**Space:** O(N), where N is the total number of nodes. We are storing the node values in a set to check for presence in the next traversal.
