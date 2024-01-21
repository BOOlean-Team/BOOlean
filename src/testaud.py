from audioplayer import AudioPlayer

def play_test_sound(file_path):
    try:
        player = AudioPlayer(file_path)
        player.play(block=True)
        print("Sound playback finished.")
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    # Replace 'your_test_sound.wav' with the actual filename of your test sound.
    test_sound_file = "assets/squeak.wav"

    print(f"Playing test sound: {test_sound_file}")
    play_test_sound(test_sound_file)