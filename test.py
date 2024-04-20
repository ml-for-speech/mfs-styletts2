from txtsplit import txtsplit
from openphonemizer import OpenPhonemizer
import torch
import numpy as np
from scipy.io.wavfile import write

phonemizer = OpenPhonemizer()

from mfs_styletts2.lj import LFinference

text = "Hello this is a test"

device = "cpu"

sentences = txtsplit(phonemizer(text))
wavs = []
s_prev = None
for text in sentences:
    if text.strip() == "":
        continue
    text += "."  # add it back
    noise = torch.randn(1, 1, 256).to(device)
    wav, s_prev = LFinference(
        text,
        s_prev,
        noise,
        alpha=0.7,
        diffusion_steps=10,
        embedding_scale=1.1,
        phonemize=False,
    )
    wavs.append(wav)
write("out.wav", 24000, np.concatenate(wavs))
