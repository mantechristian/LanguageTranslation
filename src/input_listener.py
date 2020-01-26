import time
from pynput import keyboard
from record_audio import RecordAudio

class InputListener:
    def __init__(self):
        self.recordAudio = RecordAudio()

    # def on_press(self, key):
    #     try:
    #         print('alphanumeric key {0} pressed'.format(
    #             key.char))
    #     except AttributeError:
    #         print('special key {0} pressed'.format(
    #             key))

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        elif key == keyboard.Key.space:
                # Start recording
                # time.sleep(1)
                print('Initiate Audio Recording ...')
                self.recordAudio.start()    
            

if __name__ == "__main__":
    inputListener = InputListener()
    # Collect events until released
    # with keyboard.Listener(
    #         on_press=inputListener.on_press,
    #         on_release=inputListener.on_release) as listener:
    #     listener.join()
    with keyboard.Listener(
            on_release=inputListener.on_release) as listener:
        try:
            listener.join()
        except MyException as e:
            print('{0} was pressed'.format(e.args[0]))