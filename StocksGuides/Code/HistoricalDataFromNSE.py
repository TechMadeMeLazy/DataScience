from nsepy import get_history
from datetime import datetime


if __name__ == '__main__':
    start_date = datetime(2002, 1, 1)
    end_date = datetime(2022, 1, 1)
    data = get_history(symbol='IDEA', start=start_date, end=end_date)
    data.to_csv('IDEA_NS.csv')
    print(data)