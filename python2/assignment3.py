import os
import platform


def isUp(hostname):

    giveFeedback = False

    if platform.system() == "linux":
        response = os.system("ping "+hostname+" -n 1")
    else:
        response = os.system("ping -c 1 " + hostname)

    isUpBool = False
    if response == 0:
        if giveFeedback:
            print (hostname, 'is up!')
        isUpBool = True
    else:
        if giveFeedback:
            print (hostname, 'is down!')

    return isUpBool

print(isUp("www.google.com"))

