#!/bin/sh

cd /afs/cern.ch/work/f/fernanpe/framework_monoHFullRun2/CMSSW_10_2_9/src
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/f/fernanpe/Rate_Calculations 

python make_trees.py --in_path $1
