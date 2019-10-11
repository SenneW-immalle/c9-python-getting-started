from datetime import datetime, timedelta

# print today's date
vandaag = datetime.now()
print(vandaag)

# print yesterday's date
een_dag = timedelta(days=1)
gisteren = vandaag - een_dag
print('gisteren was het: ' + str(gisteren))
# ask a user to enter a date
ingegeven = input('Geef een datum in (dd/mm/jjjj): ')
ingegeven = datetime.strptime(ingegeven, '%d/%m/%Y')

# print the date one week from the date entered
een_week = timedelta(weeks=1)
volgende_week = ingegeven + een_week
print('1 week na de ingegeven datum is het: ' + str(volgende_week))
