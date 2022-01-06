# CLI-commands

### To select the table or the view you want to see

```
python -m CLI_command.select_table [arg]*
```

    *[arg] is the name of the table you wish to see:
    
    command  -  table

    product  >> product 
    sale     >> sale 
    item     >> expense_item 
    family   >> expense_family
    assei    >> assigned_expense_item 
    stp      >> sale_to_purchase
    cust     >> customer
    
    all      >> all tables

```
python -m CLI_command.select_view [arg1] [arg2]**
```

    
    **  [arg1] Can be "month" or "year"

    [arg2] Is to know which of the views related to [arg1] you want to see

    command  -  view table

    1   >>  income_by_month / income_by_year
    2   >>  expenses_by_month / expenses_by_year
    3   >>  income_statement_by_month /income_statement_by_year

    If you wish to see all of them, only use <arg1> like all

    command  --  view table

    all     >>  all views


### To create a sale

```
python -m CLI_command.create_sale [args]**
```

    ** Args consist of values for columns in the sales table.

    [arg1] >> product_id
    [arg2] >> created_at, must be in "YYYY-MM-DD HH:MM:SS" format
    [arg3] >> quantity
    [arg4] >> customer_id

This script also modifies all tables related to sales.

### To delete by id


```
python -m  CLI_command.delete_id [arg1] [arg2]
```
[arg1] : table name
[arg2] : id

### To insert

```
python -m  CLI_command.insert [arg1] [args2]
```
[arg1] : table name
[args2] : values of each column
   
### To update

```
python -m  CLI_command.update_id [arg1] [arg2] [args3]
```
[arg1] : table name
[arg2] : id
[args3] : values of each column