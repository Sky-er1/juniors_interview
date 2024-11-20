def merge_intervals(intervals: list[int]) -> list[tuple[int, int]]:
    """Сливает пересекающиеся или соседние интервалы."""
    sorted_intervals = sorted(zip(intervals[::2], intervals[1::2]))
    merged = []
    for start, end in sorted_intervals:
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    return merged


def intersect_intervals(intervals1: list[tuple[int, int]], intervals2: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Возвращает пересечения двух списков интервалов."""
    result = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]
        # Пересечение интервалов
        start = max(start1, start2)
        end = min(end1, end2)
        if start < end:
            result.append((start, end))
        # Двигаемся по интервалам
        if end1 < end2:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    # Сливаем интервалы ученика и учителя
    lesson = [(intervals['lesson'][0], intervals['lesson'][1])]
    pupil_intervals = merge_intervals(intervals['pupil'])
    tutor_intervals = merge_intervals(intervals['tutor'])

    # Пересечения ученик + учитель
    pupil_tutor_intersection = intersect_intervals(pupil_intervals, tutor_intervals)

    # Пересечения с уроком
    final_intersection = intersect_intervals(pupil_tutor_intersection, lesson)

    # Суммируем общую длину пересечений
    total_time = sum(end - start for start, end in final_intersection)
    return total_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print("All tests passed!")
