// cdet_nearest_sim.C
// ROOT macro: simulate random CDet hits in 2 layers and plot nearest-x matches
//
// Usage:
//   root -l
//   .x cdet_nearest_sim.C
//   // or call with custom args:
//   simulateCDetNearest(500, 250, 0);

#include <algorithm>
#include <vector>
#include <cmath>
#include <iostream>

#include "TRandom3.h"
#include "TH2D.h"
#include "TH1D.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TGraph.h"
#include "TLine.h"

static inline double paddle_center_x_m(int side, int paddle, double halfSpan_m, int paddlesPerSide)
{
  // side: -1 for left, +1 for right
  // paddle: 0..(paddlesPerSide-1)
  // halfSpan_m: 1.68 m
  // pitch is derived from span / paddlesPerSide
  const double pitch = halfSpan_m / paddlesPerSide; // meters
  const double x_local = (paddle + 0.5) * pitch;    // 0..halfSpan
  return side * x_local;                            // negative on left, positive on right
}

static inline double nearest_in_sorted(const std::vector<double>& xs_sorted, double x)
{
  // assumes xs_sorted non-empty and sorted
  auto it = std::lower_bound(xs_sorted.begin(), xs_sorted.end(), x);

  if (it == xs_sorted.begin()) return *it;
  if (it == xs_sorted.end())   return xs_sorted.back();

  double hi = *it;
  double lo = *(it - 1);
  return (std::fabs(x - lo) <= std::fabs(hi - x)) ? lo : hi;
}

void simulateCDetNearest(int nevents=1000, int nL1 = 500, int nL2 = 250, unsigned long seed = 0)
{
  // Geometry from your description
  const int paddlesPerLayer   = 1344;
  const int paddlesPerSide    = 672;   // left + right
  const double halfSpan_m     = 1.68;  // layer spans -1.68 m to +1.68 m
  const double xMin = -halfSpan_m;
  const double xMax = +halfSpan_m;

  // RNG
  TRandom3 rng;
  if (seed == 0) rng.SetSeed(0);  // ROOT chooses a time-dependent seed
  else           rng.SetSeed(seed);
  
  const int nb = 240; // binning for both axes (tweak as you like)
  TH2D* hMatch = new TH2D("hMatch",
                         "Nearest-x match: Layer 1 vs Layer 2; x_{L1} (m); x_{L2, nearest} (m)",
                         nb, xMin, xMax,
                         nb, xMin, xMax);

  for (int j=0;j<nevents;j++) {

  // Generate hits: store x positions (meters)
  std::vector<double> x1; x1.reserve(nL1);
  std::vector<double> x2; x2.reserve(nL2);

  auto gen_hit_x = [&]() -> double {
    int side   = (rng.Rndm() < 0.5) ? -1 : +1;              // left/right 50/50
    int paddle = rng.Integer(paddlesPerSide);               // 0..671
    return paddle_center_x_m(side, paddle, halfSpan_m, paddlesPerSide);
  };

  for (int i = 0; i < nL1; i++) x1.push_back(gen_hit_x());
  for (int i = 0; i < nL2; i++) x2.push_back(gen_hit_x());

  // Sort layer-2 hits for fast nearest-neighbor lookup
  std::sort(x2.begin(), x2.end());

  // Prepare plot objects
  gStyle->SetOptStat(0);

  // Optional: also keep the actual point list (for a true scatter draw)
  std::vector<double> gx, gy;
  gx.reserve(nL1);
  gy.reserve(nL1);

  // Fill: for each layer-1 hit, find nearest in layer 2
  for (int i = 0; i < (int)x1.size(); i++) {
    double xL1 = x1[i];
    double xL2 = nearest_in_sorted(x2, xL1);
    hMatch->Fill(xL1, xL2);
    gx.push_back(xL1);
    gy.push_back(xL2);
  }

  } // end event loop

  // Draw
  TCanvas* c = new TCanvas("c_cdet_nearest", "CDet nearest-x simulation", 900, 700);

  // Option A: density-style (looks good if some bins get multiple hits)
  hMatch->Draw("COLZ");

  // Option B: true scatter overlay (uncomment if you want points)
  // TGraph* gr = new TGraph((int)gx.size(), gx.data(), gy.data());
  // gr->SetMarkerStyle(20);
  // gr->SetMarkerSize(0.5);
  // gr->Draw("P SAME");

  // Helpful diagonal reference line y=x
  TLine* diag = new TLine(xMin, xMin, xMax, xMax);
  diag->SetLineStyle(2);
  diag->Draw("SAME");

  c->Update();

  std::cout << "Generated " << nL1 << " hits in L1 and " << nL2
            << " hits in L2. Filled " << nL1 << " nearest-neighbor pairs.\n";
}
