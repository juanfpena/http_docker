#
CREATE OR REPLACE VIEW income_by_year AS
SELECT year(s.created_at) AS 'year_income', 
    SUM((stp.quantity * prd.price)) AS 'sales',
    SUM((stp.quantity * pur.cost)) AS 'cost_of_goods_sold',
    (
    SUM((stp.quantity * prd.price)) - SUM((stp.quantity * pur.cost))
    ) AS 'gross_profit'
    FROM sale_to_purchase AS stp
    JOIN purchase AS pur
    ON stp.purchase_id = pur.id
    JOIN sale AS s
    ON s.id = stp.sale_id
    JOIN product AS prd
    ON s.product_id = prd.id
    GROUP BY 1;
#
CREATE OR REPLACE VIEW expenses_by_year AS
SELECT year(created_at) AS 'year_expense', 
	SUM(IF(service_name = 'marketing', cost, 0)) AS 'marketing',
    SUM(IF(service_name = 'hr', cost, 0)) AS 'human_resources',
    SUM(IF(service_name = 'finance', cost, 0)) AS 'finance',
    SUM(IF(service_name = 'others', cost, 0)) AS 'other_expenses',
    (
    SUM(IF(service_name = 'marketing', cost, 0)) +
    SUM(IF(service_name = 'hr', cost, 0)) +
    SUM(IF(service_name = 'finance', cost, 0)) +
    SUM(IF(service_name = 'others', cost, 0))
    ) AS 'total_expenses'
    FROM assigned_expense_item AS a
    JOIN expense_item AS e 
    ON a.item_id = e.id
    JOIN expense_family AS f
    ON e.family_id = f.id
    GROUP BY 1;
#
CREATE OR REPLACE VIEW income_statement_by_year AS
SELECT year_income AS 'year',  
    sales, 
    cost_of_goods_sold, 
    gross_profit,
    marketing,
    human_resources,
    finance,
    other_expenses,
    total_expenses,
    (gross_profit - total_expenses) AS 'profits'
    FROM income_by_year AS i
    JOIN expenses_by_year AS e 
    ON i.year_income = e.year_expense
    GROUP BY 1
    ORDER BY 1;