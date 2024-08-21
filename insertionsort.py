import time

def insertionSort(data, draw_bars, timeDelay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_bars(data, ["#003153" if x == j or x == j+1 else "#00FCEA" for x in range(len(data))])
            time.sleep(float(timeDelay))  # setting delay according to speed value
        
        data[j + 1] = key
        draw_bars(data, ["#003153" if x == i or x == j+1 else "#00FCEA" for x in range(len(data))])
        time.sleep(float(timeDelay))  # setting delay according to speed value
    
    draw_bars(data, ['#003153' for i in range(len(data))])

