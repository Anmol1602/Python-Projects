import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import datetime
import os
import simpleaudio as sa

# Set sampling frequency
fs = 16000

# Get duration from user
second = int(input("Enter time duration in seconds: "))

# Get user preference for mono or stereo
channels = int(input("Enter number of channels (1 for mono, 2 for stereo): "))

# Record audio
print("Recording...\n")
record_voice = sd.rec(int(second * fs), samplerate=fs, channels=channels)
sd.wait()
print("Recording finished.")

# Check the maximum amplitude
max_val = np.max(np.abs(record_voice))
print("Max amplitude in recorded data:", max_val)

# Get current timestamp for file naming
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_filename = f"output_{timestamp}.wav"

# Normalize the audio if max amplitude is very low
if max_val > 0.00001:  # Threshold to avoid amplifying noise
    record_voice = record_voice / max_val *20
    output_filename = f"output_normalized_{timestamp}.wav"
    print("Audio normalized due to low amplitude.")

# Save the recorded audio to a file
write(output_filename, fs, record_voice)
print(f"Finished. Your output file is saved as: {output_filename}")

# Optional: Play the recorded audio
playback = input("Would you like to play the recorded audio? (yes/no): ")
if playback.lower() == "yes":
    wave_obj = sa.WaveObject.from_wave_file(output_filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Provide feedback on the saved file location
file_path = os.path.abspath(output_filename)
print(f"Recording saved at: {file_path}")
