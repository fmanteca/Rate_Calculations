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
count_c = 0
count_w = 0
Ev_count_c = 0.0
Ev_count_w = 0.0
max_nComp = 0
max_nWire = 0
numEventsclct = 0.0
numEventsalct = 0.0
alreadyfilled=False

station_nComp = [0,0,0,0,0]
station_nWire = [0,0,0,0,0]
station_count_c = [0.0,0.0,0.0,0.0,0.0]
station_count_w = [0.0,0.0,0.0,0.0,0.0]
Ev_station_count_c = [0.0,0.0,0.0,0.0,0.0]
Ev_station_count_w = [0.0,0.0,0.0,0.0,0.0]

sector_nComp = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
sector_nWire = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
sector_count_c = [[ [0.0 for col in range(5)] for col in range(2)] for row in range(6)]
sector_count_w = [[ [0.0 for col in range(5)] for col in range(2)] for row in range(6)]
Ev_sector_count_c = [[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
Ev_sector_count_w = [[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]

threshold_nComp = [[0,25,15,10,10],[0,10,7,7,7]]
threshold_nWire = [[0,25,20,15,15],[0,10,10,7,7]]
threshold_chamber = 1

station_rate_c = [0.0,0.0,0.0,0.0,0.0]
station_rate_w = [0.0,0.0,0.0,0.0,0.0]
sector_rate_c = [[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
sector_rate_w = [[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]

X = 25

hists = []
Ev_max_nComp = TH1F("Ev_max_nComp","Max nComp per Event", 40, -.5, 39.5); hists.append(Ev_max_nComp)
Ev_max_nWire = TH1F("Ev_max_nWire","Max nWire per Event", 40, -.5, 39.5); hists.append(Ev_max_nWire)
Ev_max_nComp_ME1 = TH1F("Ev_max_nComp_ME1","Max nComp per Event in ME1", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME1)
Ev_max_nComp_ME2 = TH1F("Ev_max_nComp_ME2","Max nComp per Event in ME2", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME2)
Ev_max_nComp_ME3 = TH1F("Ev_max_nComp_ME3","Max nComp per Event in ME3", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME3)
Ev_max_nComp_ME4 = TH1F("Ev_max_nComp_ME4","Max nComp per Event in ME4", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME4)
Ev_max_nWire_ME1 = TH1F("Ev_max_nWire_ME1","Max nWire per Event in ME1", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME1)
Ev_max_nWire_ME2 = TH1F("Ev_max_nWire_ME2","Max nWire per Event in ME2", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME2)
Ev_max_nWire_ME3 = TH1F("Ev_max_nWire_ME3","Max nWire per Event in ME3", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME3)
Ev_max_nWire_ME4 = TH1F("Ev_max_nWire_ME4","Max nWire per Event in ME4", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME4)

Ev_max_nComp_ME11 = TH1F("Ev_max_nComp_ME11","Max nComp per Event in a Single Sector in ME1/1", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME11)
Ev_max_nComp_ME12 = TH1F("Ev_max_nComp_ME12","Max nComp per Event in a Single Sector in ME1/2", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME12)
Ev_max_nComp_ME21 = TH1F("Ev_max_nComp_ME21","Max nComp per Event in a Single Sector in ME2/1", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME21)
Ev_max_nComp_ME22 = TH1F("Ev_max_nComp_ME22","Max nComp per Event in a Single Sector in ME2/2", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME22)
Ev_max_nComp_ME31 = TH1F("Ev_max_nComp_ME31","Max nComp per Event in a Single Sector in ME3/1", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME31)
Ev_max_nComp_ME32 = TH1F("Ev_max_nComp_ME32","Max nComp per Event in a Single Sector in ME3/2", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME32)
Ev_max_nComp_ME41 = TH1F("Ev_max_nComp_ME41","Max nComp per Event in a Single Sector in ME4/1", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME41)
Ev_max_nComp_ME42 = TH1F("Ev_max_nComp_ME42","Max nComp per Event in a Single Sector in ME4/2", 40, -.5, 39.5); hists.append(Ev_max_nComp_ME42)

Ev_max_nWire_ME11 = TH1F("Ev_max_nWire_ME11","Max nWire per Event in a Single Sector in ME1/1", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME11)
Ev_max_nWire_ME12 = TH1F("Ev_max_nWire_ME12","Max nWire per Event in a Single Sector in ME1/2", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME12)
Ev_max_nWire_ME21 = TH1F("Ev_max_nWire_ME21","Max nWire per Event in a Single Sector in ME2/1", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME21)
Ev_max_nWire_ME22 = TH1F("Ev_max_nWire_ME22","Max nWire per Event in a Single Sector in ME2/2", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME22)
Ev_max_nWire_ME31 = TH1F("Ev_max_nWire_ME31","Max nWire per Event in a Single Sector in ME3/1", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME31)
Ev_max_nWire_ME32 = TH1F("Ev_max_nWire_ME32","Max nWire per Event in a Single Sector in ME3/2", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME32)
Ev_max_nWire_ME41 = TH1F("Ev_max_nWire_ME41","Max nWire per Event in a Single Sector in ME4/1", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME41)
Ev_max_nWire_ME42 = TH1F("Ev_max_nWire_ME42","Max nWire per Event in a Single Sector in ME4/2", 40, -.5, 39.5); hists.append(Ev_max_nWire_ME42)

print "Creating histograms"
for i in tqdm(range(len(hists))):
  hists[i].GetYaxis().SetTitle("Events")
  if(i==0 or i==2 or i==3 or i==4 or i==5):
    hists[i].GetXaxis().SetTitle("# Comparator Digis")
  elif(i==1 or i==6 or i==7 or i==8 or i==9):
    hists[i].GetXaxis().SetTitle("# Wire Digis")
  elif(i>9 and i<=17):
    hists[i].GetXaxis().SetTitle("# Comparator Digis")
  elif(i>17):
    hists[i].GetXaxis().SetTitle("# Wire Digis")
  hists[i].SetDirectory(0)

print "Starting CLCT Analysis"
for i in tqdm(range(0, nEntries_clct),disable=tqdm_disable):
  clct.GetEntry(i)
 
  if(clct.t_Event!=lastEventclct):
    if(count_c > 0):
      Ev_count_c+=1
    count_c=0
    for j in range(1,len(station_nComp)):
      if(station_count_c[j] > threshold_chamber):
        Ev_station_count_c[j]+=1
      for l in range(2):
        for k in range(6):
          if(alreadyfilled): continue
          if(sector_count_c[k][l][j] > threshold_chamber):
            Ev_sector_count_c[l][j]+=1
            alreadyfilled=True
        alreadyfilled=False
    station_count_c = [0.0,0.0,0.0,0.0,0.0]
    sector_count_c = [[ [0.0 for col in range(5)] for col in range(2)] for row in range(6)]

    #Fill Histogram with max nComp of event
    Ev_max_nComp.Fill(max_nComp)
    max_nComp = 0

    #Fill Histograms with max nComp per station
    Ev_max_nComp_ME1.Fill(station_nComp[1])
    Ev_max_nComp_ME2.Fill(station_nComp[2])
    Ev_max_nComp_ME3.Fill(station_nComp[3])
    Ev_max_nComp_ME4.Fill(station_nComp[4])
    station_nComp = [0,0,0,0,0]

    #Fill Histograms with max nComp in a single sector
    Ev_max_nComp_ME11.Fill(sector_nComp[1][0])
    Ev_max_nComp_ME12.Fill(sector_nComp[1][1])
    Ev_max_nComp_ME21.Fill(sector_nComp[2][0])
    Ev_max_nComp_ME22.Fill(sector_nComp[2][1])
    Ev_max_nComp_ME31.Fill(sector_nComp[3][0])
    Ev_max_nComp_ME32.Fill(sector_nComp[3][1])
    Ev_max_nComp_ME41.Fill(sector_nComp[4][0])
    Ev_max_nComp_ME42.Fill(sector_nComp[4][1])
    sector_nComp = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

    numEventsclct+=1
    lastEventclct = clct.t_Event

  if(clct.t_nComp>X):
    count_c+=1
  if(clct.t_nComp > max_nComp):
    max_nComp = clct.t_nComp

  for j in range(1,len(station_nComp)):
    if(clct.t_station == j):
      if(clct.t_nComp > station_nComp[clct.t_station]):
        station_nComp[clct.t_station] = clct.t_nComp
      if(clct.t_nComp > threshold_nComp[0][clct.t_station]):
        station_count_c[clct.t_station]+=1
      if(clct.t_ring==2 or (clct.t_station==1 and clct.t_ring==1)):
        for k in range(6):
          if(clct.t_sector == k+1):
            if(clct.t_nComp > sector_nComp[clct.t_station][clct.t_ring-1]):
              sector_nComp[clct.t_station][clct.t_ring-1] = clct.t_nComp
            if(clct.t_nComp > threshold_nComp[clct.t_ring-1][clct.t_station]):
              sector_count_c[k][clct.t_ring-1][clct.t_station]+=1
      elif(clct.t_ring==1 and clct.t_station!=1):
        for k in range(6):
          if(clct.t_sector == k+1):
            if(clct.t_nComp > sector_nComp[clct.t_station][clct.t_ring-1]):
              sector_nComp[clct.t_station][clct.t_ring-1] = clct.t_nComp
            if(clct.t_nComp > threshold_nComp[clct.t_ring-1][clct.t_station]):
              sector_count_c[k][clct.t_ring-1][clct.t_station]+=1

print "Starting ALCT Analysis"
for i in tqdm(range(0, nEntries_alct),disable=tqdm_disable):
  alct.GetEntry(i)

  if(alct.t_Event!=lastEventalct):
    if(count_w > 0):
      Ev_count_w+=1
    count_w=0
    for j in range(1,len(station_nWire)):
      if(station_count_w[j] > threshold_chamber):
        Ev_station_count_w[j]+=1
      for l in range(2):
        for k in range(6):
          if(alreadyfilled): continue
          if(sector_count_w[k][l][j] > threshold_chamber):
            Ev_sector_count_w[l][j]+=1
            alreadyfilled=True
        alreadyfilled=False
    station_count_w = [0.0,0.0,0.0,0.0,0.0]
    sector_count_w = [[ [0.0 for col in range(5)] for col in range(2)] for row in range(6)]

    #Fill Histogram with max nWire of event
    Ev_max_nWire.Fill(max_nWire)
    max_nWire = 0

    #Fill Histograms with max nWire per station
    Ev_max_nWire_ME1.Fill(station_nWire[1])
    Ev_max_nWire_ME2.Fill(station_nWire[2])
    Ev_max_nWire_ME3.Fill(station_nWire[3])
    Ev_max_nWire_ME4.Fill(station_nWire[4])
    station_nWire = [0,0,0,0,0]

    #Fill Histograms with max nWire in a single sector
    Ev_max_nWire_ME11.Fill(sector_nWire[1][0])
    Ev_max_nWire_ME12.Fill(sector_nWire[1][1])
    Ev_max_nWire_ME21.Fill(sector_nWire[2][0])
    Ev_max_nWire_ME22.Fill(sector_nWire[2][1])
    Ev_max_nWire_ME31.Fill(sector_nWire[3][0])
    Ev_max_nWire_ME32.Fill(sector_nWire[3][1])
    Ev_max_nWire_ME41.Fill(sector_nWire[4][0])
    Ev_max_nWire_ME42.Fill(sector_nWire[4][1])
    sector_nWire = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

    numEventsalct+=1
    lastEventalct = alct.t_Event

  if(alct.t_nWire>X):
    #print "---- Endcap =",alct.t_endcap,", Station =",alct.t_station,", Ring =",alct.t_ring,", and chamber =",alct.t_chamber," has nWire =",alct.t_nWire
    count_w+=1
  if(alct.t_nWire > max_nWire):
    max_nWire = alct.t_nWire

  for j in range(1,len(station_nWire)):
    if(alct.t_station == j):
      if(alct.t_nWire > station_nWire[alct.t_station]):
        station_nWire[alct.t_station] = alct.t_nWire
      if(alct.t_nWire > threshold_nWire[0][alct.t_station]):
        station_count_w[alct.t_station]+=1
      if(alct.t_ring==2 or (alct.t_station==1 and alct.t_ring==1)):
        for k in range(6):
          if(alct.t_sector == k+1):
            if(alct.t_nWire > sector_nWire[alct.t_station][alct.t_ring-1]):
              sector_nWire[alct.t_station][alct.t_ring-1] = alct.t_nWire
            if(alct.t_nWire > threshold_nWire[alct.t_ring-1][alct.t_station]):
              sector_count_w[k][alct.t_ring-1][alct.t_station]+=1
      elif(alct.t_ring==1 and alct.t_station!=1):
        for k in range(6):
          if(alct.t_sector == k+1):
            if(alct.t_nWire > sector_nWire[alct.t_station][alct.t_ring-1]):
              sector_nWire[alct.t_station][alct.t_ring-1] = alct.t_nWire
            if(alct.t_nWire > threshold_nWire[alct.t_ring-1][alct.t_station]):
              sector_count_w[k][alct.t_ring-1][alct.t_station]+=1
 

rate_c = Ev_count_c/numEventsclct*30.0*1000.0
rate_w = Ev_count_w/numEventsalct*30.0*1000.0

for j in range(1,len(station_nComp)):
  station_rate_c[j] = Ev_station_count_c[j]/numEventsclct*30.0*1000.0
  station_rate_w[j] = Ev_station_count_w[j]/numEventsalct*30.0*1000.0
  for k in range(2):
    sector_rate_c[k][j] = Ev_sector_count_c[k][j]/numEventsclct*30.0*1000.0
    sector_rate_w[k][j] = Ev_sector_count_w[k][j]/numEventsalct*30.0*1000.0

File.Close()

save_file = TFile("Event_tree.root","RECREATE")
c1 = TCanvas("c1", "histograms", 900, 700)
print "Saving histograms"
for i in tqdm(range(len(hists))):
  hists[i].Write()
  hists[i].Draw()
  c1.SaveAs("plots/hist"+str(i)+".png")

print "========================== Results =========================="
print "In", int(numEventsclct), "events,", int(Ev_count_c), "events had >", X, "Comparator Digis in a single chamber. Rate =", rate_c, "KHz" 
print "In", int(numEventsalct), "events,", int(Ev_count_w), "events had >", X, "Wire Digis in a single chamber.       Rate =", rate_w, "KHz"
print ""

print "========================== Comparator Rates by Station =========================="
for j in range(1,len(station_nComp)):
  print "In", int(numEventsclct), "events, there are", int(Ev_station_count_c[j]), "events where ME", j, "has >", threshold_chamber, "chambers with >", threshold_nComp[0][j], "Comparator Digis in a single chamber. Rate =", station_rate_c[j], "KHz"
print "============================= Wire Rates by Station ============================="
for j in range(1,len(station_nWire)):  
  print "In", int(numEventsalct), "events, there are", int(Ev_station_count_w[j]), "events where ME", j, "has >", threshold_chamber, "chambers with >", threshold_nWire[0][j], "Wire Digis in a single chamber. Rate =", station_rate_w[j], "KHz"
print""

print "========================== Comparator Rates by Sector =========================="
for j in range(1,len(station_nComp)):
  for k in range(2):
    print "In", int(numEventsclct), "events, there are", int(Ev_sector_count_c[k][j]), "events where at least 1 Sector in ME", j, "/", k+1, "has >", threshold_chamber, "chambers with >", threshold_nComp[k][j], "Comparator Digis in a single chamber. Rate =", sector_rate_c[k][j], "KHz"
print "============================= Wire Rates by Sector ============================="
for j in range(1,len(station_nWire)):
  for k in range(2):
    print "In", int(numEventsalct), "events, there are", int(Ev_sector_count_w[k][j]), "events where at least 1 Sector in ME", j, "/", k+1, "has >", threshold_chamber, "chambers with >", threshold_nWire[k][j], "Wire Digis in a single chamber. Rate =", sector_rate_w[k][j], "KHz"
