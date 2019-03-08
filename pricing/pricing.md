# Pricing system

## Overall
- Base fee + fee/km. E.g., 5CHF base fee, then 0.1CHF/km.
- Fees can increase for periods of high demand, e.g., morning to go to work and evening to go home. For example, 10CHF + 0.2CHF/km.
- Fee can decrease for periods of low demand, e.g. afternoon, evening, night. E.g., 3CHF + 0.05CHF/km. 
- These high/low periods and the corresponding fees are optimized as data comes in. Can also have continuous prices fixed by an algorithm, depending on the time and location.

## Weekends and holidays
- Weekends and holidays will be highly demanded. There might be 100 people wanting a car, but only 20 cars.
- Assign cars using an auction system.
- Suppose there are k cars and n people want to book a car. The n people give the price for the base fee they are willing to pay (the fee/km doesn't change since otherwise, people with short routes can overbid). The k highest bidders win, and pay the k-th highest price (they all pay the same price in the end). The minimum price is the normal one, e.g., 5CHF.

### Example
- 2 cars, 5 people interested.
- They bid 10, 11, 20, 22, 50 CHF respectively.
- Bidders with 25 and 50 CHF win and both pay 22CHF. 
 