from audioplayer import AudioPlayer
import threading

AUDIO_SQUEAK = "assets/squeak.wav"


class AudioManager:
    def play_sound(self, file_path):
        player = AudioPlayer(file_path)
        player.play(block=True)


# try:
#     audio_manager = AudioManager()
#     audio_manager.play_sound(AUDIO_SQUEAK)
#     print("Sound played successfully.")
# except Exception as e:
#     print(f"Error playing sound: {e}")
