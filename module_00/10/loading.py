import time
import sys

def ft_progress(lst):
    for val in lst:
        progress_b = "EAT: "

        #init time
        if lst.index(val) == 0:
            start_time = time.time()

        #calculate and print partial time
        partial_time = time.time() - start_time
        expect_time = partial_time  * (len(lst) / (lst.index(val) + 1) - 1)
        progress_b += "{:.2f}s".format(expect_time) 

        #percentage
        progress_b += " ["
        progress_b += str(int((lst.index(val)/len(lst) * 100) + 1)).rjust(3) + "%"
        progress_b += "]"

        #bar
        progress_b += "["
        lines = (lst.index(val) * 20 // len(lst))
        for i in range(lines):
            progress_b += "="
        progress_b += ">"
        for i in range(lines, 19):
            progress_b += " "
        progress_b += "] "

        #remainder
        progress_b += f"{lst.index(val) + 1}/{len(lst)}"
        progress_b += " | "
        progress_b += f"elapsed time: {(time.time() - start_time):.2f}s"
        sys.stdout.write("\033[?25l")
        print("\r", progress_b, end="")
        yield val
    sys.stdout.write("\033[?25h")

if __name__ == '__main__':
    listy = range(333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.08)
    print()
    print(ret)
