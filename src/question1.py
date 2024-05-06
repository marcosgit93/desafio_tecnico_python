class Contract:
    """
    Inicializa uma nova instância da classe `Contrato`.

    Args:
        id (int): O ID do contrato.
        debt (float): A dívida associada ao contrato.
    """
    def __init__(self, id: int, debt: float):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    """
    Retorna os IDs dos N contratos abertos com o maior saldo devedor, excluindo quaisquer contratos que tenham sido renegociados.
        Parâmetros:
            open_contracts (List[Contrato]): Uma lista de objetos Contrato representando os contratos abertos.
            renegotiated_contracts (List[int]): Uma lista de inteiros representando os IDs dos contratos renegociados.
            top_n (int): O número de contratos com o maior saldo devedor a serem retornados.

        Retorna:
            List[int]: Uma lista de inteiros representando os IDs dos N contratos abertos com o maior saldo devedor.
        """
    @staticmethod
    def get_top_N_open_contracts(open_contracts: list, renegotiated_contracts: list, top_n: int) -> int:
        open_contracts = [contract for contract in open_contracts if contract.id not in renegotiated_contracts]

        sorted_contracts = sorted(open_contracts, key=lambda x: x.debt, reverse=True)

        top_n_debtors = [contract.id for contract in sorted_contracts[:top_n]]
        return top_n_debtors


contracts = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]
renegotiated = [3]
top_n = 3

actual_open_contracts = Contracts.get_top_N_open_contracts(open_contracts=contracts,
                                                           renegotiated_contracts=renegotiated, top_n=top_n)
expected_open_contracts = [5, 4, 2]
assert expected_open_contracts == actual_open_contracts