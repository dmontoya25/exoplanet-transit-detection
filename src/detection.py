from astropy.timeseries import BoxLeastSquares
import numpy as np
import lightkurve as lk

def download_lightcurve(target, mission="Kepler"):
    search_result = lk.search_lightcurve(target, mission=mission)
    lc = search_result[0].download()
    return lc



def run_bls(time, flux, min_period=1.0, max_period=10.0):
    time = np.asarray(time, dtype=float)
    flux = np.asarray(flux, dtype=float)

    bls = BoxLeastSquares(time, flux)

    periods = np.linspace(min_period, max_period, 5000)
    durations = np.linspace(0.05, 0.3, 10)  # days

    results = bls.power(periods, durations)
    best_idx = np.argmax(results.power)

    return {
        "best_period": results.period[best_idx],
        "t0": results.transit_time[best_idx],
        "power": results.power[best_idx],
        "results": results,
    }
