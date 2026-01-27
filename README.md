# Exoplanet Transit Detection with Kepler Data

This project implements a complete pipeline for detecting exoplanet transits
from Kepler light curve data, and is readily applicable to other space-based photometric missions such as TESS.

The workflow combines classical astrophysical signal processing and statistical methods, including light curve cleaning, transit feature extraction, periodic transit detection using the Box Least Squares (BLS) algorithm, and result interpretation.

---

## 📌 Project Overview

Exoplanet transits appear as periodic dips in stellar brightness when a planet
passes in front of its host star. Detecting these signals requires careful
preprocessing and robust period-search algorithms.

This project demonstrates:
- Light curve exploration and normalization
- Transit feature extraction
- Period detection using Box Least Squares (BLS)
- Phase-folded visualization of detected transits

