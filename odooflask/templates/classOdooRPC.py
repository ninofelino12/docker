from odoorpc import OdooRPC

class MyOdooRPC(OdooRPC):

    def __init__(self, url, login, password):
        super().__init__(url, login, password)

    def my_custom_method(self, arg1, arg2):
        """
        This is a custom method that adds to OdooRPC.

        Args:
            arg1: The first argument.
            arg2: The second argument.

        Returns:
            The result of the method.
        """
        return self.execute('my_custom_method', arg1, arg2)


my_odoo_rpc = MyOdooRPC('http://localhost:8069', 'admin', 'admin')

# Call the custom method.
result = my_odoo_rpc.my_custom_method('Hello', 'World')

# Print the result.
print(result)