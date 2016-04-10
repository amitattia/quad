from commandP import *
import time
import sys

try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        # FIXME what to do on other platforms?
        # Just give up here.
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        """getch() -> key character

        Read a single keypress from stdin and return the resulting character. 
        Nothing is echoed to the console. This call will block if a keypress 
        is not already available, but will not wait for Enter to be pressed. 

        If the pressed key was a modifier key, nothing will be detected; if
        it were a special function key, it may return the first character of
        of an escape sequence, leaving additional characters in the buffer.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch



def control():
    bool = input("press d to delay, f to flow")
    if(bool == "d"):
        print("delay mode")
        wait = int(input("enter delay time:"))
        while True:
            try:
                print("press (W|A|S|D), O for up, L for down")
                press = getch()
                if(press == "a"):
                    left()
                    time.sleep(wait)
                elif (press == "w"):
                    forwards()
                    time.sleep(wait)
                elif (press == "s"):
                    backwards()
                    time.sleep(wait)
                elif( press == "d"):
                    right()
                    time.sleep(wait)
                elif(press == "o"):
                    up()
                    time.sleep(wait)
                elif(press == "l"):
                    down()
                    time.sleep(wait)
                
                zero()
        except IOError:
            print('io')
            time.sleep(1)
    else:
        print("flow mode")
        while True:
            try:
                print("press (W|A|S|D), O for up, L for down, Q to stop")
                press = getch()
                if(press == "a"):
                    left()
                elif (press == "w"):
                    forwards()
                elif (press == "s"):
                    backwards()
                elif( press == "d"):
                    right()
                elif(press == "o"):
                    up()
                elif(press == "l"):
                    down()
                elif(press == "q")
                    zero()
        except IOError:
            print('io')
            time.sleep(1)
