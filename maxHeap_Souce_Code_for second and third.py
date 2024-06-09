import heapq

def extract_second_max_heap(heap):
    if len(heap) < 2:
        return None  # Heap doesn't have enough elements

    # Extract the maximum element (root)
    maximum = heap[0]

    print("test maximum", maximum)

    # Replace the root with the last element
    heap[0] = heap[-1]
    del heap[-1]  # Remove the last element

    print("last deleted ", heap[-1])

    # Heapify the root element to maintain the heap property
    heapq._heapify_max(heap)  # Convert to max heap

    # The new root is the second maximum element
    second_maximum = heap[0]

    # Replace the root again with the last element
    heap[0] = heap[-1]
    del heap[-1]

    print("last deleted ", heap[-1])

    # Heapify the root element again
    heapq._heapify_max(heap)

    # The new root is the third maximum element
    third_maximum = heap[0]


    #return third_maximum this return third maximum if needed
    return second_maximum

# Example usage:
my_heap = [50, 30, 20, 10, 40]
second_max = extract_second_max_heap(my_heap)
print("Second maximum element:", second_max)
