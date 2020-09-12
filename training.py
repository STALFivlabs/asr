#training function for ASR
from Feature_Extract_LPC import lpc
from Feature_Match_LBG import lbg_codebook

from scipy.io.wavfile import read
import numpy as np

def train(no_filtbank, orderLPC, name, no_centroids, model_type):
    directory = 'train'
    codebook = np.empty((no_centroids, orderLPC))#the main codebook vector

    fname = '\\' + name + '_2.wav'
    print ("Now", name+"\'s features are being trained")
    (fs,s) = read(directory + fname) #for each file, read() returns a tuple. The first one is samples/second (sample rate) and second is the actual data read from the audio file
    if(model_type=='lpc'):
        coeff = lpc(s, fs, orderLPC)
    elif(model_type=='lpcc'):
        lpc_coeff = lpc(s, fs, orderLPC)
        coeff = lpcc(lpc_coeff)
    else:
        print("Invalid model type! Model type should be 'mfcc' or 'lpc'.")
        exit()
        
    codebook = lbg_codebook(coeff, no_centroids) #features passed to lbg are the LPC for current speaker.
    print ("Training complete\n")

    return codebook
