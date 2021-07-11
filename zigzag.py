import time, sys, random

indent = 0
indent_max = 20
indent_increasing = True
symbols = ["••••••••••", "**********"]
print("* enter ctrl-c to quit *")

try:
    while True:
        print(' ' * indent, end='')
        rand_hash = random.choice(symbols)
        print(rand_hash)
        time.sleep(0.2)

        if indent_increasing:
            indent += 1
            if indent == indent_max:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 1:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
