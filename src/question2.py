class Orders:

    @staticmethod
    def combine_orders(requests, n_max):
        """
        Combines orders based on the maximum limit allowed per trip.

        Args:
            requests (list): List of orders to be combined.
            n_max (int): Maximum limit allowed per trip.

        Returns:
            int: Number of trips needed to combine the orders.
        """
        requests.sort(reverse=True)

        num_trips = 0

        while requests:
            largest = requests.pop(0)

            if largest <= n_max and requests:
                for i, request in enumerate(requests):
                    if largest + request <= n_max:
                        requests.pop(i)
                        break

            num_trips += 1

        return num_trips


orders = [110, 30, 10]
n_max = 100
expected_orders = 2

how_many = Orders().combine_orders(orders, n_max)
assert how_many == expected_orders