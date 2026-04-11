from typing import Protocol, runtime_checkable
@runtime_checkable
class Serializable(Protocol):  
    def to_dict(self) -> dict: ...       
    def to_json(self) -> str: ...
   
class User:
    def __init__(self, name:str) -> None:
        self.name = name
    def to_dict(self) -> dict:
        return {"name": self.name}
    def to_json(self) -> str:
        return "{'name': '" + self.name + "'}"
class Product:
    def __init__(self, name:str) -> None:
        self.name = name
    def to_dict(self) -> dict:
        return {"name": self.name}
    def to_json(self) -> str:
        return "{'name': '" + self.name + "'}"
    
class BrokenItem:
    def __init__(self, name:str) -> None:
        self.name = name
    def to_dict(self) -> dict:
        return {"name": self.name}    
    
def export(item: Serializable) -> str:
    return item.to_json()
print(export(User("didier")))
print(export(Product("ballon")))
print(export(BrokenItem("ballon")))
print(isinstance(User, Serializable))
print(isinstance(Product, Serializable))
print(isinstance(BrokenItem, Serializable))