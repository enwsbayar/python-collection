# The musical scales are constructed by a series of whole tones (W) and half tones (H).

# Between each two notes we have a whole tone, except for E to F and B to C that we have a half tone.

# For the major scale with key (root note) in C (C D E F G A B) we have the following mode (distances formula): W W H W W W H

# If we want to change the key we must to keep the same distances pattern, then we should use accidentals bemols or sharps (b or #) in order to decrease o increase a note by half tone, for example if we change the root of the major scale to D the result is D E F# G A B C# that keeps the W W H W W W H notes distances pattern.

# In this kata you have to code a function that allow us to get a scale given a mode and a key note. For example for get_scale('W W H W W W H', 'C') we should get as result ['C', 'D', 'E', 'F', 'G', 'A', 'B'] .

# If we change the key, for example get_scale('W W H W W W H', 'D') we should get as result ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'], that follows the same distances pattern but starting with the D note.

# alt text

# If we change the pattern , for example get_scale('W H W W H W W', 'C') whe should get as result ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'], that is a different scale in the case the Aeolian or minor scale.

# In this link you have additional information on how circle of fifths works!

# To get the same distances we also can provide a solution applying the opposite accidental over the previous or following note, for example an alternative solution for ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'] is ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#'], that is Eb = D# , Ab = G# and Bb = A#. But in this kata we want to mantain the notes notation sequence.

def get_scale(mode, key):
  notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
  flats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
  
  use_flats = 'b' in key
  scale_notes = flats if use_flats else notes
  
  start_idx = scale_notes.index(key)
  current_idx = start_idx
  
  steps = mode.split()
  
  note_letters = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
  start_letter = key[0]
  letter_idx = note_letters.index(start_letter)
  
  result = []
  cumulative = 0
  
  for i in range(len(steps)):
    expected_letter = note_letters[(letter_idx + i) % 7]
    target_idx = (start_idx + cumulative) % 12
    
    found = False
    for candidate in scale_notes:
      if candidate[0] == expected_letter:
        cand_idx = scale_notes.index(candidate)
        if cand_idx == target_idx:
          result.append(candidate)
          found = True
          break
      
      if not found:
        all_notes = notes + flats + ['E#', 'B#', 'Fb', 'Cb']
        for candidate in all_notes:
          if candidate[0] == expected_letter:
            if candidate in ['E#', 'Fb']:
              cand_idx = (notes.index('F') if candidate == 'E#' else notes.index('E')) % 12
            elif candidate in ['B#', 'Cb']:
              cand_idx = (notes.index('C') if candidate == 'B#' else notes.index('B')) % 12
            else:
              cand_idx = notes.index(candidate) if candidate in notes else flats.index(candidate)
            
            if cand_idx == target_idx:
              result.append(candidate)
              break
    
      if i < len(steps):
        cumulative += 2 if steps[i] == 'W' else 1
  
  return result