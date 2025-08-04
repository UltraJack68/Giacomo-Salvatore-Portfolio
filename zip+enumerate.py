# %% cell 1
nums = [1, 2, 3, 4, 5]
nums1 = [6, 7, 8, 9, 0]

def enumerates(nums):
    for index, x in enumerate(nums):
        print(f"{index}, {x}" )


# %%
nums = [1, 2, 3, 4, 5]
nums1 = [6, 7, 8, 9, 0]
def zips():
    for x, y in zip(nums, nums1):
        print(f"{x}, {y}")


# %%
nums = [1, 2, 3, 4, 5]
nums1 = [6, 7, 8, 9, 0]
def ran_len():
    for index, (x, y) in enumerate(zip(nums, nums1)):
        print(f"{index}, {x}, {y}")

# %%
