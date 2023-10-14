class Persona:
  def __init__(self, nombre: str, edad: int, altura: str, sexo: str):
    self._nombre = nombre
    self._edad = edad
    self._altura = altura
    self._sexo = sexo

  def getNombre(self) -> str:
    return self._nombre

  def setNombre(self, nombre: str) -> None:
    self._nombre = nombre

  def getEdad(self) -> int:
    return self._edad

  def setEdad(self, edad: int) -> None:
    self._edad = edad

  def getAltura(self) -> str:
    return self._altura

  def setAltura(self, altura: str) -> None:
    self._altura = altura

  def getSexo(self) -> str:
    return self._sexo

  def setSexo(self, sexo: str) -> None:
    self._sexo = sexo
