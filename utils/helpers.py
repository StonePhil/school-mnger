def linear_search(records, search_value: str, field_index: int):
    #linear search by a specific field
    results = []
    search_lower = search_value.lower()
    for record in records:
        if str(record[field_index]).lower() == search_lower:
            results.append(record)
    return results


def bubble_sort(records, key_index: int):
    #bubble sort by a specific column, case insensitive
    n = len(records)
    sorted_records = records[:]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if str(sorted_records[j][key_index]).lower() > str(sorted_records[j + 1][key_index]).lower():
                sorted_records[j], sorted_records[j + 1] = sorted_records[j + 1], sorted_records[j]
                swapped = True
        if not swapped:
            break
    return sorted_records
