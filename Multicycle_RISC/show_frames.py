# usage: python show_frames.py uart_out.bin   -> prints each game screen
import sys
d = open(sys.argv[1], 'rb').read().decode('latin1')
frames = d.split('\x1b[H')
print(len(frames) - 1, "frames\n")
for i, f in enumerate(frames[1:], 1):
    print(f"--- frame {i} ---\n{f.replace(chr(27)+'[2J','')}")
