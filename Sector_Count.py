import os, sys
import ROOT
from ROOT import TH1F,TH2F,TFile,TTree,TCanvas, TProfile, TNtuple, gErrorIgnoreLevel, kInfo, kWarning
from tqdm import tqdm

tqdm_disable = False
ROOT.gErrorIgnoreLevel = kWarning;

File = TFile("Data/TPEHists_2.root","READ")
clct = File.Get("lctreader/Ev_clcttree")
alct = File.Get("lctreader/Ev_alcttree")

nEntries_clct = clct.GetEntries()
nEntries_alct = alct.GetEntries()

clct.GetEntry(0)
alct.GetEntry(0)
lastEventclct = clct.t_Event
lastEventalct = clct.t_Event
numEventsclct = 0.0
numEventsalct = 0.0

sector_nComp = [0,0,0,0,0,0,0]
sector_nWire = [0,0,0,0,0,0,0]
sector_count_c = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
sector_count_w = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
Ev_sector_count_c = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
Ev_sector_count_w = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

threshold_nComp = [[0,25,15,10,10],[0,10,7,7,7],[0,10,0,0,0]]
threshold_nWire = [[0,25,20,15,15],[0,12,12,10,10],[0,10,0,0,0]]
threshold_chamber = 2

sector_rate_c = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
sector_rate_w = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

X = 25

hists = []
Ev_max_nComp_Sec1 = TH1F("Ev_max_nComp_Sec1","Max nComp per Event in Sector 1", 40, -.5, 39.5); hists.append(Ev_max_nComp_Sec1)
Ev_max_nComp_Sec2 = TH1F("Ev_max_nComp_Sec2","Max nComp per Event in Sector 2", 40, -.5, 39.5); hists.append(Ev_max_nComp_Sec2)
Ev_max_nComp_Sec3 = TH1F("Ev_max_nComp_Sec3","Max nComp per Event in Sector 3", 40, -.5, 39.5); hists.append(Ev_max_nComp_Sec3)
Ev_max_nComp_Sec4 = TH1F("Ev_max_nComp_Sec4","Max nComp per Event in Sector 4", 40, -.5, 39.5); hists.append(Ev_max_nComp_Sec4)
Ev_max_nComp_Sec5 = TH1F("Ev_max_nComp_Sec5","Max nComp per Event in Sector 5", 40, -.5, 39.5); hists.append(Ev_max_nComp_Sec5)
Ev_max_nComp_Sec6 = TH1F("Ev_max_nComp_Sec6","Max nComp per Event in Sector 6", 40, -.5, 39.5); hists.append(Ev_max_nComp_Sec6)
Ev_max_nWire_Sec1 = TH1F("Ev_max_nWire_Sec1","Max nWire per Event in Sector 1", 40, -.5, 39.5); hists.append(Ev_max_nWire_Sec1)
Ev_max_nWire_Sec2 = TH1F("Ev_max_nWire_Sec2","Max nWire per Event in Sector 2", 40, -.5, 39.5); hists.append(Ev_max_nWire_Sec2)
Ev_max_nWire_Sec3 = TH1F("Ev_max_nWire_Sec3","Max nWire per Event in Sector 3", 40, -.5, 39.5); hists.append(Ev_max_nWire_Sec3)
Ev_max_nWire_Sec4 = TH1F("Ev_max_nWire_Sec4","Max nWire per Event in Sector 4", 40, -.5, 39.5); hists.append(Ev_max_nWire_Sec4)
Ev_max_nWire_Sec5 = TH1F("Ev_max_nWire_Sec5","Max nWire per Event in Sector 5", 40, -.5, 39.5); hists.append(Ev_max_nWire_Sec5)
Ev_max_nWire_Sec6 = TH1F("Ev_max_nWire_Sec6","Max nWire per Event in Sector 6", 40, -.5, 39.5); hists.append(Ev_max_nWire_Sec6)

print "Creating histograms"
for i in tqdm(range(len(hists))):
  hists[i].GetYaxis().SetTitle("Events")
  if(i<6):
    hists[i].GetXaxis().SetTitle("# Comparator Digis")
  else:
    hists[i].GetXaxis().SetTitle("# Wire Digis")
  hists[i].SetDirectory(0)

