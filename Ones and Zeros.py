def binary_array_to_number(arr):
  # your code
    num = ''.join(str(i) for i in arr)
    return int(num,2)