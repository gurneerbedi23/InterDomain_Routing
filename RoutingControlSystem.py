from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

#print(config.sections())
#print(list(config['ASN 100 to ASN 200']))
#print(config['ASN 100 to ASN 200']['Cost'])

ASN110_RCID = config['ASN 110']['RCID']
ASN110_ASN = config['ASN 110']['ASN']
ASN110_IP = config['ASN 110']['IP Address']

ASN120_RCID = config['ASN 120']['RCID']
ASN120_ASN = config['ASN 120']['ASN']
ASN1120_IP = config['ASN 120']['IP Address']

ASN210_RCID = config['ASN 210']['RCID']
ASN210_ASN = config['ASN 210']['ASN']
ASN210_IP = config['ASN 210']['IP Address']

ASN220_RCID = config['ASN 220']['RCID']
ASN220_ASN = config['ASN 220']['ASN']
ASN220_IP = config['ASN 220']['IP Address']

ASN310_RCID = config['ASN 310']['RCID']
ASN310_ASN = config['ASN 310']['ASN']
ASN310_IP = config['ASN 310']['IP Address']

ASN330_RCID = config['ASN 330']['RCID']
ASN330_ASN = config['ASN 330']['ASN']
ASN330_IP = config['ASN 330']['IP Address']

ASN430_RCID = config['ASN 430']['RCID']
ASN430_ASN = config['ASN 430']['ASN']
ASN430_IP = config['ASN 430']['IP Address']

ASN420_RCID = config['ASN 420']['RCID']
ASN420_ASN = config['ASN 420']['ASN']
ASN420_IP = config['ASN 420']['IP Address']

cost_100_200 = config['ASN 100 to ASN 200, 10 to 20']['Cost']
cost_100_300 = config['ASN 100 to ASN 300']['Cost']
cost_100_400 = config['ASN 100 to ASN 400']['Cost']
cost_200_300 = config['ASN 200 to ASN 300']['Cost']
cost_200_400 = config['ASN 200 to ASN 400']['Cost']
cost_300_400 = config['ASN 300 to ASN 400']['Cost']

# dict = {
#     'ASN110_RCID' : config['ASN 110']['RCID'],
#     1 : config['ASN 110']['ASN'],
#     'ASN110_IP' : config['ASN 110']['IP Address']
# }

