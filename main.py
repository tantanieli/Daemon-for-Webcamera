from kurs_daemon import Daemon
import sys
import subprocess
import time

TAKE_PHOTO_CMD = "avconv -f video4linux2 -i /dev/video0 -vframes 1 {0}/{1}.jpeg"
INTERVAL = 30
PATH = "/tmp"

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
    kursach = MyDaemon("/tmp/kursach.pid")
    if sys.argv[1] == "start":
        kursach.start()
    elif sys.argv[1] == "stop":
        kursach.stop()
