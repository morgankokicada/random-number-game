import random


num = 0


def generate_random_num():
  return random.randint(0, 10)


def diff_from_answer(guess, ans):
  diff = ans - guess
  if diff == 0:
    return "Correct"
  elif diff > 0:
    return "Too low"
  else:
    return "Too high"