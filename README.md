# Article Log Analysis

This is a short script that answers 3 simple questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

These are displayed in plain text format in the terminal.

## Dependencies
- Python 3.6
- The database is named `news`. If this changes, then it will need to be updated in the `psycopg2.connect()` method.

## Usage
- Run the script `python3 logger.py`