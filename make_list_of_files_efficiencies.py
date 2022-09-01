import os
import shutil
import glob

list_dirs = [
    '/eos/cms/store/group/phys_smp/fernanpe/Eff_Rate/Final',
]

# make list of files 

for directory in list_dirs:
    for f in glob.glob(directory + '/**/*.root',recursive=True):
        os.system('echo ' + f + ' >> file_args_efficiencies.txt')
