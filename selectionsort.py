import time

def selectionSort(data, draw_bars, timeDelay):
    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            draw_bars(data, ["#003153" if x == j or x == min_idx else "#00FCEA" for x in range(len(data))])
            time.sleep(float(timeDelay))  # setting delay according to speed value
        
        # Swap the found minimum element with the first element
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_bars(data, ["#003153" if x == i or x == min_idx else "#00FCEA" for x in range(len(data))])
        time.sleep(float(timeDelay))  # setting delay according to speed value
    
    draw_bars(data, ['#003153' for i in range(len(data))])

