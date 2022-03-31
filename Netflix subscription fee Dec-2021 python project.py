Country_code: Country,TotalLibrary Size,No. of TV Shows,No. of Movies,Cost Per Month - Basic ($),Cost Per Month - Standard ($),Cost Per Month - Premium ($)
ar,Argentina,4760,3154,1606,3.74,6.3,9.26
au,Australia,6114,4050,2064,7.84,12.12,16.39
at,Austria,5640,3779,1861,9.03,14.67,20.32
be,Belgium,4990,3374,1616,10.16,15.24,20.32
bo,Bolivia,4991,3155,1836,7.99,10.99,13.99
br,Brazil,4972,3162,1810,4.61,7.11,9.96
bg,Bulgaria,6797,4819,1978,9.03,11.29,13.54
ca,Canada,6239,4311,1928,7.91,11.87,15.03
cl,Chile,4994,3156,1838,7.07,9.91,12.74
co,Colombia,4991,3156,1835,4.31,6.86,9.93
cr,Costa Rica,4988,3152,1836,8.99,12.99,15.99
hr,Croatia,2274,1675,599,9.03,11.29,13.54
cz,Czechia,7325,5234,2091,8.83,11.49,14.15
dk,Denmark,4558,2978,1580,12.0,15.04,19.6
ec,Ecuador,4992,3155,1837,7.99,10.99,13.99
ee,Estonia,6456,4486,1970,9.03,11.29,13.54
fi,Finland,4045,2638,1407,9.03,13.54,18.06
fr,France,5445,3604,1841,10.16,15.24,20.32
de,Germany,5668,3814,1854,9.03,14.67,20.32
gi,Gibraltar,6167,4079,2088,9.03,14.67,20.32
gr,Greece,4772,3344,1428,9.03,12.42,15.8
gt,Guatemala,4767,3154,1613,7.99,10.99,13.99
hn,Honduras,4989,3154,1835,7.99,10.99,13.99
hk,Hong Kong,4746,2883,1863,8.08,10.0,11.93
hu,Hungary,6884,4802,2082,7.64,10.71,13.78
is,Iceland,6387,4426,1961,9.03,14.67,20.32
in,India,5843,3718,2125,2.64,6.61,8.6
id,Indonesia,3887,2449,1438,8.36,10.66,12.96
ie,Ireland,6486,4515,1971,9.03,14.67,20.32
il,Israel,5713,3650,2063,10.56,15.05,19.54
it,Italy,5183,3545,1638,9.03,14.67,20.32
jp,Japan,5475,3619,1856,8.73,13.13,17.45
lv,Latvia,6450,4479,1971,9.03,11.29,13.54
li,Liechtenstein,3048,1712,1336,12.88,20.46,26.96
lt,Lithuania,6462,4490,1972,9.03,11.29,13.54
my,Malaysia,5952,3565,2387,8.29,10.65,13.02
mx,Mexico,4993,3158,1835,6.62,10.43,14.24
md,Moldova,3937,2473,1464,9.03,11.29,13.54
mc,Monaco,5804,3806,1998,9.03,13.54,18.06
nl,Netherlands,5376,3779,1597,9.03,13.54,18.06
nz,New Zealand,6084,4003,2081,8.8,12.53,16.94
no,Norway,4528,2955,1573,9.94,12.17,17.75
py,Paraguay,4797,3155,1642,8.29,11.49,14.69
pe,Peru,4986,3155,1831,6.11,8.56,11.01
ph,Philippines,6362,4154,2208,7.35,9.14,10.93
pl,Poland,5109,3512,1597,7.13,10.58,14.76
pt,Portugal,5047,3419,1628,9.03,13.54,18.06
ro,Romania,5303,3832,1471,9.03,11.29,13.54
ru,Russia,5711,3624,2087,8.13,10.84,13.56
sm,San Marino,2310,1937,373,9.03,14.67,20.32
sg,Singapore,6303,4109,2194,9.51,12.81,16.11
sk,Slovakia,7035,5055,1980,9.03,11.29,13.54
za,South Africa,5736,3686,2050,6.26,10.05,12.58
kr,South Korea,5195,3334,1861,8.07,11.47,14.45
es,Spain,5229,3536,1693,9.03,14.67,20.32
se,Sweden,4361,2973,1388,10.9,14.2,19.7
ch,Switzerland,5506,3654,1852,12.88,20.46,26.96
tw,Taiwan,5105,3134,1971,9.74,11.9,14.07
th,Thailand,4948,2977,1971,8.34,10.43,12.52
tr,Turkey,4639,2930,1709,1.97,3.0,4.02
ua,Ukraine,5336,3261,2075,5.64,8.46,11.29
gb,United Kingdom,6643,4551,2092,7.91,13.2,18.48
us,United States,5818,3826,1992,8.99,13.99,17.99
uy,Uruguay,4989,3154,1835,8.99,12.99,15.99
ve,Venezuela,4797,3154,1643,7.99,10.99,13.99

# created dictoionaries

dict= countries{'Argentina': 'ar',
 'Australia': 'au',
  'Austria': 'at',
   'Belguim': 'be'
}

 dict=basic_cost = {'Argentina': 3.74,
 'Australia': 7.84,
  'Austria': 9.03,
   'Belguim': 10.16
}
# per month

 dict=standard_cost = {'Argentina': 6.30,
 'Australia': 12.12,
  'Austria': 14.67, 
  'Belguim': 15.24
}
# per month

dict =premium_cost = {'Argentina': 9.26,
 'Australia': 16.39,
  'Austria': 20.32,
  'Belgium': 20.32
}
# per month

basic_cost= countries('Argentina')
print('This is', + str(3.74), +'per month')

for countries in countries.keys():
    print('Argentina', 'Australia', 'Austria', 'Belgium')

for country, basic_cost in countries.items():
    print('This is ', + str(basic_cost), + ' per month', +' Belguim' ,+ 'countries' )

Belguim = country.get('Belguim')
print('Belguim')


import csv

with open('Netflix subscription fee Dec-2021.csv','r') as csv_file:
    csv_reader = csv.reader(csv.file)

    for line in csv_reader:
        print(line)


# reading in a csv file

# creating classes

class fee(object):

    def __init__(self, Argentina, Belgium, Austria, Austrailia, price,):
        self.country=Argentina
        self.country=Belgium
        self.country=Austria
        self.country=Austrailia

        def speak(self):
            print('This is ', self.Austria, 'the price', '9.03')

        def change_price(self):
            self.price=price
            print('This is',self.Belguim, 'standard: price', '15.24' )

        def add_country(self.country):
            self.Australia=Australia
            print('This has' , self.Australia, 'been added')










Austria=fee('Austria','9.03')
Belguim=fee('Belguim', '10.16' '15.24')
Argentina=fee('Argentina','3.74')
Australia=fee('Australia','7.84')



Austria.speak()
Belguim.speak()
Austria.speak()
Australia.speak()












