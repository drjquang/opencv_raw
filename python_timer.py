from threading import Timer, Thread, Event


class PerpetualTimer:
    def __init__(self, time_interval, my_function):
        self.time_interval = time_interval
        self.my_function = my_function
        self.thread = Timer(self.time_interval, self.handle_function)

    def handle_function(self):
        self.my_function()
        self.thread = Timer(self.time_interval, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def do_cmd():
    print("This function is activated.\n")


t = PerpetualTimer(2.5, do_cmd)
t.start()
while True:
    key_stroke = input()
    if key_stroke == ord('q'):
        t.cancel()
        break
