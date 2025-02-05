import ugradio
import numpy as np

required_rates = [2*1170000,2*1230000]
additional_rates = np.arange(2.5e6, 3.3e6, 1e5)
SAMPLE_RATES = np.sort(np.array(required_rates+list(additional_rates)))
for SAMPLE_RATE in SAMPLE_RATES:
    sdr = ugradio.sdr.SDR(sample_rate = SAMPLE_RATE,fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]))
    _ = sdr.capture_data(nblocks=1)
    data = sdr.capture_data(nblocks=100)
    sdr.close()
    np.savez(f"mixer_data/{SAMPLE_RATE}_sum_freq_data.npz", data)
