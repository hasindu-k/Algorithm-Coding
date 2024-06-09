def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

    print("heapify called")

def extract_max_heap(heap):
    if len(heap) == 0:
        return None  # Heap is empty

    # Extracting the maximum element
    maximum = heap[0]

    # Replace the root with the last element
    heap[0] = heap[-1]
    del heap[-1]  # Remove the last element

    print("last deleted ", heap[-1])

    # Heapify the root element to maintain the heap property
    heapify(heap, len(heap), 0)
    print("run")

    return maximum

# Example usage:
heap = [10, 5, 3, 2, 7, 8]
print("Max heap before extraction:", heap)
max_element = extract_max_heap(heap)
second_max_element = extract_max_heap(heap)
print("Maximum element extracted:", max_element)
print("Second maximum element:", second_max_element)
print("Max heap after extraction:", heap)
