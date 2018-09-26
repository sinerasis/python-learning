#import libraries
import settings

#attempt to open file
try:
    file = open(settings.InputFile, "r")

    print(file.readlines())
except:
    print("Could not open file: " + settings.InputFile)