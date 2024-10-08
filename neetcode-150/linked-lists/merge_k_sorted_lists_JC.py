class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use merge-sort!
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[mid:]
                right = arr[:mid]

                mergeSort(left)
                mergeSort(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
            
        # Grab all nodes and stuff them into an array. Then use merge sort to sort.
        arr = []
        for root in lists:
            while root is not None:
                arr.append(root.val)
                root = root.next
        mergeSort(arr)
        
        # Create the new, sorted LL.
        dummy = root = ListNode()
        for nodeVal in arr:
            root.next = ListNode(nodeVal)
            root = root.next
        
        return dummy.next

        # on side note, how the hell do you do it in SC O(1)?

'''
TLDR: Get every single element, shove it into arr, then run merge sort. Then, run a loop on the sorted arr to get your sorted LL.

TC O(nlogn) - Sorting
SC O(n)... apparently can get O(1) with priority queue?
'''
