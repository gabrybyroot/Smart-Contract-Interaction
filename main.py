from web3 import Web3
import json

class SmartContractInteraction:
    def __init__(self, contract_address, contract_abi_json, my_address, private_key):
        # Initialize Web3 and contract details
        self.w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
        self.contract_address = contract_address
        self.contract_abi = json.loads(contract_abi_json)
        self.my_address = my_address
        self.private_key = private_key

        # Check connection to the Binance Smart Chain
        if not self.w3.isConnected():
            raise ConnectionError("Not connected. Check your settings.")

        # Create a contract instance
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def check_connection(self):
        return self.w3.isConnected()

    def withdraw(self):
        # Implement the logic for executing the withdrawal
        pass

    def claim(self):
        # Implement the logic for executing the claim
        pass

    # Add other functions as needed

    def execute_transaction(self, function, *args):
        # Build and execute a transaction for a given function
        nonce = self.w3.eth.getTransactionCount(self.my_address)
        transaction = function(*args).buildTransaction({
            'gas': 200000,
            'gasPrice': self.w3.toWei('10', 'gwei'),
            'nonce': nonce,
        })

        signed_txn = self.w3.eth.account.signTransaction(transaction, self.private_key)
        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        txn_receipt = self.w3.eth.waitForTransactionReceipt(txn_hash)

        return txn_receipt, txn_hash, signed_txn

# Example usage:
contract_address = 'Insert address smart contract'
contract_abi_json = '...'  # Insert the complete ABI here
my_address = "Insert your pubblic wallet address here"
private_key = ''  # Insert your private key here

# Create an instance of the SmartContractInteraction class
smart_contract_interaction = SmartContractInteraction(contract_address, contract_abi_json, my_address, private_key)

# Example of using the functions
if smart_contract_interaction.check_connection():
    print("Connected successfully!")

    # Example of calling the withdraw function
    withdraw_receipt, withdraw_hash, withdraw_signed_txn = smart_contract_interaction.execute_transaction(
        smart_contract_interaction.contract.functions.withdraw
    )
    print('Withdraw Transaction Receipt:', withdraw_receipt, withdraw_hash, withdraw_signed_txn)

    # Example of calling the claim function
    claim_receipt, claim_hash, claim_signed_txn = smart_contract_interaction.execute_transaction(
        smart_contract_interaction.contract.functions.claim
    )
    print('Claim Transaction Receipt:', claim_receipt, claim_hash, claim_signed_txn)

else:
    print("Not connected. Check your settings.")
