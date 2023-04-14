from loading import ft_progress
import time

def int_bar(x):
    for i in ft_progress(range(x)):
        time.sleep(0.02)

int_bar(100)