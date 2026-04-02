def readBinaryWatch(turnedOn):
    result = []

    for h in range(12):       # hours 0-11
        for m in range(60):   # minutes 0-59
            if (bin(h).count("1") + bin(m).count("1")) == turnedOn:
                result.append(f"{h}:{m:02d}")

    return result

print(readBinaryWatch(7))