import os
print("Netsh")
os.system("color 0a")
os.system("netsh wlan show profiles")
print("Choose your target")
t = input(">_ ")
os.system("color 4")
os.system("netsh wlan show profiles %s key=clear" % t)
os.system("pause")                                      