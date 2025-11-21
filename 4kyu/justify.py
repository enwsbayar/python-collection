# Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

# Here are the rules:

# Use spaces to fill in the gaps between words.
# Each line should contain as many words as possible.
# Use '\n' to separate lines.
# Last line should not terminate in '\n'
# '\n' is not included in the length of a line.
# Gaps between words can't differ by more than one space.
# Lines should end with a word not a space.
# Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
# Last line should not be justified, use only one space between words.
# Lines with one word do not need gaps ('somelongword\n').
# Example with width=30:

# Lorem  ipsum  dolor  sit amet,
# consectetur  adipiscing  elit.
# Vestibulum    sagittis   dolor
# mauris,  at  elementum  ligula
# tempor  eget.  In quis rhoncus
# nunc,  at  aliquet orci. Fusce
# at   dolor   sit   amet  felis
# suscipit   tristique.   Nam  a
# imperdiet   tellus.  Nulla  eu
# vestibulum    urna.    Vivamus
# tincidunt  suscipit  enim, nec
# ultrices   nisi  volutpat  ac.
# Maecenas   sit   amet  lacinia
# arcu,  non dictum justo. Donec
# sed  quam  vel  risus faucibus
# euismod.  Suspendisse  rhoncus
# rhoncus  felis  at  fermentum.
# Donec lorem magna, ultricies a
# nunc    sit    amet,   blandit
# fringilla  nunc. In vestibulum
# velit    ac    felis   rhoncus
# pellentesque. Mauris at tellus
# enim.  Aliquam eleifend tempus
# dapibus. Pellentesque commodo,
# nisi    sit   amet   hendrerit
# fringilla,   ante  odio  porta
# lacus,   ut   elementum  justo
# nulla et dolor.
# Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

def justify(text, width):
  words = text.split()
  if not words:
    return ""
  
  lines = []
  current_line = []
  current_length = 0
  
  for word in words:
    if current_length + len(word) + len(current_line) <= width:
      current_line.append(word)
      current_length += len(word)
    else:
      lines.append(current_line)
      current_line = [word]
      current_length = len(word)

  if current_line:
      lines.append(current_line)
  
  result = []
  for i, line in enumerate(lines):
    if i == len(lines) - 1:
      result.append(' '.join(line))
    elif len(line) == 1:
      result.append(line[0])
    else:
      total_chars = sum(len(word) for word in line)
      total_spaces = width - total_chars
      gaps = len(line) - 1
      space_per_gap = total_spaces // gaps
      extra_spaces = total_spaces % gaps
      
      justified_line = []
      for j, word in enumerate(line):
        justified_line.append(word)
        if j < len(line) - 1:
          spaces = space_per_gap + (1 if j < extra_spaces else 0)
          justified_line.append(' ' * spaces)
        
        result.append(''.join(justified_line))
  
  return '\n'.join(result)