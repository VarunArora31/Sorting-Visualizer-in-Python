import time
def partitions(data, head, tail, drawData, timeDelay):
    border = head 
    pivot =  data[tail]
    
    drawData(data, colorarray(len(data), head, tail, border, border) )
    time.sleep(timeDelay)
    
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, colorarray(len(data), head, tail, border, j, True) )
            time.sleep(timeDelay)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, colorarray(len(data), head, tail, border, j, True) )
        time.sleep(timeDelay)
    
    drawData(data, colorarray(len(data), head, tail, border, tail, True))
    data[border], data[tail] =  data[tail], data[border]
    return border

def quickSort(data, head, tail, draw_bar, timeDelay):
    if(head< tail) :   
        partitions_index = partitions(data, head, tail, draw_bar, timeDelay)

        quickSort(data, head, partitions_index-1, draw_bar, timeDelay)
        
        quickSort(data, partitions_index + 1, tail, draw_bar, timeDelay)
    
def colorarray(datalen, head, tail, border, curr_index, isSwapping = False):
    colorarray = []
    
    for i in range(datalen):
        
        if i >= head and i <= tail:
            colorarray.append("gray")
        else:
            colorarray.append("white")
            
        if i == tail:
            colorarray[i] == 'orange'
        elif i == border:
            colorarray[i] == 'red'
        elif i == curr_index:
            colorarray == 'yellow'
            
        if isSwapping:
            if i == border or i == curr_index:
                colorarray[i] = 'green'
                
    return colorarray
                            
            