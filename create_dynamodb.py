from chalicelib.adapters.repositories.entity.products import ProductTable

def create_table():
    if not ProductTable.exists():
        ProductTable.create_table(wait=True)
