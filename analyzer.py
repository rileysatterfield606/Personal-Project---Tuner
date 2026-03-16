import copy
import pyaudio
import wave
import sys
from threading import Thread
import numpy as np
from queue import Queue

class note_analyzer(Thread): 
    """ This class is going to record and find the frequency of 
    the note that is the loudest. """

    # Settings 👅
    SAMPLING_RATE = 44100
    CHUNK_SIZE = 1024
    THRESHOLD = 300
    
    
        
        # I don't know if I need the octave here but it might be useful for later so I'm just gonna leave it in
    def __init__(self, queue):
        super().__init__()
        # This is the queue that the main thread will use to get the note name and cents off from the analyzer thread
        self.queue = queue 
        self.running = True

    def run(self): # ts actaully has to be called run for the thread to work- thread actually looks for a method called run and executes that on the new thread
        # Yay now it will record and analyze 
        p = pyaudio.PyAudio() # even in the documentation it is jst p
        stream = p.open(
            rate=self.SAMPLING_RATE,
            channels=1,
            input=True,
            frames_per_buffer=self.CHUNK_SIZE,
            format= pyaudio.paInt16
            )
        
        while self.running:
            raw = stream.read(self.CHUNK_SIZE, exception_on_overflow=False) # Exception on overflow is basically like if you fall behind don't crash
            data = np.frombuffer(raw, dtype=np.int16) # Convert the raw audio data to a numpy array cause python can't do it itself
            if np.max(np.abs(data)) < self.THRESHOLD: # Ok basicallly if you are playing smth then make #s pos, find loudest, if it is not withing threshold then its background
                continue
            
            # Now comes the important signal processing stuff- we gotta use FFT
            fft = np.fft.rfft(data * np.hanning(len(data))) # Creates a window/ smooth curve to fade the edges of audio chunk to zero, also lowk runs FAST FOURIER TRANSFORM which breaks audio chunks aaprt into frequencies
            freqs = np.fft.rfftfreq(len(data), 1/ self.SAMPLING_RATE) # List of magnitudes that generates matching list of freqs into hz
            dominant_freq = freqs[np.argmax(np.abs(fft))] # Find the index of the max magnitude in the FFT and get the corresponding frequency from the freqs list
            self.queue.put(dominant_freq) # Put our frequency into the queue 
    
