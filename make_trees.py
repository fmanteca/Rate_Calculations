from ROOT import TFile, TTree
from ROOT import gROOT, AddressOf
import uproot
from array import array
from tqdm import tqdm
import numpy as np
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "Receive the parameters")
    parser.add_argument('--in_path', action = 'store', type = str, dest = 'in_path', help = 'inut file')
    args = parser.parse_args()

    comp_ME11 = array('f', [0.])
    comp_ME12 = array('f', [0.])
    comp_ME13 = array('f', [0.])
    comp_ME21 = array('f', [0.])
    comp_ME22 = array('f', [0.])
    comp_ME31 = array('f', [0.])
    comp_ME32 = array('f', [0.])
    comp_ME41 = array('f', [0.])
    comp_ME42 = array('f', [0.])

    wire_ME11 = array('f', [0.])
    wire_ME12 = array('f', [0.])
    wire_ME13 = array('f', [0.])
    wire_ME21 = array('f', [0.])
    wire_ME22 = array('f', [0.])
    wire_ME31 = array('f', [0.])
    wire_ME32 = array('f', [0.])
    wire_ME41 = array('f', [0.])
    wire_ME42 = array('f', [0.])

    # light file
    #in_path = "/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-1000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_350_MFF_160_CTau_1000mm_L1_ANA/220708_191825/0000/out_ana_muonshower_4.root"
    
    # light data file
    #in_path = '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220708_112250/0001/out_ana_muonshower_1995.root'


    if 'ZeroBias' in args.in_path:
        out_path = "/eos/user/f/fernanpe/Rate_Calculations/trees/" + args.in_path.split('/')[12].replace('out','data_prodblock_' + args.in_path.split('/')[11])
    else:
        out_path = "/eos/user/f/fernanpe/Rate_Calculations/trees/" + args.in_path.split('/')[12].replace('out','HTo2LongLivedTo4b_prodblock_' + args.in_path.split('/')[11] + '_' + args.in_path.split('/')[8].split('_')[1] + '_' + args.in_path.split('/')[8].split('_')[2] + '_' + args.in_path.split('/')[8].split('_')[3])

    f = TFile( out_path, 'RECREATE' )
    comp_tree = TTree( 'comparator', 'Max Comparator digis in a single chamber in each ring per event' )
    wire_tree = TTree( 'wire', 'Max Comparator digis in a single chamber in each ring per event' )

    comp_tree.Branch( 'Ev_max_nComp_ME11', comp_ME11, 'comp_ME11/F')
    comp_tree.Branch( 'Ev_max_nComp_ME12', comp_ME12, 'comp_ME12/F')
    comp_tree.Branch( 'Ev_max_nComp_ME13', comp_ME13, 'comp_ME13/F')
    comp_tree.Branch( 'Ev_max_nComp_ME21', comp_ME21, 'comp_ME21/F')
    comp_tree.Branch( 'Ev_max_nComp_ME22', comp_ME22, 'comp_ME22/F')
    comp_tree.Branch( 'Ev_max_nComp_ME31', comp_ME31, 'comp_ME31/F')
    comp_tree.Branch( 'Ev_max_nComp_ME32', comp_ME32, 'comp_ME32/F')
    comp_tree.Branch( 'Ev_max_nComp_ME41', comp_ME41, 'comp_ME41/F')
    comp_tree.Branch( 'Ev_max_nComp_ME42', comp_ME42, 'comp_ME42/F')

    wire_tree.Branch( 'Ev_max_nWire_ME11', wire_ME11, 'wire_ME11/F')
    wire_tree.Branch( 'Ev_max_nWire_ME12', wire_ME12, 'wire_ME12/F')
    wire_tree.Branch( 'Ev_max_nWire_ME13', wire_ME13, 'wire_ME13/F')
    wire_tree.Branch( 'Ev_max_nWire_ME21', wire_ME21, 'wire_ME21/F')
    wire_tree.Branch( 'Ev_max_nWire_ME22', wire_ME22, 'wire_ME22/F')
    wire_tree.Branch( 'Ev_max_nWire_ME31', wire_ME31, 'wire_ME31/F')
    wire_tree.Branch( 'Ev_max_nWire_ME32', wire_ME32, 'wire_ME32/F')
    wire_tree.Branch( 'Ev_max_nWire_ME41', wire_ME41, 'wire_ME41/F')
    wire_tree.Branch( 'Ev_max_nWire_ME42', wire_ME42, 'wire_ME42/F')

    
    File = TFile(args.in_path,"READ")

    clct = File.Get("MuonNtuplizerCath/FlatTree")
    alct = File.Get("MuonNtuplizerAnod/FlatTree")
    lct = File.Get("MuonNtuplizer/FlatTree")

    nEntries_clct = clct.GetEntries()
    nEntries_alct = alct.GetEntries()

    good_times = [6,7,8] # BX 7 is the nominal bunch crossing. BX 6 is -1 and 8 is +1                                                                                                                         


    print("Starting CLCT Analysis")
    for i in tqdm(range(0, nEntries_clct)):
        clct.GetEntry(i)

        # Select MC events with at least one LLP in acceptance
        # Accomplished in 2% of the cases according to branch gen_llp_in_acceptance? TO BE ASKED
        #if "MH" in in_path:
        #    if clct.gen_llp_in_acceptance[0] != 1 and clct.gen_llp_in_acceptance[1] != 1

        counter_nComp_posEndcap = np.zeros((5,4))
        counter_nComp_negEndcap = np.zeros((5,4))
        counter_nComp = np.zeros((5,4))

        # Loop over all the hits in the event
        for hit in range(len(clct.csc_comp_time)):
        
            # keep only in time hits
            if clct.csc_comp_time[hit] not in good_times:
                continue
            
            # ring number = 4 means ME1a, assuming that ME1a is an extension of ME1b. But they should be decoupled 
            # https://cmssdt.cern.ch/lxr/source/DataFormats/MuonDetId/interface/CSCIndexer.h?v=CMSSW_10_6_20
            # https://github.com/cms-sw/cmssw/issues/25200#issuecomment-438723065
        
            if clct.csc_comp_ring[hit] == 4:
                continue
        
            # Count in time hits in each CSC chamber
            if clct.csc_comp_region[hit] == 1:
                if(clct.csc_comp_station[hit] == 1):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_posEndcap[1][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_posEndcap[1][2] += 1
                    elif(clct.csc_comp_ring[hit] == 3):
                        counter_nComp_posEndcap[1][3] += 1
                if(clct.csc_comp_station[hit] == 2):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_posEndcap[2][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_posEndcap[2][2] += 1
                if(clct.csc_comp_station[hit] == 3):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_posEndcap[3][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_posEndcap[3][2] += 1
                if(clct.csc_comp_station[hit] == 4):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_posEndcap[4][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_posEndcap[4][2] += 1
            elif clct.csc_comp_region[hit] == -1:
                if(clct.csc_comp_station[hit] == 1):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_negEndcap[1][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_negEndcap[1][2] += 1
                    elif(clct.csc_comp_ring[hit] == 3):
                        counter_nComp_negEndcap[1][3] += 1
                if(clct.csc_comp_station[hit] == 2):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_negEndcap[2][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_negEndcap[2][2] += 1
                if(clct.csc_comp_station[hit] == 3):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_negEndcap[3][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_negEndcap[3][2] += 1
                if(clct.csc_comp_station[hit] == 4):
                    if(clct.csc_comp_ring[hit] == 1):
                        counter_nComp_negEndcap[4][1] += 1
                    elif(clct.csc_comp_ring[hit] == 2):
                        counter_nComp_negEndcap[4][2] += 1
            else:
                print(clct.csc_comp_region[hit])

    
        # Calculate the maximum of the two endcaps (chamber by chamber)
        counter_nComp = np.maximum(counter_nComp_posEndcap,counter_nComp_negEndcap)
    
        # Events with 0 hits in time?. Less than 1% of the events
        # I will keep them by setting nMaxHits = 0 in all the chambers
        #if np.array_equal(counter_nComp, np.zeros((5,4))):
        #    continue
    
        # Get the maximum nHit value and its chamber (station and ring indexes)
    
        max_value = np.amax(counter_nComp)
        max_station = np.where(counter_nComp == np.amax(counter_nComp))[0] #if repeated nhits, len(max_station) will be greater than 1
        max_ring = np.where(counter_nComp == np.amax(counter_nComp))[1]

        max_nComp = np.zeros((5,4))
    
        # It is possible that two different chambers have the same number of hits. In that case both nhits values are stored for both of them

        for chamber in zip(max_station.tolist(), max_ring.tolist()):
            max_nComp[chamber[0]][chamber[1]] = max_value
        
        comp_ME11[0] = max_nComp[1][1]
        comp_ME12[0] = max_nComp[1][2]
        comp_ME13[0] = max_nComp[1][3]
        comp_ME21[0] = max_nComp[2][1]
        comp_ME22[0] = max_nComp[2][2]
        comp_ME31[0] = max_nComp[3][1]
        comp_ME32[0] = max_nComp[3][2]
        comp_ME41[0] = max_nComp[4][1]
        comp_ME42[0] = max_nComp[4][2]
    
        comp_tree.Fill()



    print("Starting ALCT Analysis")
    for i in tqdm(range(0, nEntries_alct)):
        alct.GetEntry(i)
    
        counter_nWire_posEndcap = np.zeros((5,4))
        counter_nWire_negEndcap = np.zeros((5,4))
        counter_nWire = np.zeros((5,4))

        # Loop over all the hits in the event
        for hit in range(len(alct.csc_wire_time)):
        
            # keep only in time hits
            if alct.csc_wire_time[hit] not in good_times:
                continue
            
            # ring number = 4 means ME1a, assuming that ME1a is an extension of ME1b. But they should be decoupled 
            # https://cmssdt.cern.ch/lxr/source/DataFormats/MuonDetId/interface/CSCIndexer.h?v=CMSSW_10_6_20
            # https://github.com/cms-sw/cmssw/issues/25200#issuecomment-438723065
        
            if alct.csc_wire_ring[hit] == 4:
                continue
            
        
            # Count in time hits in each CSC chamber
            if alct.csc_wire_region[hit] == 1:
                if(alct.csc_wire_station[hit] == 1):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_posEndcap[1][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_posEndcap[1][2] += 1
                    elif(alct.csc_wire_ring[hit] == 3):
                        counter_nWire_posEndcap[1][3] += 1
                if(alct.csc_wire_station[hit] == 2):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_posEndcap[2][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_posEndcap[2][2] += 1
                if(alct.csc_wire_station[hit] == 3):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_posEndcap[3][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_posEndcap[3][2] += 1
                if(alct.csc_wire_station[hit] == 4):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_posEndcap[4][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_posEndcap[4][2] += 1
            elif alct.csc_wire_region[hit] == -1:
                if(alct.csc_wire_station[hit] == 1):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_negEndcap[1][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_negEndcap[1][2] += 1
                    elif(alct.csc_wire_ring[hit] == 3):
                        counter_nWire_negEndcap[1][3] += 1
                if(alct.csc_wire_station[hit] == 2):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_negEndcap[2][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_negEndcap[2][2] += 1
                if(alct.csc_wire_station[hit] == 3):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_negEndcap[3][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_negEndcap[3][2] += 1
                if(alct.csc_wire_station[hit] == 4):
                    if(alct.csc_wire_ring[hit] == 1):
                        counter_nWire_negEndcap[4][1] += 1
                    elif(alct.csc_wire_ring[hit] == 2):
                        counter_nWire_negEndcap[4][2] += 1
            else:
                print(alct.csc_wire_region[hit])

    
        # Calculate the maximum of the two endcaps (chamber by chamber)
        counter_nWire = np.maximum(counter_nWire_posEndcap,counter_nWire_negEndcap)

        # Events with 0 hits in time?. Less than 1% of the events
        # I will keep them by setting nMaxHits = 0 in all the chambers
        #if np.array_equal(counter_nWire, np.zeros((5,4))):
        #    continue
        
        # Get the maximum nHit value and its chamber (station and ring indexes)
        
        max_value = np.amax(counter_nWire)
        max_station = np.where(counter_nWire == np.amax(counter_nWire))[0] #if repeated nhits, len(max_station) will be greater than 1
        max_ring = np.where(counter_nWire == np.amax(counter_nWire))[1]
        
        max_nWire = np.zeros((5,4))
    
        # It is possible that two different chambers have the same number of hits. In that case both nhits values are stored for both of them

        for chamber in zip(max_station.tolist(), max_ring.tolist()):
            max_nWire[chamber[0]][chamber[1]] = max_value

                    
        wire_ME11[0] = max_nWire[1][1]
        wire_ME12[0] = max_nWire[1][2]
        wire_ME13[0] = max_nWire[1][3]
        wire_ME21[0] = max_nWire[2][1]
        wire_ME22[0] = max_nWire[2][2]
        wire_ME31[0] = max_nWire[3][1]
        wire_ME32[0] = max_nWire[3][2]
        wire_ME41[0] = max_nWire[4][1]
        wire_ME42[0] = max_nWire[4][2]
    
        wire_tree.Fill()


    f.Write()
    f.Close()
