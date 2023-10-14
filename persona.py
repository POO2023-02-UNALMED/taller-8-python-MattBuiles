class Persona:
  def __init__(self, nombre: str, edad: int, altura: str, sexo: str):
    self._nombre = nombre
    self._edad = edad
    self._altura = altura
    self._sexo = sexo

  def get_nombre(self) -> str:
    return self._nombre

  def set_nombre(self, nombre: str) -> None:
    self._nombre = nombre

  def get_edad(self) -> int:
    return self._edad

  def set_edad(self, edad: int) -> None:
    self._edad = edad

  def get_altura(self) -> str:
    return self._altura

  def set_altura(self, altura: str) -> None:
    self._altura = altura

  def get_sexo(self) -> str:
    return self._sexo

  def set_sexo(self, sexo: str) -> None:
    self._sexo = sexo
