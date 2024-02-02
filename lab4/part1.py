#student name: Ethan Watchorn
#student number: 16538530

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """

    # Uses global keyword to allow the threads to reference the shared variables
    global testcase
    global sortedFirstHalf
    global sortedSecondHalf

    # Determines which half of the list the function will sort
    if firstHalf:
        sorting_buffer = testcase[:int(len(testcase)/2)]
    else:
        sorting_buffer = testcase[int(len(testcase)/2):]

    # Moves the largest element to end of the list, then repeats on the sub-list of length n-1 until it's all sorted.
    for i in range(len(sorting_buffer)-1, 0, -1):
        # Compares each element with the next element. If it's bigger, switch their places and repeat.
        for j in range(i):
            if sorting_buffer[j] > sorting_buffer[j+1]:
                temp = sorting_buffer[j]
                sorting_buffer[j] = sorting_buffer[j+1]
                sorting_buffer[j+1] = temp

    # Depending on which half of the list we sorted, assign the sorting buffer to the respective shared variable.
    if firstHalf:
        sortedFirstHalf = sorting_buffer
    else:
        sortedSecondHalf = sorting_buffer

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    # Uses global keyword to allow the threads to reference the shared variables
    global sortedFirstHalf
    global sortedSecondHalf
    global SortedFullList
    first = sortedFirstHalf
    second = sortedSecondHalf

    # looks at the smallest (first) entries of each sorted list, and appends the lowest entry to the sorted list.
    # If an entry from a list gets appended, we remove it from the original list so we don't append again.
    # Do this until one of the lists is empty.
    while len(first)>0 and len(second)>0:
        if first[0] < second[0]:
            SortedFullList.append(first[0])
            first.remove(first[0])
        else:
            SortedFullList.append(second[0])
            second.remove(second[0])
    # Adds the rest of the sorted entries to the sorted list (one of the half lists is empty at this point.)
    SortedFullList = SortedFullList + second + first

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified
    thread_first_half = threading.Thread(target=sortingWorker, args=[True])
    thread_second_half = threading.Thread(target=sortingWorker, args=[False])
    thread_merge = threading.Thread(target=mergingWorker)
    thread_first_half.start()
    thread_second_half.start()
    thread_first_half.join()
    thread_second_half.join()
    # Starts merging after the first two lists are sorted
    # Data in sorted_full depends on data from the half-sorting.
    thread_merge.start()
    thread_merge.join()

    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)
