from datetime import datetime, timedelta
from scrapper import scrape
from algorithm import trending

def needsUpdate():
    with open('../../lastUpdated.txt', 'r') as file:
        content = file.read()

    if str(content) == "":
        return True

    lastUpdated = datetime.strptime(content, '%Y-%m-%d %H:%M:%S.%f')
    today = datetime.now()
    diff = today - lastUpdated

    one_week = timedelta(weeks=1)

    if diff > one_week:
        return True
    else:
        print("Already up to date\n")
        return False

def update():
    if needsUpdate():
        scrape()

        with open('../../bestSold.txt', 'w') as file:
            file.write(trending())
        
        today = datetime.now()
        todayf = today.strftime('%Y-%m-%d %H:%M:%S.%f')
        with open('../../lastUpdated.txt', 'w') as file:
            file.write(todayf)