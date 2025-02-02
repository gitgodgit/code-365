def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
    total_duration = 0
    for i in range(len(timeSeries) - 1):
        if timeSeries[i + 1] - timeSeries[i] < duration:
            total_duration += timeSeries[i + 1] - timeSeries[i]
        else:
            total_duration += duration
    return total_duration + duration

