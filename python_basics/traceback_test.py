"""
回溯

"""
# import sys
#
# try:
#     1 / 0
# except:
#     print(sys.exc_info())


import traceback

try:
    1 / 0
except:
    print(traceback.print_exc())
