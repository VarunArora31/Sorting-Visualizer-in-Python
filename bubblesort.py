import time

def bubbleSort(data, draw_bars, timeDelay):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_bars(data, ["#003153" if x == j or x == j+1 else "#00FCEA" for x in range(len(data))])
                time.sleep(float(timeDelay)) #setting delay according to speed value
    draw_bars(data,['#003153' for i in range(len(data))])