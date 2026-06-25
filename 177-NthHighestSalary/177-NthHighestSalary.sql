-- Last updated: 6/25/2026, 9:15:50 AM
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      with cte as (
        select salary , Dense_rank()over(order by salary desc) as rnk from Employee
      )

      select distinct salary from cte where rnk=N

  );
END