# COP4533_PA1

# README

## Names and UFID
Esmil Canet, 42022968  
Amanda Tantalean, 34278244  

## Instructions to Run the Code

### Step 1: Navigate to the `src/` directory
`cd src/`

### Step 2: Run the matcher
`python main.py match [input_file]`

- `[input_file]` must be located in the `data/` directory  
- Example:
`python main.py match input.txt`

### Step 3: Run the verifier
`python main.py verify [preferences_file] [output_to_validate]`

- Both files must be located in the `data/` directory  
- Example:
`python main.py verify preferences.txt output.txt`

## Assumptions
- Inputs contain numbers from **1 to n**
- All input and output files are **`.txt` files**
- Files follow the same format as the examples provided on Canvas

## Graphs
![Matching runtime graph](images/matchingGraph.png)
![Verification runtime graph](images/verifyGraph.png)
