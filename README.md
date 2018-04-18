This is project code for the Udacity [Full-Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

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

## Example
You should see something similar to the following:

```
---------------------------------------------------------
                    Article Log Analysis
---------------------------------------------------------

------------ Top 3 Articles of All Time ------------

"Candidate is jerk, alleges rival" - 338647 Views
"Bears love berries, alleges bear" - 253801 Views
"Bad things gone, say good people" - 170098 Views

--------- Most Popular Authors of All Time ---------

Ursula La Multa - 507594 Views
Rudolf von Treppenwitz - 423457 Views
Anonymous Contributor - 170098 Views
Markoff Chaney - 84557 Views

-------- Days Where Greater Than 1% Errors ---------

2016-07-17 - 2.33%
```
