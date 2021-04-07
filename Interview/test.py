
def reverse(arr, s):
    if(len(arr)):
        x = arr.pop();
        reverse(arr, s);
    else:
        arr.append(s);
    if(x):
        arr.append(x);


def reverse(arr):
    if(len(arr)):
        s =  arr.pop();
        reverse(arr);
    reverse(arr, s);



1. Cars
    1. id
    2. type
    3. price
    4. isAvailable

2. User
    1. id
    2. address
    3. email
    4. phone

3. Location
    1. id
    2. address
    3. phone
    4. isAvailable
    5. CarId

4. RentHistory
    1. id
    2. CarId
    3. UserId
    4. startDate
    5. endDate
    6. charge
    7. locationId

5. BookingSubscription
    1. id
    2. typeId
    3. Userid
    4. startDate
    5. expirationDate
    6. price

    Select * from Location
    INNER JOIN Cars On Cars.id = Location.Carid
    INNER JOIN RentHistory On RentHistory.CarId = Cars.id
    where location.address = 'given value' and Cars.type = 'SUV'
    and  (endDate < A or startDate > B );







