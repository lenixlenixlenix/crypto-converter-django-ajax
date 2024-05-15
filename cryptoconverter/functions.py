import requests
import csv

class CryptoClass():
    
    @staticmethod
    def convert_crypto(currency1: int, currency2: int, amount: int):
        with open("currency_names.csv", newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            val_curr1 = float(data[currency1-1][1])
            val_curr2 = float(data[currency2-1][1])

            result = val_curr1 / val_curr2 * amount
            return result

    @staticmethod
    def update():
        url = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD"
        response = requests.get(url)

        with open("currency_names.csv", 'w', newline="") as file:
            writer = csv.writer(file)
            for i in range(0, 100):
                currency_sign = (((response.json()["Data"])[i])["CoinInfo"])["Name"]
                try:
                    currency_amount = ((((response.json()["Data"])[i])["RAW"])["USD"])["PRICE"]
                except KeyError:
                    pass

                writer.writerow([currency_sign, currency_amount])
        
    
    @staticmethod
    def return_names():
        with open("currency_names.csv", newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            names_list = []
            for i in range(0, 100):
                names_list.append(data[i][0])
            
            return names_list
