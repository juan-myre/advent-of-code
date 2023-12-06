f = open("manual.txt", "r")

from functools import reduce
import re

def findInteresingIndices(line, interestingIndices, regex = r"[^\.0-9\n]{1}"):
    if line is None:
        return

    results = [m.start() for m in re.finditer(regex, line)]

    for index in results:
      index_before = index - 1 if index > 0 else None
      index_after = index + 1 if index < len(line) - 1 else None

      interestingIndices.append(index)

      if index_before != None:
        interestingIndices.append(index_before)

      if index_after != None:
        interestingIndices.append(index_after)

def getNumbers(line, interestingIndices):
  numbers = []
  for match in re.finditer(r'[0-9]+', line):
    for interestingIndex in interestingIndices:
      if match.start() <= interestingIndex and match.end() > interestingIndex:
        numbers.append(int(match.group()))
        break

  return numbers

def getGearRatios(prevLine, currLine, nextLine, interestingIndices):
    total_sum = 0


    for asteriskIndex in interestingIndices:
        numbers = []

        for line in [prevLine, currLine, nextLine]:
            if line is None:
                continue

            for match in re.finditer(r'[0-9]+', line):
                if match.start() <= asteriskIndex and match.end() > asteriskIndex:
                    numbers.append(int(match.group()))
                    break

        if len(numbers) == 2:
            total_sum += sum(numbers)

    return total_sum

def processFile():
    lines = []
    out_sum = 0
    for line in f:
        lines.append(line)

    for i in range(0, len(lines)):
        prevLine = lines[i - 1] if i > 0 else None
        currLine = lines[i]
        nextLine = lines[i + 1] if i < len(lines) - 1 else None

        interestingIndices = []

        asteriskRegex = r"\*"

        findInteresingIndices(currLine, interestingIndices, asteriskRegex)

        interestingIndices = list(dict.fromkeys(interestingIndices))
        print(interestingIndices)

        gear_ratios = getGearRatios(
            prevLine,
            currLine,
            nextLine,
            interestingIndices,
        )

        out_sum += gear_ratios

    print(out_sum)

def processFile():
    lines = []
    out_sum = 0
    for line in f:
        lines.append(line)

    for i in range(0, len(lines)):
        prevLine = lines[i - 1] if i > 0 else None
        currLine = lines[i]
        nextLine = lines[i + 1] if i < len(lines) - 1 else None

        interestingIndices = []

        findInteresingIndices(prevLine, interestingIndices)
        findInteresingIndices(currLine, interestingIndices)
        findInteresingIndices(nextLine, interestingIndices)

        interestingIndices = list(dict.fromkeys(interestingIndices))
        print(interestingIndices)

        numbers = getNumbers(currLine, interestingIndices)

        out_sum += sum(numbers)

    print(out_sum)


processFile()