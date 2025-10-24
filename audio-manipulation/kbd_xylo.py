import os

if os.name == "posix":
    from boombox import GstBoomBox as BoomBox
else:
    from boombox import BoomBox

from pynput import keyboard


class KeyboardXylophone:


    def __init__(
        self, duration_ms: int = 250, volume: float = 0.1, freq_mul: int = 10
    ) -> None:
        self._boombox = BoomBox("")
        self.duration_ms = duration_ms
        self.volume = volume
        self.freq_mul = freq_mul

    def play_sound(self, frequency: float):
        self._boombox.play_tone(frequency, self.duration_ms, self.volume)

    def on_press(self, key):
        try:
            self.play_sound(ord(key.char) * self.freq_mul)
        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def run(self):
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            listener.join()


if __name__ == "__main__":
    kbdxylo = KeyboardXylophone()
    kbdxylo.run()