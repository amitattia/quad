#import modules
import gpsP
import scanP

#main function
if __name__ == "__main__":
    mode = input('Enter (g|s|i|e)...')
    while True:
        try:
            if mode == 'g':
                gpsP.gpsNavigation()
            if mode == 's':
                scanP.scanArea()
            if mode == 'i':
                print('empty')
            if mode == 'e':
                exit()
        except KeyboardInterrupt:
            print('ctrl+c')
            mode = input('Enter (g|s|i|e)...')
