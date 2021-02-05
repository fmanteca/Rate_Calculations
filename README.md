# Rate_Calculations

Data and Signal MC is stored on Fermilab LPC machine at:
  - /uscms/home/menendez/nobackup/Trigger/CMSSW_10_6_4/src/Data/

# Step 1: Create Trees

Open file **tree_maker.ipynb**.
Run it and input the name of the dataset you want to process.
The program will save the highest number of hits in a single chamber for each station/ring for each events.
The file has to be run individually for each dataset you want to process.

# Step 2: Calculate Optimal Thresholds

Open file **Optimal_Threshold_Calculator.ipynb**.
Select background file in "input_bkg" and select as many signal files as you'd like to optimize in "input_sig".
The program will find optimal thresholds to maximize efficiency while keeping rate below 1 KhZ.
Set "hard_cuts = True" to just have the program return rate and efficiency for given thresholds without calculating new ones.
Use the file **Efficiency_Calculator.ipynb** to more quickly calculate efficiency for whichever samples you want to check.

# Step 3: Create Efficiency vs. Rate ROC Curves

Open file **ROC_maker.ipynb**.
Select background file in "input_bkg" and select as many signal files as you'd like to include in the curbes in "input_sig".
The program will draw a ROC curve for each station/ring.

# Step 4: Create Comparison Plots

Open file **Comparison_Plot_Maker.ipynb**.
Select background file in "F1" and select as many signal files as you'd like to plot in "signal".
The program will create plots showing the distribution of max hits for each station/ring.


