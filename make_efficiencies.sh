#!/bin/sh

cd /afs/cern.ch/work/f/fernanpe/CMSSW_12_3_5/src/Rate_Calculations
cmsenv

python3 compute_efficiency.py --in_path $1
