import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import datetime
import os
import cv2
import pyautogui
import threading
import queue
from moviepy.editor import VideoFileClip, AudioFileClip

# Set sampling frequency for audio
fs = 16000

# Ensure directories exist
os.makedirs("audio_files", exist_ok=True)
os.makedirs("screen_files", exist_ok=True)
os.makedirs("final_files", exist_ok=True)


# Function to record audio
def record_audio(duration, channels, result_queue):
    print("Recording audio...\n")
    record_voice = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    print("Audio recording finished.")

    # Check the maximum amplitude
    max_val = np.max(np.abs(record_voice))
    print("Max amplitude in recorded data:", max_val)

    # Normalize the audio if max_val is very low
    if max_val > 0.00001:  # Threshold to avoid amplifying noise
        record_voice = record_voice / max_val * 0.5  # Adjust the multiplier as needed
        output_filename = f"audio_files/output_normalized_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"
        print("Audio normalized due to low amplitude.")
    else:
        output_filename = f"audio_files/output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"

    # Save the recorded audio to a file
    write(output_filename, fs, record_voice)
    print(f"Audio saved as: {output_filename}")

    # Store the result in the queue
    result_queue.put(output_filename)


# Function to record screen
def record_screen(duration, output_filename="screen_recording.mp4"):
    print("Recording screen...\n")
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, screen_size)

    start_time = datetime.datetime.now()
    while (datetime.datetime.now() - start_time).seconds < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    out.release()
    print(f"Screen recording finished. Video saved as {output_filename}")

    return output_filename


# Function to combine audio and video
def combine_audio_video(video_filename, audio_filename, output_filename):
    print(f"Combining {video_filename} and {audio_filename} into {output_filename}...")
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)

    # Set audio of the video
    final_video = video_clip.set_audio(audio_clip)

    # Write the final video file
    final_video.write_videofile(output_filename, codec="libx264")
    print(f"Combined video saved as: {output_filename}")


# Main function to run both audio and screen recording simultaneously
def main():
    duration = int(input("Enter recording duration in seconds: "))
    channels = int(input("Enter number of channels (1 for mono, 2 for stereo): "))

    # Queue to get the result from the audio thread
    result_queue = queue.Queue()

    # Start audio recording in a separate thread
    audio_thread = threading.Thread(
        target=record_audio, args=(duration, channels, result_queue)
    )
    audio_thread.start()

    # Start screen recording in the main thread
    screen_output_filename = f"screen_files/screen_recording_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"
    screen_output_filename = record_screen(
        duration, output_filename=screen_output_filename
    )

    # Wait for audio recording to finish
    audio_thread.join()

    # Get the correct audio filename from the queue
    audio_filename = result_queue.get()

    # Combine the audio and video into a single file
    final_output_filename = f"final_files/final_recording_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"
    combine_audio_video(screen_output_filename, audio_filename, final_output_filename)

    print("Both screen and audio recordings are complete.")


if __name__ == "__main__":
    main()
