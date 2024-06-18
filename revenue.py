import csv

file = open('revenue.csv', 'r')
reader = csv.DictReader(file)

d = {}

for row in reader:
    year = int(row['Year'])
    category = row['Category']
    revenue = float(row['Revenue'])

    if year not in d:
        d[year] = {category: revenue}
    else:
        try:
            d[year][category] += revenue
        except KeyError:
            d[year][category] = revenue

file.close()

sorted_years = sorted(d)
previous_year = sorted_years[0]

for year in sorted_years[1:]:
    year_dict = d[year]
    print(f'\nGrowth {year} vs. {previous_year}')

    for category in sorted(year_dict):
        revenue_current = year_dict[category]
        try:
            revenue_previous = d[previous_year][category]
            revenue_growth = f'{(revenue_current - revenue_previous) / revenue_previous:.2f}%'
        except KeyError:
            revenue_growth = 'No data for previous year'
        except ZeroDivisionError:
            revenue_growth = f'${revenue_current - revenue_previous}'

        print(f'\t{category}: {revenue_growth}')

    previous_year = year

