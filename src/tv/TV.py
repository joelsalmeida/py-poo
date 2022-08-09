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
        return self.__chanel

    @property
    def screen_size(self):
        return self.__screen_size

    @property
    def on(self):
        return self.__on

    def turn_up_volume(self):
        self.rais_if_off()
        if self.__volume < 99:
            self.__volume += 1

    def turn_down_volume(self):
        self.rais_if_off()
        if self.__volume > 0:
            self.__volume -= 1

    def change_chanel(self, chanel):
        self.rais_if_off()
        if chanel > 99 or chanel < 0:
            raise ValueError('Invalid chanel')

        self.__chanel = chanel

    def turn_on_off(self):
        if self.__on is True:
            self.__on = False
        else:
            self.__on = True

    def rais_if_off(self):
        if self.__on is False:
            raise ValueError('TV is off')
