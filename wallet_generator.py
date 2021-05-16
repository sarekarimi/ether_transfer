from .block_chain import *

## Creating Random Wallets :)

pubk = "0x64B58a15eBA5d8E50FE317E62062d5D3e4abB91f"
prik = "8e4f35ff384d570b59c99f1800d6776af7c84813a6aa38cc2c4251c968734cc3"
_file_name = "wallets_with_pk.json"
_file = open(_file_name, "w")
_file.write("{}")
_file.close()
_file_to_send = "wallets.json"
_file = open(_file_to_send, "w")
_file.write("[]")
_file.close()

n = w3.eth.get_transaction_count(pubk) 
for i in range(5000):
    acc = w3.eth.account.create("passwordIsSimple")
    print(acc.address, acc.privateKey.hex())
    _amount = float(random.randint(10**14, 10**16)) / 10**18
    trx = transfer(acc.address, _amount, prik, pubk,n)
    n += 1
    so_far = json.load(open(_file_name))

    so_far.update({
        acc.address: {
            "pk": acc.privateKey.hex(),
            "amount": _amount,
            "trx": trx
        }
    })
    to_send = json.load(open(_file_to_send))
    to_send.append(acc.address)
    json.dump(to_send,open(_file_to_send,"w"))
    json.dump(so_far,open(_file_name,"w"))