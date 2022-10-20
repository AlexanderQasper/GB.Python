from time import sleep
from datetime import datetime as dt


class Traffic_Light:
    """ Класс светофора, реализующий свое переключение при запуске running( """
    _states = {'red': 7, 'yellow': 2, 'green': 6}
    _colour = None

    def running(self):
        for colour, sw_time in self._states.items():
            self._colour = colour
            start_state_time = dt.now()

            print(f"TrafficLight switched to state '{self._colour}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"TrafficLight leave state '{self._colour}' after "
                  f"{(dt.now() - start_state_time).seconds} seconds")

Traffic_Light().running()
