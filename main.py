import requests
import json
import datetime
import cbpro



def main():
    sandbox_website = "https://public.sandbox.exchange.coinbase.com"
    sandbox_rest = "https://api-public.sandbox.exchange.coinbase.com"

    data = open("cbpro.cfg", 'r').read().splitlines()

    api_key = data[0]
    api_secret = data[1]
    api_passphrase = data[2]

    auth_client = cbpro.AuthenticatedClient(api_key, api_secret, api_passphrase)

    id_list = {}

    for each in auth_client.get_accounts():
        #print(each)
        if float(each['balance']) > 0:
            id_list[each['currency']] = each['id']

    history_gen = auth_client.get_account_history(id_list['ETH'])
    history = list(history_gen)
    for record in history:
        print(record)


if __name__ == "__main__":
    main()