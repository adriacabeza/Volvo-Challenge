"""
Pricing functions
"""

BASE_FEE = 5
FEE_PER_KM = 0.1


def time_score(time):
    """
    If time is between 7AM and 9AM, or 5PM and 7PM, returns 2. Else return 1.
    Can (and will) be optimized with ML.
    """
    if ('07:00' < time < '09:00') or ('17:00' < time < '19:00'):
        return 2
    else:
        return 1


def demand_score(car, time):
    """
    Compute the demand score of the car. Returns a coefficient, which is high when demand is high
    and low when demand is low. 
    """
    coefficient = car['demand_score']*time_score(time)
    return coefficient


def get_price(car, time):
    """
    Computes the price the user will pay for the car at that time. 
    Returns the base fee and the fee per km.
    """
    coefficient = demand_score(car, time)
    return coefficient*BASE_FEE, coefficient*FEE_PER_KM


def get_auction_winners(cars, bids):
    k = len(cars)
    winning_bids = sorted(bids, key=lambda k: k['value'], reverse=True)[:k]
    fee = winning_bids[-1]['value']
    return [bid['person'] for bid in winning_bids], fee


cars = [
    {
        'position': [47.4245, 9.3767],
        'demand_score': 1.2
    },
    {
        'position': [48.4245, 8.3767],
        'demand_score': 0.8
    }
]

times = ['08:00', '13:00', '18:00']

bids = [
    {
        'person': 'John',
        'value': 10
    },
    {
        'person': 'Jack',
        'value': 11
    },
    {
        'person': 'Jane',
        'value': 20
    },
    {
        'person': 'Bob',
        'value': 22
    },
    {
        'person': 'Bill',
        'value': 50
    },
]

print('Pricing example')
for car in cars:
    for time in times:
        print('Price for car at position {}N {}E, at time {} is: base fee {:.2f}, fee per km {:.2f}'.format(
            *car['position'], time, *get_price(car, time)))

print('Auction example')
for bid in bids:
    print('{} has bid {}CHF'.format(bid['person'],bid['value']))

winners, fee = get_auction_winners(cars,bids)
for w in winners:
    print('{} has won the auction and will pay {}CHF'.format(w,fee))