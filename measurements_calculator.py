"""Script to calculate electricity counter trend and recognize where difference between measurements was at maximum."""
data_by_month = {
    "09.21": 180940,
    "08.21": 177604,
    "07.21": 171305,
    "06.21": 166208,
    "05.21": 161704,
    "04.21": 158429,
    "03.21": 155353,
    "02.21": 153274,
    "01.21": 150464,
    "12.20": 147810,
    "11.20": 145568,
    "10.20": 143204
}

months = [x for x in data_by_month.keys()]
data = [x for x in data_by_month.values()]
max_diff = 0
months_at_max_diff = None

for i in range(len(months)-1):
    diff = data[i] - data[i+1] 
    print(f"Difference between {months[i]} and {months[i+1]}: {diff}")
    if diff > max_diff:
        max_diff = diff
        months_at_max_diff = (months[i], months[i+1])

print(f"Max difference was between {months_at_max_diff[0]} and {months_at_max_diff[1]} and equals: {max_diff}")
