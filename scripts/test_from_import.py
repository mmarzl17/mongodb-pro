import sys
from utils.common import a


print("a: ", a)
import_modules = sys.modules
for m in import_modules:
    print("m: {}\n".format(m))