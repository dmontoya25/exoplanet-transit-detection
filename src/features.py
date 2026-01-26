import numpy as np
from astropy import units as u
def extract_transit_features(lc_folded, period):
    phase = lc_folded.phase
    flux = lc_folded.flux

    depth = np.abs(np.min(flux) - np.median(flux))

    in_transit = flux < np.median(flux) - 0.5 * depth
    duration_phase = phase[in_transit].max() - phase[in_transit].min()
    duration_days = duration_phase * period

    noise = np.std(flux[~in_transit])
    snr = depth / noise

    return {
        "Period (Days)": float(period),
        "Depth": float(depth),
        "Duration (Days)": duration_days.to(u.day).value,
        "SNR": float(snr),
    }
