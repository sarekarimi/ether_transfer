import random
import json
from web3 import Web3
# import json

MAIN_URL = "https://mainnet.infura.io/v3/bb055071bba745488eda95512a6d0035"
URL = 'https://8cf41633363c49a584fbfb0b556a5927.ropsten.rpc.rivet.cloud/'
URL = 'wss://ropsten.infura.io/ws/v3/bb055071bba745488eda95512a6d0035'

w3 = Web3(Web3.WebsocketProvider(URL))
# w3 = Web3(Web3.HTTPProvider(URL))


def _checking(_addr):
    '''
    ورودی تابع ک استرینگ است که چک میشمود ایا ادرس معبتری هست یا خیر

    false یا addrress درنهایت
    خارح میشود
    '''
    if not isinstance(_addr, str):
        print("ادرس بد وارد کردی باید یک استرینگ باشه")
        return False
    try:
        if not w3.isConnected():
            print("نت مشکل داره ")
            return False
        addr_ = Web3.toChecksumAddress(_addr)
        if not _addr:
            print("ادرس بدی وارد کردی شرمنده تم")
            return False
        return addr_
    except Exception as e:
        print(e)
        print("یه مشکلی وجود داره ×ـ× مثلا نتت ضعیفه")
        return False


def balance(_addr: str) -> float:
    """
    اینجا ادرس خواسته رو به تابع بدید
    توی خروجی یه عدد میده که همون باقیمانده ی حسابش هستش :)
    """
    addr_ = _checking(_addr)
    return float(w3.eth.get_balance(addr_) / 10**18)



def transfer(_to_addr: str, _value: float, private_key: str, public_key: str ,_nounce:int ):
    to_addr_ = _checking(_to_addr)
    public_key = _checking(public_key)
    
    if to_addr_ and public_key:
        try:
            if balance(public_key) < _value:
                print("پول ت کمه ، نمیتونی کمک کنی ")
                return False
            p = w3.eth.gas_price
            
            trancation = {
                'from': public_key,
                'to': to_addr_,
                "gas": "0x200000",
                "gasPrice": p,
                "nonce": _nounce,
                "value": int(_value * 10**18),
            }
            raw_trx = w3.eth.account.privateKeyToAccount(
                private_key).sign_transaction(trancation)
            res = w3.eth.send_raw_transaction(raw_trx.rawTransaction).hex()
            return res
        except Exception as e:
            print(e)
            print("یک اتفاقی افتاده که من نمیدونم ....")
            return 0

    

####################### My Code #######################

# open json file 
with open('wallets.json') as wallets_data:    
    wallet = json.load(wallets_data)
    sum=each_balance = 0
    list_account_addr = {}
    wallet_length = len(wallet)


# read 20 random account address and calculate balance
# create dictionary for transfer loop  
    for i in range(10):
        index = random.randint(1,wallet_length)
        each_balance = balance(wallet[index])
        sum = sum + each_balance
        list_account_addr[wallet[index]]=each_balance

    average = sum/wallet_length
    below_average = average/10


# transfer ether to accounts and create transaction file
with open("transferlistfile.txt", "a") as transfer_list:
    _public_key = Web3.toChecksumAddress("0xAf77fB90baCE88edad8be674232C4a072BdC29A3")
    _nounce = w3.eth.get_transaction_count(_public_key )
    count_below_average = 0
    for key,value in list_account_addr.items():
        if value < below_average:
            transfer_list.write(str(transfer(key,
                0.005,
                "47d88b93b485140ee774fde779906182c2f419528793411e60029d09c60f371d",
                "0x036e42A6554089685809c893758194D0b00c6726",
                _nounce )))
            transfer_list.write("\n")   
            _nounce += 1
            count_below_average += 1
    print ("count_below_average : ", count_below_average)
    print ("Done")
 