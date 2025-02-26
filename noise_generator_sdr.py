import ugradio
import numpy as np
SAMPLE_RATES = np.arange(1e6, 3.3e6, 1e5)
for SAMPLE_RATE in SAMPLE_RATES:
    sdr = ugradio.sdr.SDR(sample_rate = SAMPLE_RATE,fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]))
    _ = sdr.capture_data(nblocks=1)
    data = sdr.capture_data(nblocks=100)
    sdr.close()
    np.savez(f"noise_generator_data/{SAMPLE_RATE}_noise_generator_data.npz", data)
