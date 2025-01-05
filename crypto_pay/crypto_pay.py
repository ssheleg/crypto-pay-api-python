from flask import Flask, request, jsonify
from api import Api

class CryptoPay:
    """
    Main class for interacting with the CryptoPay API.
    """

    Assets = {
        'BTC': 'BTC',
        'ETH': 'ETH',
        'USDT': 'USDT',
        'LTC': 'LTC',
        'BNB': 'BNB',
        'TRX': 'TRX',
        'USDC': 'USDC',
    }

    def __init__(self, token, options=None):
        """
        Initialize the CryptoPay client.

        :param token: Your API token
        :param options: Optional client options
        """
        self.options = options or {}
        self.api = Api(token, self.options)

    def get_me(self):
        """Get basic information about the app."""
        return self.api.call_api('getMe')

    def create_invoice(self, asset, amount, options=None):
        """
        Create a new invoice.

        :param asset: Currency code
        :param amount: Amount of the invoice
        :param options: Additional options for the invoice
        :return: Created invoice object
        """
        return self.api.call_api('createInvoice', {'asset': asset, 'amount': amount, **(options or {})})

    def delete_invoice(self, invoice_id):
        """Delete an invoice created by your app."""
        return self.api.call_api('deleteInvoice', {'invoice_id': invoice_id})

    def create_check(self, asset, amount, pin_to_user_id=None, pin_to_username=None):
        """Create a new check."""
        return self.api.call_api('createCheck', {
            'asset': asset,
            'amount': amount,
            'pin_to_user_id': pin_to_user_id,
            'pin_to_username': pin_to_username
        })

    def delete_check(self, check_id):
        """Delete a check created by your app."""
        return self.api.call_api('deleteCheck', {'check_id': check_id})

    def transfer(self, user_id, asset, amount, spend_id, comment=None, disable_send_notification=False):
        """Transfer coins from your app's balance to a user."""
        return self.api.call_api('transfer', {
            'user_id': user_id,
            'asset': asset,
            'amount': amount,
            'spend_id': spend_id,
            'comment': comment,
            'disable_send_notification': disable_send_notification
        })

    def get_invoices(self, options=None):
        """Get invoices created by your app."""
        return self.api.call_api('getInvoices', options)

    def get_transfers(self, options=None):
        """Get transfers created by your app."""
        return self.api.call_api('getTransfers', options)

    def get_balance(self):
        """Get balance of your app."""
        return self.api.call_api('getBalance')

    def get_exchange_rates(self):
        """Get exchange rates of supported currencies."""
        return self.api.call_api('getExchangeRates')

    def get_currencies(self):
        """Get a list of supported currencies."""
        return self.api.call_api('getCurrencies')

    def get_stats(self, start_at=None, end_at=None):
        """Get app statistics."""
        return self.api.call_api('getStats', {'start_at': start_at, 'end_at': end_at})

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook endpoint for handling updates."""
    update = request.json
    # process the update here
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(port=5000)  # run Flask