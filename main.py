from analyzer import note_analyzer
from utils import frequency_to_note_name
from queue import Queue


# NOW WE PUT IT TOGETHER
freq_queue = Queue() # Create a queue for communication between threads
analyzer = note_analyzer(freq_queue) # Create an instance of the note analyzer
analyzer.start() # START IT

print("RECORDING")

try: 

    while True:
        freqs = freq_queue.get() # Get the frequencies from the analyzer thread
        note_name, cents_off = frequency_to_note_name(freqs) # Convert frequency to note name and cents off
        if freqs is not None:
            if abs(cents_off) < 10:
                tuned = "IN TUNE"
            elif cents_off > 0:
                tuned = "SHARP"
            else:
                tuned = "FLAT"
            print(f"NOTE: {note_name}, CENTS OFF: {cents_off:.2f}, TUNING: {tuned}")

except KeyboardInterrupt:
    print("\n STOPPING")
