# Write your MySQL query statement below
SELECT name, SUM(amount) AS balance
FROM Users JOIN Transactions ON Users.account = Transactions.account
GROUP BY Users.account
HAVING (balance > 10000);