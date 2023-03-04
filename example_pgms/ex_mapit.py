import webbrowser
import sys
import pyperclip

#pgm to open google maps

sys.argv

if len(sys.argv) > 1:
    #start_address = ' '.join(sys.argv[1:])
    start_address = sys.argv[1]
    end_address = sys.argv[2]
else:
    address=pyperclip.paste()

webbrowser.open("https://www.google.com/maps/dir/" + start_address + r'/'+ end_address)
