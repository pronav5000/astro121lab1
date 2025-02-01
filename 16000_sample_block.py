import ugradio
import numpy as np

SAMPLE_RATE = 1e6
sdr = ugradio.sdr.SDR(sample_rate = SAMPLE_RATE, fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]))
_ = sdr.capture_data(nblocks=1)
data = sdr.capture_data(nsamples=16000, nblocks=1)
sdr.close()
np.savez(f"noise_generator_data/{SAMPLE_RATE}_16000_data.npz", data)