print "Starting CLCT Analysis"
for i in tqdm(range(0, nEntries_clct),disable=tqdm_disable):
  clct.GetEntry(i)
 
  if(clct.t_Event!=lastEventclct):
    for j in range(1,len(sector_nComp)):
      if(sector_count_c[j] > threshold_chamber):
        Ev_sector_count_c[j]+=1
    sector_count_c = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

    #Fill Histograms with max nComp per sector
    Ev_max_nComp_Sec1.Fill(sector_nComp[1])
    Ev_max_nComp_Sec2.Fill(sector_nComp[2])
    Ev_max_nComp_Sec3.Fill(sector_nComp[3])
    Ev_max_nComp_Sec4.Fill(sector_nComp[4])
    Ev_max_nComp_Sec5.Fill(sector_nComp[5])
    Ev_max_nComp_Sec6.Fill(sector_nComp[6])
    sector_nComp = [0,0,0,0,0,0,0]

    numEventsclct+=1
    lastEventclct = clct.t_Event

  for j in range(1,len(sector_nComp)):
    if(clct.t_sector == j):
      if(clct.t_nComp > sector_nComp[clct.t_sector]):
        sector_nComp[clct.t_sector] = clct.t_nComp
      if(clct.t_nComp > threshold_nComp[clct.t_ring-1][clct.t_station]):
        sector_count_c[clct.t_sector]+=1

print "Starting ALCT Analysis"
for i in tqdm(range(0, nEntries_alct),disable=tqdm_disable):
  alct.GetEntry(i)

  if(alct.t_Event!=lastEventalct):
    for j in range(1,len(sector_nWire)):
      if(sector_count_w[j] > threshold_chamber):
        Ev_sector_count_w[j]+=1
    sector_count_w = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

    #Fill Histograms with max nComp per sector
    Ev_max_nWire_Sec1.Fill(sector_nWire[1])
    Ev_max_nWire_Sec2.Fill(sector_nWire[2])
    Ev_max_nWire_Sec3.Fill(sector_nWire[3])
    Ev_max_nWire_Sec4.Fill(sector_nWire[4])
    Ev_max_nWire_Sec5.Fill(sector_nWire[5])
    Ev_max_nWire_Sec6.Fill(sector_nWire[6])
    sector_nWire = [0,0,0,0,0,0,0]

    numEventsalct+=1
    lastEventalct = alct.t_Event

  for j in range(1,len(sector_nWire)):
    if(alct.t_sector == j):
      if(alct.t_nWire > sector_nWire[alct.t_sector]):
        sector_nWire[alct.t_sector] = alct.t_nWire
      if(alct.t_nWire > threshold_nWire[alct.t_ring-1][alct.t_station]):
        sector_count_w[alct.t_sector]+=1   
 

for j in range(1,len(sector_nComp)):
  sector_rate_c[j] = Ev_sector_count_c[j]/numEventsclct*30.0*1000.0
  sector_rate_w[j] = Ev_sector_count_w[j]/numEventsalct*30.0*1000.0

File.Close()

save_file = TFile("Event_tree.root","RECREATE")
c1 = TCanvas("c1", "histograms", 900, 700)
print "Saving histograms"
for i in tqdm(range(len(hists))):
  hists[i].Write()
  hists[i].Draw()
  c1.SaveAs("plots/sector_hist"+str(i)+".png")

print "========================== Comparator Rates by Sector =========================="
for j in range(1,len(sector_nComp)):
  print "In", int(numEventsclct), "events, there are", int(Ev_sector_count_c[j]), "events where Sector", j, "has >", threshold_chamber, "chambers with >", threshold_nComp[0][1], "in ME1/1, >", threshold_nComp[1][1], "in ME1/2, >", threshold_nComp[0][2], "in ME2/1, >", threshold_nComp[1][2], "in ME2/2, >", threshold_nComp[0][3], "in ME3/1, >", threshold_nComp[1][3], "in ME3/2, >", threshold_nComp[0][4], "in ME4/1, >", threshold_nComp[1][4], "in ME4/1. Rate =", sector_rate_c[j], "KHz"
print "============================= Wire Rates by Sector ============================="
for j in range(1,len(sector_nWire)):
  print "In", int(numEventsalct), "events, there are", int(Ev_sector_count_w[j]), "events where Sector", j, "has >", threshold_chamber, "chambers with >", threshold_nWire[0][1], "in ME1/1, >", threshold_nWire[1][1], "in ME1/2, >", threshold_nWire[0][2], "in ME2/1, >", threshold_nWire[1][2], "in ME2/2, >", threshold_nWire[0][3], "in ME3/1, >", threshold_nWire[1][3], "in ME3/2, >", threshold_nWire[0][4], "in ME4/1, >", threshold_nWire[1][4], "in ME4/1. Rate =", sector_rate_w[j], "KHz"
