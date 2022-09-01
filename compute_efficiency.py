from ROOT import TFile, TTree
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "Receive the parameters")
    parser.add_argument('--in_path', action = 'store', type = str, dest = 'in_path', help = 'input file')
    args = parser.parse_args()
    
    if "MH" in args.in_path:
        sample = args.in_path.split('_')
        HM = (sample[3])
        LLPM = (sample[5])
        CTau = (sample[7][0:-7])
    else:
        HM = "Zero"
        LLPM = "Bias"
        CTau = "Data"


    File = TFile(args.in_path,"READ")

    #clct = File.Get("MuonNtuplizerCath/FlatTree")
    #alct = File.Get("MuonNtuplizerAnod/FlatTree")
    tree = File.Get("MuonNtuplizer/FlatTree")

    nEntries = tree.GetEntries()
    nEvents_passAcc = 0
    nEvents_pass1loose = 0
    nEvents_pass1nominal = 0
    nEvents_pass1tight = 0
    nEvents_pass2loose = 0
    nEvents_pass2loose_or_1nominal = 0
    nEvents_pass2loose_or_1tight = 0
    nEvents_pass2loose_or_1nominal_diffSectors = 0
    nEvents_pass2loose_or_1tight_diffSectors = 0

    for i in range(0, nEntries):
        tree.GetEntry(i)

        # Select MC events with at least one LLP in acceptance
        # Accomplished in about 2% of the cases according to branch gen_llp_in_acceptance
        # Selection: 0.9 < abs(eta) < 2.4, 568. < abs(vz) < 1100, xy radius < 695.5
        if "MH" in args.in_path:
            if len(tree.gen_llp_in_acceptance) == 1:
                if(tree.gen_llp_in_acceptance[0] != 1):
                    continue
            elif len(tree.gen_llp_in_acceptance) == 2:
                if(tree.gen_llp_in_acceptance[0] != 1 and tree.gen_llp_in_acceptance[1] != 1):
                    continue
            else:
                continue
                
            nEvents_passAcc+=1
        
        nLooseShowers = 0
        nNominalShowers = 0
        nTightShowers = 0
        sectors = []
        
        # Skip events without showers
        if not len(tree.csc_shower_isLooseInTime) > 0:
            continue

        # iterate over all the tagged CSC showers in the event
        for shower in range(len(tree.csc_shower_isLooseInTime)):
            if tree.csc_shower_isLooseInTime[shower]:
                nLooseShowers+=1
                sectors.append(tree.csc_shower_sector[shower]*tree.csc_shower_region[shower])
            if tree.csc_shower_isNominalInTime[shower]:
                nNominalShowers+=1
            if tree.csc_shower_isTightInTime[shower]:
                nTightShowers+=1
        
        pass_2LooseDifferentSectors = False
        if len(set(sectors)) > 1:
            pass_2LooseDifferentSectors = True
            
        if nLooseShowers > 0:
            nEvents_pass1loose+=1
        if nNominalShowers > 0:
            nEvents_pass1nominal+=1
        if nTightShowers > 0:
            nEvents_pass1tight+=1
        if nLooseShowers > 1:
            nEvents_pass2loose+=1
        if nLooseShowers > 1 or nNominalShowers > 0:
            nEvents_pass2loose_or_1nominal+=1
        if pass_2LooseDifferentSectors or nNominalShowers > 0:
            nEvents_pass2loose_or_1nominal_diffSectors+=1
        if nLooseShowers > 1 or nTightShowers > 0:
            nEvents_pass2loose_or_1tight+=1
        if pass_2LooseDifferentSectors or nTightShowers > 0:
            nEvents_pass2loose_or_1tight_diffSectors+=1
                
                    
        
    if "MH" in args.in_path:
        with open('Efficiency_output.txt', 'a') as f:
            f.write("%s,%s,%s,%i,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%\n"%(HM,LLPM,CTau,nEvents_passAcc,nEvents_pass1loose/nEvents_passAcc*100,nEvents_pass1nominal/nEvents_passAcc*100,nEvents_pass1tight/nEvents_passAcc*100,nEvents_pass2loose/nEvents_passAcc*100,nEvents_pass2loose_or_1nominal/nEvents_passAcc*100,nEvents_pass2loose_or_1tight/nEvents_passAcc*100,nEvents_pass2loose_or_1nominal_diffSectors/nEvents_passAcc*100,nEvents_pass2loose_or_1tight_diffSectors/nEvents_passAcc*100))
    else:
        with open('Efficiency_output.txt', 'a') as f:
            f.write("%s,%s,%s,%i,%.2f kHz,%.2f kHZ,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz\n"%(HM,LLPM,CTau,nEntries,nEvents_pass1loose/nEntries*30000,nEvents_pass1nominal/nEntries*30000,nEvents_pass1tight/nEntries*30000,nEvents_pass2loose/nEntries*30000,nEvents_pass2loose_or_1nominal/nEntries*30000,nEvents_pass2loose_or_1tight/nEntries*30000,nEvents_pass2loose_or_1nominal_diffSectors/nEntries*30000,nEvents_pass2loose_or_1tight_diffSectors/nEntries*30000))



