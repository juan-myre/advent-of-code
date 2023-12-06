f = open("scratch.txt", "r")

import math

def count_wins(line):
  winning_numbers_my_numbers = line.split(': ')[1].split(' | ')
  winning_numbers = winning_numbers_my_numbers[0].strip().split()
  my_numbers = winning_numbers_my_numbers[1].strip().split()

  matches = 0
  for num in my_numbers:
    if num in winning_numbers:
      matches += 1

  return matches

def calculate_winning_numbers():
  total_score = 0
  for line in f:

    matches = count_wins(line)

    if matches > 0:
      total_score += math.pow(2, matches - 1)

  print(total_score)

def count_all_scratch_cards():
  total_cards = 0

  card_multipliers = {}

  lines = []
  index = 1
  for line in f:
    lines.append(line)
    card_multipliers[index] = 1
    index += 1

  for index in range(1, len(lines) + 1):
    print(card_multipliers)
    total_cards += card_multipliers[index]
    matches = count_wins(lines[index - 1])
    print(matches)

    if matches > 0:
      for x in range(0, matches):
        card_multipliers[index + 1 + x] += card_multipliers[index]


  print(total_cards)
count_all_scratch_cards()