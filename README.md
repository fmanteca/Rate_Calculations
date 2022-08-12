# Rate_Calculations


## Step 0: Create input trees

    cmsrel CMSSW_12_3_5
    cd CMSSW_12_3_5/src
    cmsenv
    git clone https://github.com/gem-sw/GEMCode.git
    scram b -j 20
    python3 LLPToHadronicShowers/multicrab_RAW2DIGI_L1_ANA.py --sampleChoice 2

(don't forget to modify the output path)

My outputs (Data and Signal MC) are stored on lxplus eos at:
  - /eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/

## Step 1: Create analysis Trees

    git clone git@github.com:fmanteca/Rate_Calculations.git

Open file **tree_maker.ipynb**. You can use the Swan Service on lxplus: https://swan.cern.ch/

Run it and input the name of the dataset you want to process.
The program will save the highest number of hits in a single chamber for each station/ring for each events.
The file has to be run individually for each dataset you want to process.

### Condor submission

The huge amount of heavy data samples makes the usage of **tree_maker.ipynb** unfeasible.
The code in **tree_maker.ipynb** has been copied to the **make_trees.py.py** module, that takes as input a root file from the emulator.

To submit jobs to condor you need first to build the list of input root files:

    python3 make_list_of_files.py

The output txt file can be used as condor argument.
To launch the jobs:

    condor_submit condor.sub

Once finisehd, merge the output files:

    source doHadd.sh

## Step 2: Calculate Optimal Thresholds

Open file **Optimal_Threshold_Calculator.ipynb**.
Select background file in "input_bkg" and select as many signal files as you'd like to optimize in "input_sig".
The program will find optimal thresholds to maximize efficiency while keeping rate below 1 KhZ.
Set "hard_cuts = True" to just have the program return rate and efficiency for given thresholds without calculating new ones.
Use the file **Efficiency_Calculator.ipynb** to more quickly calculate efficiency for whichever samples you want to check.

## Step 3: Create Efficiency vs. Rate ROC Curves

Open file **ROC_maker.ipynb**.
Select background file in "input_bkg" and select as many signal files as you'd like to include in the curbes in "input_sig".
The program will draw a ROC curve for each station/ring.

## Step 4: Create Comparison Plots

Open file **Comparison_Plot_Maker.ipynb**.
Select background file in "F1" and select as many signal files as you'd like to plot in "signal".
The program will create plots showing the distribution of max hits for each station/ring.

## Step 5: Compute efficiencies and rates

    git clone https://github.com/Nik-Menendez/LLPToHadronicShowers.git
    cd LLPToHadronicShowers
    pip3 install uproot4
    pip3 install awkward1
    source run_efficiency_simple.sh
