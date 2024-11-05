from csv import reader

counts = 0  

with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1]) > 30:
            try:
                price = float(row[6].replace(',', '.'))
                if price >= 200:
                    count += 1
            except ValueError:
                print(f'Invalid price: {row[6]}')

print('Total number is: ', counts)