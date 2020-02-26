from django.test import TestCase

# Create your tests here.
test_list = [4, 5, 8, 9, 10, 13, 15, 17]
mid = len(test_list) // 2

print((test_list[mid]+test_list[~mid])/2)
print(mid)
print(test_list[~mid])