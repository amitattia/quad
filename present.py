#import modules
import gpsP
import scanP
import imgP

#main function
if __name__ == "__main__":
    mode = input('Enter (g|s|i|e)...')
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
            if mode == 'e':
                exit()
        except KeyboardInterrupt:
            print('ctrl+c')
            mode = input('Enter (g|s|i|e)...')
