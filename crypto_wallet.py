# import ting the required libraries and dependencies:
import os 
import requests
from dotenv import load_dotenv
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3 import Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy
load_dotenv()
w3 =Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
# Making three functions for the following reasons:

## Function to automate generation of account:
def generate_account(w3):
    
    mnemonic = os.getenv('MNEMONIC')
    wallet = Wallet(mnemonic)
    private,public = wallet.derive_account('eth')
    account =Account.privateKeyToAccount(private)
    
    return account

## Function to get the balance of the account generated:
def get_balance(w3,address):
    
    wei_balance = w3.eth.get_balance(address)
    ether = w3.fromWei(wei_balance,'ether')
    
    return ether

## Funtion to send transaction from the account generated:
def send_transaction(w3,account,to,wage):
    
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)
    value = w3.toWei(wage,'ether')
    gas_estimate = w3.eth.estimateGas({'to' : to,'from': account.address, 'value' : value})
    
    raw_tx = {
        'to' : to,
        'from' : account.address,
        'value' : value,
        'gas' : gas_estimate,
        'gasPrice' : 0,
        'nonce' : w3.eth.getTransactionCount(account.address)
    }
    
    signed_tx = account.signTransaction(raw_tx)
    
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)