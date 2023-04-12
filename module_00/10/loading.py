from time import sleep
import sys

def ft_progress(lst):
    it = 0
    while it < lst:
        percent = int(100 * (it / lst)) + 1
        partial = str(it + 1) + '/' + str(lst)  
        leng = 20 * it // lst
        bar = '=' * leng
        bar += '>'
        bar += ' ' * (20 - leng)  
        resp = f'\rProgreso:| {bar}| {partial} '
        print(resp, end = str(percent))
        it += 1
        yield lst
    
def launch(l = 2000):
    for i in ft_progress(l):
        sleep(0.002)

if __name__ == '__main__':
    try:
        launch(int(sys.argv[1]))
    except:
        launch()
