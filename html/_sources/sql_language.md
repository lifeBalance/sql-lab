# About the SQL language
In the last section, you saw briefly an `SQL` query in action. There are a few things to take into account when writing these queries.

## Case-insensitive
`SQL` is case-insensitive, meaning that it doesn't really matter if we write in uppercase:
```sql
SELECT * FROM customers;
```

lowercase:
```sql
select * from customers;
```

and even:
```sql
SeLeCt * fRoM customers;
```

## Statements end with a semicolon
Remember to end your statements with a semicolon.