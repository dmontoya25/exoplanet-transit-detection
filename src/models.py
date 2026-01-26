
def classify_transit(features):
    if (
        features["Depth"] > 0.005 and
        features["SNR"] > 7 and
        features["Duration (Days)"] < 1.0
    ):
        return "Likely Exoplanet Transit"
    else:
        return "Unlikely / Noise"
