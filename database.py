import sqlite3


def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    with open('create_table.sql', 'r') as f:
        sql = f.read()
        cursor.execute(sql)
    return conn, cursor


def insert_data(ticker, date, currency_data):
    print('Inserting data for {} on {}'.format(ticker, date))
    conn, cursor = create_table()
    cursor.execute(
        'INSERT INTO currency_data '
        '(ticker, date, open, high, low, close) '
        'VALUES (?, ?, ?, ?, ?, ?)',
        (
            ticker,
            date,
            currency_data.open,
            currency_data.high,
            currency_data.low,
            currency_data.adj_close
        )

    )
    cursor.close()
    conn.commit()
    conn.close()


