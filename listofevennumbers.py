nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(" list of integers:")
print(nums)
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)