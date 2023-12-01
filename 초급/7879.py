# 7879. 회색조

hex_code = input()
six_codes = hex_code.lstrip('#')

r, g, b = (int(six_codes[i:i+2], 16) for i in (0, 2, 4))
average = round((r + g + b) / 3)
rgb = (average, average, average)
codes = '%02X%02X%02X' % rgb
result = '#' + codes
print(result)