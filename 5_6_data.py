import ugradio
import numpy as np

SAMPLE_RATE = 1e6
sdr=ugradio.sdr.SDR(sample_rate=SAMPLE_RATE, fir_coeffs=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]))
_=sdr.capture_data(nblocks=1)
data=sdr.capture_data(nblocks=100)
sdr.close()
np.savez("sdr_data/sdr_nw4_data.npz", data)