while True:
    print("\n\nEnter a number 1 - 8 to choose which client you are")
    print("\nClient 1: ASN 10 on ASN 100\nClient 2: ASN 20 on ASN 100\nClient 3: ASN 10 on ASN 200\nClient 4: ASN 40 on ASN 200\nClient 5: ASN 30 on ASN 300\nClient 6: ASN 10 on ASN 300\nClient 7: ASN 20 on ASN 400\nClient 8: ASN 30 on ASN 400\n")
    sender = input('Number: ')


    print("\n\nEnter a number 1 - 8 to choose which client you want to communicate with")
    print("\nClient 1: ASN 10 on ASN 100\nClient 2: ASN 20 on ASN 100\nClient 3: ASN 10 on ASN 200\nClient 4: ASN 40 on ASN 200\nClient 5: ASN 30 on ASN 300\nClient 6: ASN 10 on ASN 300\nClient 7: ASN 20 on ASN 400\nClient 8: ASN 30 on ASN 400\n")
    receiver = input('Number: ')

    # ASN 100, ASN 10
    if sender == receiver:
        raise ValueError('sender and receiver must be different')
    elif sender == '1' and receiver == '2':
        print('\n\nRCU MESSAGE{RCID =',ASN110_RCID, ', LOCAL_ASN =', config['ASN 100 to ASN 200, 10 to 20']['LOCAL_ASN'], ', DEST_ASN = PATH{ASN 100, ASN 20}', ', BANDWIDTH =', config['ASN 100 to ASN 200, 10 to 20']['Link Capacity'], ', Cost = [SAME ASN]}\n\n')
    elif sender == '1' and receiver == '3':
        print('\n\nRCU MESSAGE{RCID =',ASN110_RCID, ', LOCAL_ASN =', config['ASN 100 to ASN 200, 10 to 20']['LOCAL_ASN'], ', DEST_ASN =', config['ASN 100 to ASN 200, 10 to 20']['DEST_ASN'], ', BANDWIDTH =', config['ASN 100 to ASN 200, 10 to 20']['Link Capacity'], ', Cost =', cost_100_200,'}\n\n')
    elif sender == '1' and receiver == '4':
        print('\n\nRCU MESSAGE{RCID =',ASN110_RCID, ', LOCAL_ASN =', config['ASN 100 to ASN 200, 10 to 20']['LOCAL_ASN'], ' DEST_ASN = PATH{ASN 200, ASN 40}, BANDWIDTH =', config['ASN 100 to ASN 200, 10 to 20']['Link Capacity'], ', Cost =', cost_100_200,'}\n\n')
    elif sender == '1' and receiver == '5':
        print('\n\nRCU MESSAGE{RCID =',ASN110_RCID, ', LOCAL_ASN =', config['ASN 100 to ASN 200, 10 to 20']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 300']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n')
    elif sender == '1' and receiver == '6':
        print('\n\nRCU MESSAGE{RCID =',ASN110_RCID, ', LOCAL_ASN =', config['ASN 100 to ASN 200, 10 to 20']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 300']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n')
    elif sender == '1' and receiver == '7':
        print('\n\nRCU MESSAGE{RCID =',ASN110_RCID, ', LOCAL_ASN =', config['ASN 100 to ASN 200, 10 to 20']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 400']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n')
    elif sender == '1' and receiver == '8':
        print('\n\nRCU MESSAGE{RCID =',ASN110_RCID, ', LOCAL_ASN =', config['ASN 100 to ASN 200, 10 to 20']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 400']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n')
    
    #ASN 100, ASN 20
    elif sender == '2' and receiver == '1':
        print('\n\nRCU MESSAGE{RCID =',ASN120_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 200, 10 to 20']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost = [SAME ASN]}\n\n') 
    elif sender == '2' and receiver == '3':
        print('\n\nRCU MESSAGE{RCID =',ASN120_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{ASN 200, ASN 10}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =',cost_100_200, '}\n\n') 
    elif sender == '2' and receiver == '4':
        print('\n\nRCU MESSAGE{RCID =',ASN120_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{ASN 200, ASN 40}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =',cost_100_200, '}\n\n') 
    elif sender == '2' and receiver == '5':
        print('\n\nRCU MESSAGE{RCID =',ASN120_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 300']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n') 
    elif sender == '2' and receiver == '6':
        print('\n\nRCU MESSAGE{RCID =',ASN120_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 300']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n') 
    elif sender == '2' and receiver == '7':
        print('\n\nRCU MESSAGE{RCID =',ASN120_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 400']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n') 
    elif sender == '2' and receiver == '8':
        print('\n\nRCU MESSAGE{RCID =',ASN120_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 100 to ASN 400']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n') 

    # ASN 200, ASN 10
    elif sender == '3' and receiver == '1':
        print('\n\nRCU MESSAGE{RCID =',ASN210_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 100']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_200,'}\n\n') 
    elif sender == '3' and receiver == '2':
        print('\n\nRCU MESSAGE{RCID =',ASN210_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 100']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_100_200,'}\n\n') 
    elif sender == '3' and receiver == '4':
        print('\n\nRCU MESSAGE{RCID =',ASN210_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{ASN 200, ASN 40}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost = [SAME ASN]}\n\n') 
    elif sender == '3' and receiver == '5':
        print('\n\nRCU MESSAGE{RCID =',ASN210_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 300']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n') 
    elif sender == '3' and receiver == '6':
        print('\n\nRCU MESSAGE{RCID =',ASN210_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 300']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n')
    elif sender == '3' and receiver == '7':
        print('\n\nRCU MESSAGE{RCID =',ASN210_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 400']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    elif sender == '3' and receiver == '8':
        print('\n\nRCU MESSAGE{RCID =',ASN210_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 400']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 100 to ASN 300']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    
    # ASN 200, ASN 40
    elif sender == '4' and receiver == '1':
        print('\n\nRCU MESSAGE{RCID =',ASN220_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN3'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 100']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 200 to ASN 100']['Link Capacity'], ', Cost =', cost_100_200,'}\n\n')
    elif sender == '4' and receiver == '2':
        print('\n\nRCU MESSAGE{RCID =',ASN220_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN3'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 100']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 200 to ASN 100']['Link Capacity'], ', Cost =', cost_100_200,'}\n\n')
    elif sender == '4' and receiver == '3':
        print('\n\nRCU MESSAGE{RCID =',ASN220_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN3'], ', DEST_ASN = PATH{ASN 200, ASN 10}, BANDWIDTH =', config['ASN 200 to ASN 100']['Link Capacity'], ', Cost = [SAME ASN]}\n\n')
    elif sender == '4' and receiver == '5':
        print('\n\nRCU MESSAGE{RCID =',ASN220_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN3'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 300']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 200 to ASN 300']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n')
    elif sender == '4' and receiver == '6':
        print('\n\nRCU MESSAGE{RCID =',ASN220_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN3'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 300']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 200 to ASN 300']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n')
    elif sender == '4' and receiver == '7':
        print('\n\nRCU MESSAGE{RCID =',ASN220_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN3'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 400']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 200 to ASN 400']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    elif sender == '4' and receiver == '8':
        print('\n\nRCU MESSAGE{RCID =',ASN220_RCID, ', LOCAL_ASN =', config['ASN 200 to ASN 100']['LOCAL_ASN3'], ', DEST_ASN = PATH{', config['ASN 200 to ASN 400']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 200 to ASN 400']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    
    # ASN 300, ASN 30
    elif sender == '5' and receiver == '1':
        print('\n\nRCU MESSAGE{RCID =',ASN330_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 100']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 300 to ASN 100']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n')
    elif sender == '5' and receiver == '2':
        print('\n\nRCU MESSAGE{RCID =',ASN330_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 100']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 300 to ASN 100']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n')
    elif sender == '5' and receiver == '3':
        print('\n\nRCU MESSAGE{RCID =',ASN330_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 200']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 300 to ASN 200']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n')
    elif sender == '5' and receiver == '4':
        print('\n\nRCU MESSAGE{RCID =',ASN330_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 200']['DEST_ASN'], ', ASN 40}, BANDWIDTH =', config['ASN 300 to ASN 200']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n')
    elif sender == '5' and receiver == '6':
        print('\n\nRCU MESSAGE{RCID =',ASN330_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN'], ', DEST_ASN = PATH{ASN 300, ASN 10}, BANDWIDTH =', config['ASN 300 to ASN 200']['Link Capacity'], ', Cost = [SAME ASN]}\n\n')
    elif sender == '5' and receiver == '7':
        print('\n\nRCU MESSAGE{RCID =',ASN330_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 400']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 300 to ASN 400']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    elif sender == '5' and receiver == '8':
        print('\n\nRCU MESSAGE{RCID =',ASN330_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 400']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 300 to ASN 400']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    
    # ASN 300, ASN 10
    elif sender == '6' and receiver == '1':
        print('\n\nRCU MESSAGE{RCID =',ASN310_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 100']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 300 to ASN 100']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n')
    elif sender == '6' and receiver == '2':
        print('\n\nRCU MESSAGE{RCID =',ASN310_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 100']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 300 to ASN 100']['Link Capacity'], ', Cost =', cost_100_300,'}\n\n')
    elif sender == '6' and receiver == '3':
        print('\n\nRCU MESSAGE{RCID =',ASN310_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 200']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 300 to ASN 200']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n')
    elif sender == '6' and receiver == '4':
        print('\n\nRCU MESSAGE{RCID =',ASN310_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 200']['DEST_ASN'], ', ASN 40}, BANDWIDTH =', config['ASN 300 to ASN 200']['Link Capacity'], ', Cost =', cost_200_300,'}\n\n')
    elif sender == '6' and receiver == '5':
        print('\n\nRCU MESSAGE{RCID =',ASN310_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN2'], ', DEST_ASN = PATH{ASN 300, ASN 30}, BANDWIDTH =', config['ASN 300 to ASN 200']['Link Capacity'], ', Cost = [SAME ASN]}\n\n')
    elif sender == '6' and receiver == '7':
        print('\n\nRCU MESSAGE{RCID =',ASN310_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 400']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 300 to ASN 400']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    elif sender == '6' and receiver == '8':
        print('\n\nRCU MESSAGE{RCID =',ASN310_RCID, ', LOCAL_ASN =', config['ASN 300 to ASN 200']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 300 to ASN 400']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 300 to ASN 400']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    
    # ASN 400, ASN 20
    elif sender == '7' and receiver == '1':
        print('\n\nRCU MESSAGE{RCID =',ASN420_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 100']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 400 to ASN 100']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n')
    elif sender == '7' and receiver == '2':
        print('\n\nRCU MESSAGE{RCID =',ASN420_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 100']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 400 to ASN 100']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n')
    elif sender == '7' and receiver == '3':
        print('\n\nRCU MESSAGE{RCID =',ASN420_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 200']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 400 to ASN 200']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    elif sender == '7' and receiver == '4':
        print('\n\nRCU MESSAGE{RCID =',ASN420_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 200']['DEST_ASN'], ', ASN 40}, BANDWIDTH =', config['ASN 400 to ASN 200']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    elif sender == '7' and receiver == '5':
        print('\n\nRCU MESSAGE{RCID =',ASN420_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 300']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 400 to ASN 300']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    elif sender == '7' and receiver == '6':
        print('\n\nRCU MESSAGE{RCID =',ASN420_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 300']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 400 to ASN 300']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    elif sender == '7' and receiver == '8':
        print('\n\nRCU MESSAGE{RCID =',ASN420_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN'], ', DEST_ASN = PATH{ASN 400, ASN 30}, BANDWIDTH =', config['ASN 400 to ASN 300']['Link Capacity'], ', Cost = [SAME ASN]}\n\n')
    
    # ASN 400, ASN 30
    elif sender == '8' and receiver == '1':
        print('\n\nRCU MESSAGE{RCID =',ASN430_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 100']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 400 to ASN 100']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n')
    elif sender == '8' and receiver == '2':
        print('\n\nRCU MESSAGE{RCID =',ASN430_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 100']['DEST_ASN'], ', ASN 20}, BANDWIDTH =', config['ASN 400 to ASN 100']['Link Capacity'], ', Cost =', cost_100_400,'}\n\n')
    elif sender == '8' and receiver == '3':
        print('\n\nRCU MESSAGE{RCID =',ASN430_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 200']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 400 to ASN 200']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    elif sender == '8' and receiver == '4':
        print('\n\nRCU MESSAGE{RCID =',ASN430_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 200']['DEST_ASN'], ', ASN 40}, BANDWIDTH =', config['ASN 400 to ASN 200']['Link Capacity'], ', Cost =', cost_200_400,'}\n\n')
    elif sender == '8' and receiver == '5':
        print('\n\nRCU MESSAGE{RCID =',ASN430_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 300']['DEST_ASN'], ', ASN 30}, BANDWIDTH =', config['ASN 400 to ASN 300']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    elif sender == '8' and receiver == '6':
        print('\n\nRCU MESSAGE{RCID =',ASN430_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{', config['ASN 400 to ASN 300']['DEST_ASN'], ', ASN 10}, BANDWIDTH =', config['ASN 400 to ASN 300']['Link Capacity'], ', Cost =', cost_300_400,'}\n\n')
    elif sender == '8' and receiver == '7':
        print('\n\nRCU MESSAGE{RCID =',ASN430_RCID, ', LOCAL_ASN =', config['ASN 400 to ASN 100']['LOCAL_ASN2'], ', DEST_ASN = PATH{ASN 400, ASN 20}, BANDWIDTH =', config['ASN 400 to ASN 300']['Link Capacity'], ', Cost = [SAME ASN]}\n\n')
    else:
        print('\nInvalid client selection, try again')
