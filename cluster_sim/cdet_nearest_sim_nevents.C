// cdet_nearest_sim_events.C
//
// Simulate multiple events of CDet hits in two layers.
// For each Layer-1 hit, find nearest Layer-2 hit in x.
// Fill:
//   (1) TH2D: x_L1 vs x_L2
//   (2) TH1D: x_L1 - x_L2
//
// Usage:
//   root -l
//   .x cdet_nearest_sim_events.C
//   // or
//   simulateCDetNearestEvents(1000, 500, 250, 0);

#include <algorithm>
#include <vector>
#include <cmath>
#include <iostream>

#include "TRandom3.h"
#include "TH2D.h"
#include "TH1D.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLine.h"

static inline double paddle_center_x_m(int side,
                                      int paddle,
                                      double halfSpan_m,
                                      int paddlesPerSide)
{
  const double pitch = halfSpan_m / paddlesPerSide;   // meters
  const double xloc  = (paddle + 0.5) * pitch;
  return side * xloc;
}

static inline double nearest_in_sorted(const std::vector<double>& xs, double x)
{
  auto it = std::lower_bound(xs.begin(), xs.end(), x);

  if (it == xs.begin()) return *it;
  if (it == xs.end())   return xs.back();

  double hi = *it;
  double lo = *(it - 1);
  return (std::fabs(x - lo) <= std::fabs(hi - x)) ? lo : hi;
}

void simulateCDetNearestEvents(int nevents = 1000,
                               int nL1 = 500,
                               int nL2 = 250,
                               unsigned long seed = 0)
{
  // Geometry
  const int    paddlesPerSide = 672;
  const double halfSpan_m    = 1.68;
  const double xMin = -halfSpan_m;
  const double xMax = +halfSpan_m;

  // RNG
  TRandom3 rng;
  rng.SetSeed(seed == 0 ? 0 : seed);

  gStyle->SetOptStat(0);

  // Histograms
  const int nb = 240;

  TH2D* hXY = new TH2D("hXY",
    "Nearest-x match; x_{Layer 1} (m); x_{Layer 2} (m)",
    nb, xMin, xMax,
    nb, xMin, xMax);

  TH1D* hDX = new TH1D("hDX",
    "x_{Layer 1} - x_{Layer 2}; #Delta x (m); Counts",
    200, -0.25, 0.25);

  // Lambda to generate one hit x-position
  auto gen_hit_x = [&]() {
    int side   = (rng.Rndm() < 0.5) ? -1 : +1;
    int paddle = rng.Integer(paddlesPerSide);
    return paddle_center_x_m(side, paddle, halfSpan_m, paddlesPerSide);
  };

  // =======================
  // Event loop
  // =======================
  for (int ev = 0; ev < nevents; ev++) {

    std::vector<double> x1, x2;
    x1.reserve(nL1);
    x2.reserve(nL2);

    for (int i = 0; i < nL1; i++) x1.push_back(gen_hit_x());
    for (int i = 0; i < nL2; i++) x2.push_back(gen_hit_x());

    std::sort(x2.begin(), x2.end());

    for (double xL1 : x1) {
      double xL2 = nearest_in_sorted(x2, xL1);
      hXY->Fill(xL1, xL2);
      hDX->Fill(xL1 - xL2);
    }
  }

  // =======================
  // Plotting
  // =======================
  TCanvas* c = new TCanvas("c_cdet",
                           "CDet nearest-hit simulation",
                           1200, 600);
  c->Divide(2,1);

  // Left: 2D scatter/density
  c->cd(1);
  hXY->Draw("COLZ");

  TLine* diag = new TLine(xMin, xMin, xMax, xMax);
  diag->SetLineStyle(2);
  diag->Draw("SAME");

  // Right: Delta-x
  c->cd(2);
  hDX->Draw();

  c->Update();

  std::cout << "Simulated " << nevents << " events\n"
            << "Total nearest-neighbor pairs filled: "
            << nevents * nL1 << std::endl;
}
