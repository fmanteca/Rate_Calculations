import os
import shutil
import glob

# list_dirs = [
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
#     '',
# ]



list_dirs = [
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-1000mm_TuneCP5_14TeV_pythia8/',
]

for directory in list_dirs:
    for f in glob.glob(directory + '**/*.root',recursive=True):
        os.system('echo ' + f + ' > file_args.txt')
        os.system('condor_submit condor.sub')

#        subcom = './make_trees.sh ' + str(f)
#        os.system(subcom)
