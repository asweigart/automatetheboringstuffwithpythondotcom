TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    #hello {{
      position: absolute;
      left: {}px;
      top: {}px;
    }}
  </style>
</head>
<body style="background-color: #{}">
  <div id="hello">Go to {}.html</div>
</body>
</html>"""

import random

urls = []
current = 'index'
for i in range(100):
    print(current)
    left = str(random.randint(10, 100))
    top = str(random.randint(10, 100))
    bgcolor = ''.join([random.choice('1234567890ABCDEF') for j in range(6)])
    nextlink = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(4)])
    with open(current + '.html', 'w', encoding='utf-8') as fo:
        fo.write(TEMPLATE.format(left, top, bgcolor, nextlink))
    current = nextlink

