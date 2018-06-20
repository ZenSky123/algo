def quickSort(arr, start, end):
    if start<end:
        left = start
        right = end
        pivot = arr[start]

        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            while left < right and arr[left] <= pivot:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[start], arr[left] = arr[left], arr[start]
        quickSort(arr, start, left - 1)
        quickSort(arr, left + 1, end)


if __name__ == '__main__':
    arr = [6, 2, 1, 23, 6, 68, 6, 213]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
