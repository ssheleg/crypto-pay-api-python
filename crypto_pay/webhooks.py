import hashlib
import hmac

class Webhooks:
    """
    Webhooks handler for CryptoPay.
    """

    SIGNATURE_HEADER_NAME = 'crypto-pay-api-signature'

    def __init__(self, token, options, update_handler):
        """
        Initialize the Webhooks handler.

        :param token: Your API token
        :param options: Webhook options
        :param update_handler: Function to handle updates
        """
        self.token = token
        self.options = options
        self.update_handler = update_handler

        if 'serverHostname' not in options or 'serverPort' not in options or 'path' not in options:
            raise ValueError('Webhook configuration is incomplete')

    def verify_update(self, update, signature):
        """
        Verify the update signature.

        :param update: Update data
        :param signature: Received signature
        :return: True if valid, False otherwise
        """
        secret = hashlib.sha256(self.token.encode()).digest()
        serialized_data = str(update).encode()
        hmac_signature = hmac.new(secret, serialized_data, hashlib.sha256).hexdigest()
        return hmac_signature == signature

    def handle_request(self, update, headers):
        """
        Handle incoming webhook requests.

        :param update: Update data
        :param headers: Request headers
        """
        if self.options.get('updateVerification', True):
            signature = headers.get(self.SIGNATURE_HEADER_NAME)
            if not signature or not self.verify_update(update, signature):
                raise ValueError('Wrong signature')
        
        self.update_handler(update)