#import modules
import gpsP
import scanP
import imgP

#main function
if __name__ == "__main__":
    mode = input('Enter (g|s|i|d|m|e)...')
    while True:
        try:
            if mode == 'g':
                gpsP.gpsNavigation()
            if mode == 's':
                tmp = scanP.scanArea()
                if tmp == False:
                    input('Scan failed')
            if mode == 'i':
                imgP.navigateImg()
            if mode == 'd':
                drop.drop()
            if mode == 'm':
                control.control()
            if mode == 'e':
                exit()
        except KeyboardInterrupt:
            print('ctrl+c')
            mode = input('Enter (g|s|i|d|e)...')
