# pattern 1
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# for i in range(5):
#     for j in range(5):
#         print("* ", end='')
#     else:
#         print("")


# pattern 2
# *
# **
# ***
# ****
# *****
# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print("*", end='')
#     else:
#         print("")

# pattern 3
#     *
#    **
#   ***
#  ****
# *****
# k = 5
# for i in range(5):
#     while k > i + 1:
#         print(" ", end='')
#         k -= 1
#     for j in range(5):
#         if j <= i:
#             print("*", end='')
#     else:
#         k = 5
#         print("")

# pattern 4
# *****
# ****
# ***
# **
# *
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end='')
#     else:
#         print("")

# pattern 5
# *****
#  ****
#   ***
#    **
#     *
# for i in range(5, 0, -1):
#     for k in range(5):
#         if i < k + 1:
#             print(" ", end='')
#     for j in range(i):
#         print("*", end='')
#     else:
#         print("")

# pattern 2
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# k = 5
# for i in range(5):
#     while k > i + 1:
#         print(" ", end='')
#         k -= 1
#     for j in range(5):
#         if j <= i:
#             print("* ", end='')
#     else:
#         k = 5
#         print("")
