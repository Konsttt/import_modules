from datetime import date
import colorterminal

from db.people import get_employees
from salary import calculate_salary

if __name__ == '__main__':
    print(date.today())
    print(date.strftime(date.today(), '%d.%m.%Y'))
    calculate_salary()
    get_employees()
    print(colorterminal.ColorText.RED + 'Hello' + colorterminal.ColorText.PURPLE + ' World')
    print(colorterminal.ColorBackground.YELLOW + colorterminal.ColorText.BLACK + 'Hello World' + colorterminal.ColorBackground.BLACK)
