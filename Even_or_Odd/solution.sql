SELECT number,
  CASE 
    WHEN number % 2 = 0 THEN 'even'
    ELSE 'odd'
  END AS EvenOrOdd
FROM number
