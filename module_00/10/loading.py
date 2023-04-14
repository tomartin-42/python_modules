from time import sleep
import sys

def ft_progress(lst):
    for val in lst:
        percent = int(100 * (val / len(lst)) + 1
        partial = str(val + 1) + '/' + str(lst)  
        leng = 20 * val // lst
        bar = '=' * leng
        bar += '>'
        bar += ' ' * (20 - leng)  
        resp = f'\rProgreso:| {bar}| {partial} '
        print(resp, end = str(percent))
        yield val
    
def launch(l = 2000):
    for i in ft_progress(l):
        sleep(0.002)

if __name__ == '__main__':
    try:
        launch(int(sys.argv[1]))
    except:
        launch()
