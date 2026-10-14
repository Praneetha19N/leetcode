select m.name from Employee as e inner join Employee as m
where e.managerId=m.Id group by e.managerId having count(e.Id)>=5;
