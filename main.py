import time
from threading import Thread, Lock
import sys
from colorama import init, Fore, Style

# Initialize colorama
init()

# Create a lock object to synchronize thread output
lock = Lock()

def animate_text(text, delay=0.1, color=Fore.WHITE):
    with lock:
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print(Style.RESET_ALL)

def sing_lyric(lyric, start_delay, char_delay, color):
    time.sleep(start_delay)
    animate_text(lyric, char_delay, color)

def sing_song():
    """
    Coordinates the singing of the song with multiple lyrics.
    """
    lyrics = [
        ("I just wanna see", 0.1, Fore.LIGHTMAGENTA_EX), 
        ("I just wanna see how beautiful you are", 0.14, Fore.LIGHTMAGENTA_EX),
        ("You know that I see it", 0.11, Fore.LIGHTMAGENTA_EX),
        ("I know you're a star", 0.13, Fore.LIGHTMAGENTA_EX),
        ("Where you go I follow", 0.10, Fore.LIGHTMAGENTA_EX),
        ("No matter how far", 0.14, Fore.LIGHTMAGENTA_EX),
        ("If life is a movie", 0.1, Fore.LIGHTMAGENTA_EX),
        ("Oh you're the best part, oh oh oh", 0.1, Fore.LIGHTMAGENTA_EX),
        ("You're the best part, oh oh oh, oh oh oh", 0.1, Fore.LIGHTMAGENTA_EX),
        ("Best part", 0.1, Fore.LIGHTMAGENTA_EX)
    ]
    delays = [0.3, 1.0, 8.1, 11.5, 15.1, 17.6, 21.0, 24.5, 31.0, 38.0]

    threads = []
    for i in range(len(lyrics)):
        lyric, char_delay, color = lyrics[i]
        start_delay = delays[i]
        t = Thread(target=sing_lyric, args=(lyric, start_delay, char_delay, color))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
