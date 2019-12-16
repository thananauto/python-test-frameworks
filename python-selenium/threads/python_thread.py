import threading
from oops.User import Admin, Office
class python_thread(threading.Thread):

    def __init__(self, object):
        self.__object = object
        threading.Thread.__init__(self)


    def run(self):
        self.__object.programming()


if __name__ == '__main__':

    list = [Admin('Mani'), Office('Falton')]

    for objet in list:
        python_thread(objet).start()

