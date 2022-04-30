from bsedata.bse import BSE
import json


if __name__ == '__main__':
    bse = BSE()
    quote = bse.getQuote('532822')
    # quote = r"{'companyName': 'Vodafone Idea Ltd', 'currentValue': '9.51', 'change': '-0.04', 'pChange': '-0.42', 'updatedOn': '29 Apr 22 | 04:00 PM', 'priceBand': '', 'securityID': 'IDEA', 'scripCode': '532822', 'group': 'A  / S&P BSE 200', 'faceValue': '10.00', 'industry': 'Telecommunication', 'previousClose': '9.55', 'previousOpen': '9.63', 'dayHigh': '9.79', 'dayLow': '9.45', '52weekHigh': '16.79', '52weekLow': '4.55', 'weightedAvgPrice': '9.61', 'totalTradedValue': '21.61 Cr.', 'totalTradedQuantity': '224.79 Lakh', '2WeekAvgQuantity': '339.23 Lakh', 'marketCapFull': '30,545.02 Cr.', 'marketCapFreeFloat': '8,552.61 Cr.', 'upperPriceBand': '', 'lowerPriceBand': '', 'buy': {'1': {'quantity': '-', 'price': '0.00'}, '2': {'quantity': '-', 'price': '0.00'}, '3': {'quantity': '-', 'price': '0.00'}, '4': {'quantity': '-', 'price': '0.00'}, '5': {'quantity': '-', 'price': '0.00'}}, 'sell': {'1': {'price': '0.00', 'quantity': '-'}, '2': {'price': '0.00', 'quantity': '-'}, '3': {'price': '0.00', 'quantity': '-'}, '4': {'price': '0.00', 'quantity': '-'}, '5': {'price': '0.00', 'quantity': '-'}}}"
    parsed_json = json.dumps(quote, indent=4, sort_keys=True)
    print(parsed_json)