#include "TH1F.h"
#include "TH1D.h"
#include "TRandom.h"
#include <vector>
#include <iostream>

void comp_sig_mc()
{

  std::vector<TH1D*> histssg;
  std::vector<TH1D*> histsmc;

  TFile *fsg = new TFile("Event_tree_Data.root");
  TFile *fmc = new TFile("Event_tree_MC.root");

  TH1D *Ev_max_nComp_sg, *Ev_max_nWire_sg, 
       *Ev_max_nComp_ME1_sg, *Ev_max_nComp_ME2_sg, *Ev_max_nComp_ME3_sg, *Ev_max_nComp_ME4_sg,
       *Ev_max_nWire_ME1_sg, *Ev_max_nWire_ME2_sg, *Ev_max_nWire_ME3_sg, *Ev_max_nWire_ME4_sg,
       *Ev_max_nComp_ME11_sg, *Ev_max_nComp_ME12_sg, *Ev_max_nComp_ME21_sg, *Ev_max_nComp_ME22_sg, *Ev_max_nComp_ME31_sg, *Ev_max_nComp_ME32_sg, *Ev_max_nComp_ME41_sg, *Ev_max_nComp_ME42_sg,
       *Ev_max_nWire_ME11_sg, *Ev_max_nWire_ME12_sg, *Ev_max_nWire_ME21_sg, *Ev_max_nWire_ME22_sg, *Ev_max_nWire_ME31_sg, *Ev_max_nWire_ME32_sg, *Ev_max_nWire_ME41_sg, *Ev_max_nWire_ME42_sg,
       *Ev_max_nComp_mc, *Ev_max_nWire_mc,
       *Ev_max_nComp_ME1_mc, *Ev_max_nComp_ME2_mc, *Ev_max_nComp_ME3_mc, *Ev_max_nComp_ME4_mc,
       *Ev_max_nWire_ME1_mc, *Ev_max_nWire_ME2_mc, *Ev_max_nWire_ME3_mc, *Ev_max_nWire_ME4_mc,
       *Ev_max_nComp_ME11_mc, *Ev_max_nComp_ME12_mc, *Ev_max_nComp_ME21_mc, *Ev_max_nComp_ME22_mc, *Ev_max_nComp_ME31_mc, *Ev_max_nComp_ME32_mc, *Ev_max_nComp_ME41_mc, *Ev_max_nComp_ME42_mc,
       *Ev_max_nWire_ME11_mc, *Ev_max_nWire_ME12_mc, *Ev_max_nWire_ME21_mc, *Ev_max_nWire_ME22_mc, *Ev_max_nWire_ME31_mc, *Ev_max_nWire_ME32_mc, *Ev_max_nWire_ME41_mc, *Ev_max_nWire_ME42_mc;
      
  TCanvas *c1 = new TCanvas("c1","c1",900,700);
  c1->SetRightMargin(0.09);
  c1->SetLeftMargin(0.15);
  c1->SetBottomMargin(0.15);

  Ev_max_nComp_sg = (TH1D*)fsg->Get("Ev_max_nComp"); histssg.push_back(Ev_max_nComp_sg);
  Ev_max_nComp_mc = (TH1D*)fmc->Get("Ev_max_nComp"); histsmc.push_back(Ev_max_nComp_mc);
  Ev_max_nWire_sg = (TH1D*)fsg->Get("Ev_max_nWire"); histssg.push_back(Ev_max_nWire_sg);
  Ev_max_nWire_mc = (TH1D*)fmc->Get("Ev_max_nWire"); histsmc.push_back(Ev_max_nWire_mc);
  Ev_max_nComp_ME1_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME1"); histssg.push_back(Ev_max_nComp_ME1_sg);
  Ev_max_nComp_ME1_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME1"); histsmc.push_back(Ev_max_nComp_ME1_mc);
  Ev_max_nComp_ME2_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME2"); histssg.push_back(Ev_max_nComp_ME2_sg);
  Ev_max_nComp_ME2_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME2"); histsmc.push_back(Ev_max_nComp_ME2_mc);
  Ev_max_nComp_ME3_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME3"); histssg.push_back(Ev_max_nComp_ME3_sg);
  Ev_max_nComp_ME3_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME3"); histsmc.push_back(Ev_max_nComp_ME3_mc);
  Ev_max_nComp_ME4_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME4"); histssg.push_back(Ev_max_nComp_ME4_sg);
  Ev_max_nComp_ME4_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME4"); histsmc.push_back(Ev_max_nComp_ME4_mc); 
  Ev_max_nWire_ME1_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME1"); histssg.push_back(Ev_max_nWire_ME1_sg);
  Ev_max_nWire_ME1_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME1"); histsmc.push_back(Ev_max_nWire_ME1_mc);
  Ev_max_nWire_ME2_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME2"); histssg.push_back(Ev_max_nWire_ME2_sg);
  Ev_max_nWire_ME2_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME2"); histsmc.push_back(Ev_max_nWire_ME2_mc);
  Ev_max_nWire_ME3_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME3"); histssg.push_back(Ev_max_nWire_ME3_sg);
  Ev_max_nWire_ME3_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME3"); histsmc.push_back(Ev_max_nWire_ME3_mc);
  Ev_max_nWire_ME4_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME4"); histssg.push_back(Ev_max_nWire_ME4_sg);
  Ev_max_nWire_ME4_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME4"); histsmc.push_back(Ev_max_nWire_ME4_mc);
  Ev_max_nComp_ME11_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME11"); histssg.push_back(Ev_max_nComp_ME11_sg);
  Ev_max_nComp_ME11_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME11"); histsmc.push_back(Ev_max_nComp_ME11_mc);
  Ev_max_nComp_ME12_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME12"); histssg.push_back(Ev_max_nComp_ME12_sg);
  Ev_max_nComp_ME12_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME12"); histsmc.push_back(Ev_max_nComp_ME12_mc);
  Ev_max_nComp_ME21_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME21"); histssg.push_back(Ev_max_nComp_ME21_sg);
  Ev_max_nComp_ME21_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME21"); histsmc.push_back(Ev_max_nComp_ME21_mc);
  Ev_max_nComp_ME22_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME22"); histssg.push_back(Ev_max_nComp_ME22_sg);
  Ev_max_nComp_ME22_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME22"); histsmc.push_back(Ev_max_nComp_ME22_mc);
  Ev_max_nComp_ME31_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME31"); histssg.push_back(Ev_max_nComp_ME31_sg);
  Ev_max_nComp_ME31_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME31"); histsmc.push_back(Ev_max_nComp_ME31_mc);
  Ev_max_nComp_ME32_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME32"); histssg.push_back(Ev_max_nComp_ME32_sg);
  Ev_max_nComp_ME32_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME32"); histsmc.push_back(Ev_max_nComp_ME32_mc);
  Ev_max_nComp_ME41_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME41"); histssg.push_back(Ev_max_nComp_ME41_sg);
  Ev_max_nComp_ME41_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME41"); histsmc.push_back(Ev_max_nComp_ME41_mc);
  Ev_max_nComp_ME42_sg = (TH1D*)fsg->Get("Ev_max_nComp_ME42"); histssg.push_back(Ev_max_nComp_ME42_sg);
  Ev_max_nComp_ME42_mc = (TH1D*)fmc->Get("Ev_max_nComp_ME42"); histsmc.push_back(Ev_max_nComp_ME42_mc);
  Ev_max_nWire_ME11_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME11"); histssg.push_back(Ev_max_nWire_ME11_sg);
  Ev_max_nWire_ME11_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME11"); histsmc.push_back(Ev_max_nWire_ME11_mc);
  Ev_max_nWire_ME12_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME12"); histssg.push_back(Ev_max_nWire_ME12_sg);
  Ev_max_nWire_ME12_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME12"); histsmc.push_back(Ev_max_nWire_ME12_mc);
  Ev_max_nWire_ME21_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME21"); histssg.push_back(Ev_max_nWire_ME21_sg);
  Ev_max_nWire_ME21_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME21"); histsmc.push_back(Ev_max_nWire_ME21_mc);
  Ev_max_nWire_ME22_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME22"); histssg.push_back(Ev_max_nWire_ME22_sg);
  Ev_max_nWire_ME22_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME22"); histsmc.push_back(Ev_max_nWire_ME22_mc);
  Ev_max_nWire_ME31_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME31"); histssg.push_back(Ev_max_nWire_ME31_sg);
  Ev_max_nWire_ME31_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME31"); histsmc.push_back(Ev_max_nWire_ME31_mc);
  Ev_max_nWire_ME32_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME32"); histssg.push_back(Ev_max_nWire_ME32_sg);
  Ev_max_nWire_ME32_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME32"); histsmc.push_back(Ev_max_nWire_ME32_mc);
  Ev_max_nWire_ME41_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME41"); histssg.push_back(Ev_max_nWire_ME41_sg);
  Ev_max_nWire_ME41_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME41"); histsmc.push_back(Ev_max_nWire_ME41_mc);
  Ev_max_nWire_ME42_sg = (TH1D*)fsg->Get("Ev_max_nWire_ME42"); histssg.push_back(Ev_max_nWire_ME42_sg);
  Ev_max_nWire_ME42_mc = (TH1D*)fmc->Get("Ev_max_nWire_ME42"); histsmc.push_back(Ev_max_nWire_ME42_mc);

  TLegend * legend = new TLegend(0.7,0.65,1,.75);
  legend->AddEntry(histssg[0],"Zerobias Data","lep");
  legend->AddEntry(histsmc[0],"Signal MC","lep");
  legend->Draw();

  c1->Print("DatavsSignal.pdf[");

  for(int i=0;i<histssg.size();i++){
    histssg[i]->SetLineColor(kBlack);
    histsmc[i]->SetLineColor(kRed);

    //histssg[i]->Scale(histsmc[i]->Integral()/histssg[i]->Integral());

    histssg[i]->Draw();
    histsmc[i]->Draw("SAME");

    legend->Draw();

    gPad->SetLogy();
    c1->Print("DatavsSignal.pdf");
  }

  c1->Print("DatavsSignal.pdf]");

}
