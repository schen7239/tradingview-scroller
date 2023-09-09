from pynput import keyboard

class KeyboardHandler:
    def __init__(self):
        self.last_key_pressed = None
        self.listener = None
        self.isListenerOn = False
        pass
    def on_key_press(self, key):
        if (key == keyboard.Key.left):
            self.set_last_key_pressed(-1)
        elif(key == keyboard.Key.right):
            self.set_last_key_pressed(1)
        elif(key == keyboard.Key.esc):
            self.set_last_key_pressed("ESCAPE")
        else:
            self.set_last_key_pressed(None)
    def init_listener(self):
        if self.isListenerOn:
            return
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()
        
    def remove_listener(self):
        self.listener.stop()
    
    def get_last_key_pressed(self):
        return self.last_key_pressed
    def set_last_key_pressed(self, val):
        self.last_key_pressed = val