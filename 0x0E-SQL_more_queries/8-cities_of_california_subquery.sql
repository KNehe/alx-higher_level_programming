-- Lists cities of California
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') GROUP BY id ORDERBY id ASC; 
