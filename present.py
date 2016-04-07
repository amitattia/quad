#import modules
import gpsP

#main function
if __name__ == "__main__":
    mode = input('Enter (g|s|i|e)...')
    while True:
        try:
            if mode == 'g':
                print('empty')
            if mode == 's':
                print('empty')
            if mode == 'i':
                print('empty')
            if mode == 'e':
                print('empty')
        except KeyboardInterrupt:
            print('ctrl+c')
            mode = input('Enter (g|s|i|e)...')
