from PySide2.QtCore import Signal


class MediaPlayer:
    def __init__(self):
        self.a = 1
        self.b = 2


class MediaPlayer2:
    def __new__(cls, *args, **kwargs):
        cls.a = -1
        cls.b = -2
        return cls


class QMP(MediaPlayer):
    vol = Signal(int)
    delta_time = Signal(int)

    def __init__(self):
        super().__init__()
        self.player = MediaPlayer()
        self.time = 0


class QMP2(MediaPlayer2):
    vol = Signal(int)
    delta_time = Signal(int)

    def __init__(self):
        super().__new__(self)
        self.player = MediaPlayer()
        self.time = 0

