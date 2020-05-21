# Rate_Calculations

Data is stored on LPC machine at:
  -Data: /uscms/home/menendez/nobackup/Trigger/CMSSW_10_6_4/src/Data/TPEHists_Data.root
  -Signal MC: /uscms/home/menendez/nobackup/Trigger/CMSSW_10_6_4/src/Data/TPEHists_LLP.root
  -Neutrino Gun MC: /uscms/home/menendez/nobackup/Trigger/CMSSW_10_6_4/src/Data/TPEHists_Neutrino_gun.root
  
Define thresholds in Count.py on lines 57 and 58
  
  Leave first index open. First list is for ring one, each index in the list is each station.
    
    e.g. [[0,ME1/1,ME2/1,ME3/1,ME4/1],[0,ME1/2,ME2/2,ME3/2,ME4/2]]
  
  threshold_chamber is more than. So threshold_chamber = 0 means the threshold is >0

Single general threshold is X on line 66 
 
run using:
  
  python Count.py
  
You can compare the distributions of two different samples after running each using comp_sig_mc.cxx in results/
