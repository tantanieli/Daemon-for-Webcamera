from kurs_daemon import Daemon
import os
import sys
import subprocess
import time

TAKE_PHOTO_CMD = "avconv -f video4linux2 -i /dev/video0 -vframes 1 {0}/{1}.jpeg"
INTERVAL = 30
PATH = "/tmp"
PIDFILE = "/tmp/kursach.pid"

class MyDaemon(Daemon):
    def run(self):
        while True:
            subprocess.Popen(TAKE_PHOTO_CMD.format(PATH, str(time.time())).split(),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL)
            time.sleep(INTERVAL)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["start", "stop", "status"]:
        print("Usage: python main.py start|stop|status")
        sys.exit(1)
    kursach = MyDaemon(PIDFILE)
    if sys.argv[1] == "start":
        kursach.start()
    elif sys.argv[1] == "stop":
        kursach.stop()
    elif sys.argv[1] == "status":
        if os.path.isfile(PIDFILE):
            pidfile = open(PIDFILE, "r")
            pid = pidfile.read()
            print("Daemon is running on PID {0}".format(pid))
        else:
            print("Daemon is not running yet")
