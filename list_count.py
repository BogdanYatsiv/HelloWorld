def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    pos = len([x for x in arr if x > 0])
    neg = sum([x for x in arr if x < 0])
    result = [pos,neg]
    return result