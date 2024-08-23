class Jkcars:
    km = int(input('ENTER APPROXIMATE KM :'))
    trip=int(input('NUMBER OF DAYS       :'))
    km1=km/trip
    if km1 <= 299:
            print('---------- FOR BELOW 300KM/DAY -------')
            print('YOUR TRAVEL KM        :', km)
            print('NUMBER OF DAYS        :',trip,'DAY TRIP')
            a = km * 10
            print('RUPEES $10/KM         :', km, '* 10 =', a)
            b = 1200
            print('ONE DAY RENT FOR CAR  :', b)
            driver = 500 * trip
            print('DRIVER BETA FOR',trip,'DAYS: $',driver)
            print('--------------------------------------------')
            d = a + b + driver
            print('THEREFORE TOTAL AMT   :$', d)
            print('--------------------------------------------')
            print('\n**THIS AMOUNT INCLUDES DIESEL AND DRIVER CHARGES** \n**TOLL CHARGES TAKEN BY CUSTOMER**')
    else:
            print('---------- FOR ABOVE 300KM/DAY ---------')
            print('YOUR TRAVEL KM       :', km)
            print('NUMBER OF DAYS       :', trip, 'DAY TRIP')
            a = km * 12
            print('RUPEES $12/KM        :', km, '* 12 =', a)
            driver = 500 * trip
            print('DRIVER BETA          : $',driver,'/day')
            print('----------------------------------')
            d = a + driver
            print('THEREFORE TOTAL AMT  :$', d)
            print('----------------------------------')
            print('\n**THIS AMOUNT INCLUDES DIESEL AND DRIVER CHARGES** \n**TOLL CHARGES TAKEN BY CUSTOMER**')

