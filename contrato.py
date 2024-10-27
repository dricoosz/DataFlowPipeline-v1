from datetime import datetime, time
from pydantic import BaseModel, EmailStr, field_validator, PositiveFloat, PositiveInt
from typing import Tuple
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "chatGPT"
    produto3 = "Llamma"
    

class Vendas(BaseModel):
    """
    Modelo de dados para representar uma venda.

    A classe `Vendas` define a estrutura dos dados para representar uma venda, incluindo informações sobre o 
    cliente, o produto vendido, a data da transação, o valor, e a quantidade do produto.

    Atributos:
        email (EmailStr): O e-mail do cliente que realizou a compra. Deve ser um e-mail válido.\n
        data (datetime): A data e a hora em que a venda foi realizada.\n
        valor (PositiveFloat): O valor da venda. Deve ser um número positivo.\n
        quantidade (PositiveInt): A quantidade do produto vendido. Deve ser um número inteiro positivo.\n
        produto (ProdutoEnum): O produto vendido, selecionado a partir de uma enumeração predefinida de produtos.\n

    Validações:
        - `produto`: Valida que o produto fornecido pertence à enumeração `ProdutoEnum`.

    Exemplo:
        ```python
        venda = Vendas(
            email="cliente@example.com",
            data=datetime(2024, 10, 22, 14, 30),
            valor=199.99,
            quantidade=2,
            produto=ProdutoEnum.produto1
        )
        ```
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
    
    @field_validator('produto')
    def categoria_produto_enum(cls, v):
        """
        Validador para garantir que o valor do campo 'produto' seja uma instância da enumeração `ProdutoEnum`.
        
        Args:
            v (str): O valor do campo 'produto'.

        Returns:
            ProdutoEnum: O valor validado, que corresponde a um dos itens da enumeração `ProdutoEnum`.

        Raises:
            ValueError: Se o valor não corresponder a um dos produtos da enumeração.
        """
        return v