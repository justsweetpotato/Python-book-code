import re


DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)

for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))

