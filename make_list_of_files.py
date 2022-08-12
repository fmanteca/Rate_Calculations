import os
import shutil
import glob

list_dirs = [
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/ZeroBias',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-1000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-3000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-500mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-1000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-500mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-125_MFF-25_CTau-1500mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-125_MFF-12_CTau-9000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-10000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-125_MFF-25_CTau-15000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-500mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-1000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-1000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-10000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-10000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-500mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-125_MFF-12_CTau-900mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-10000mm_TuneCP5_14TeV_pythia8',
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-30000mm_TuneCP5_14TeV_pythia8',
]

# make list of files 

for directory in list_dirs:
    for f in glob.glob(directory + '/**/*.root',recursive=True):
        os.system('echo ' + f + ' >> file_args.txt')
