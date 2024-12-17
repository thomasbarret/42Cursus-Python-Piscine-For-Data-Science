class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        product = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {product}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        result = [v1 + v2 for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise."""
        result = [v1 - v2 for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
