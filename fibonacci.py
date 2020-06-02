import threading, time

class Threads(threading.Thread):

    Ergebnis = [0,1]

    def __init__(self, id, name):

        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):

        i = 0
        
        while i < 20:

            zahl = Threads.Ergebnis[len(Threads.Ergebnis)-2] + Threads.Ergebnis[len(Threads.Ergebnis)-1]
            lockMe.acquire()
            Threads.Ergebnis.append(zahl)
            lockMe.release()
            i += 1

lockMe = threading.Lock()
t1 = Threads(1, "t1")
t2 = Threads(2, "t2")
t3 = Threads(3, "t3")
t4 = Threads(4, "t4")
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()


print(Threads.Ergebnis[80])



