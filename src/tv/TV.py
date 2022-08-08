class TV:
    def __init__(self, screen_size):
        self.__volume = 50
        self.__chanel = 1
        self.__screen_size = screen_size
        self.__on = False

    @property
    def volume(self):
        return self.__volume

    @property
    def chanel(self):
        return self.__volume

    @chanel.setter
    def chanel(self, new_chanel):
        self.__chanel = new_chanel

    @property
    def screen_size(self):
        return self.__screen_size

    @property
    def on(self):
        return self.__on

    @on.setter
    def on(self, on_status):
        self.__on = on_status

    def turn_up_volume(self):
        if self.__volume < 99:
            self.__volume += 1

    def turn_down_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
