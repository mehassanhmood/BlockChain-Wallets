# Importing libraries and dependencies:
import streamlit as st
from dataclasses import dataclass
from typing import Any,List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
# importing the three created functions from the crypto wallet file:
from crypto_wallet import w3,generate_account,get_balance,send_transaction
# instantiating the function to generate the ethereum account :
account = generate_account(w3)
sender = account.address
# candidate data base:
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "kendall.jpeg"]
}
# list of first names of the candidates:
people = ["Lane", "Ash", "Jo", "Kendall"]
# function to seperate each attribute of the related candidate:
def get_people():
    
    db_list = list(candidate_database.values())
    for i in range(len(people)):
        st.image(db_list[i][4],width=200)
        st.write('Name :' ,db_list[i][0])
        st.write('Ethereum Account Address :' ,db_list[i][1])
        st.write("Hourly Rate per Ether: ", db_list[i][3], 'eth')
        st.text('\n')
# Header for the app , which is self explanatory:
st.markdown('# Fintech Finder')
st.markdown('## Hire a Fintech Professional')
st.text('\n')
# side bar to show the balance in the clients account in ether :
st.sidebar.markdown('## Client, Account Address and Ethernet Balanace in Ether')
# to show the public address of the clients account:
st.sidebar.write(account.address)
# retreiving the balance from the account bu utilizing the function from crypto_wallet file:
balance = get_balance(w3,account.address)
st.sidebar.write(balance)
# a dropdown menue for the selection of the prefessional by their first name:
person = st.sidebar.selectbox('Select a Person',people)
#To select the number of hours the clients need to hire the professional for:
hours = st.sidebar.number_input('Number of Hours')
# to display the account address ,names from which the candidate will be selected and the cost of the time the candidate is hired for:
st.sidebar.markdown('## Candidate Name, Hourly Rate and Ethereum Account')
candidate = candidate_database[person][0]
st.sidebar.write(candidate)
hourly_rate =candidate_database[person][3]
st.sidebar.write(hourly_rate)
candidate_address = candidate_database[person][1]
st.sidebar.write(candidate_address)
st.sidebar.markdown('## Total wage in Ether')
# To display the total wage:
if st.button('Calculate price'):
    wage = hours*hourly_rate
    st.sidebar.write(wage)
wage = hours*hourly_rate
#To send the transaction:
if st.sidebar.button('Send Transaction'):
    st.sidebar.markdown('### Validated Transaction Hash:')
    transaction_hash = send_transaction(w3,account,to=candidate_address,wage=wage)
    st.sidebar.write(transaction_hash)
get_people()