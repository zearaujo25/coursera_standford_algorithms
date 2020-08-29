def heap_insert(heap,position_map,element):
    heap.append(element)
    position_map[element] = len(heap)-1
    bubble_up(heap,position_map,element)

def bubble_up(heap,position_map,element):
    parent = heap[(position_map[element]+1)//2 -1]
    while element < parent and position_map[element] != 0:
        swap_elements(heap,position_map,(element,parent))
        parent = heap[(position_map[element]+1)//2 -1]

def swap_elements(heap,position_map,elements):
    positions = position_map[elements[0]],position_map[elements[1]]

    heap[positions[0]] = elements[1]
    heap[positions[1]] = elements[0]

    position_map[elements[0]] = positions[1]
    position_map[elements[1]] = positions[0]


def heap_extract_min(heap,position_map):
    swap_elements(heap,position_map,(heap[0],heap[-1]))
    min_element = heap.pop()
    position_map.pop(min_element)
    if len(heap) >1:
        bubble_down(heap,position_map,heap[0])
    return min_element

def bubble_down(heap,position_map,element):
    min_child = get_min_child(position_map, element, heap)
    while element > min_child:
        swap_elements(heap,position_map,(element,min_child))
        min_child = get_min_child(position_map, element, heap)

def get_min_child(position_map, element, heap):
    left_child = heap[(position_map[element]+1)*2-1] if (position_map[element]+1)*2-1 < len(heap) else float("inf")
    right_child = heap[(position_map[element]+1)*2] if (position_map[element]+1)*2 < len(heap) else float("inf")
    return min(left_child,right_child)

def heap_delete(heap,position_map,element):
    element_position = position_map[element]
    swap_elements(heap,position_map,(element,heap[-1]))
    heap.pop()
    position_map.pop(element)
    if len(heap) >1:
        bubble_down(heap,position_map,heap[element_position])