import ugradio
import numpy as np

SAMPLE_RATES = np.arange(1.0e6, 3.2e6, 1e5)
for SAMPLE_RATE in SAMPLE_RATES:
    sdr = ugradio.sdr.SDR(sample_rate = SAMPLE_RATE, direct=False, center_freq=25e6)
    _ = sdr.capture_data(nblocks=1)
    data = sdr.capture_data(nblocks=100)
    sdr.close()
    np.savez(f"real_mixer_data/{SAMPLE_RATE}7.3.3_0.04a_diff_freq_data.npz", data)
