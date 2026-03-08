import platform
c = platform.python_version()
print(c)
print(platform.python_version_tuple())
if c >= '3.13':       
    print(True)
else:
    print(False)
    