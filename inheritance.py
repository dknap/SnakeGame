class Animal:
    def __init__(self):
        self.eyes_num = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water")


nemo = Fish()
nemo.breathe()