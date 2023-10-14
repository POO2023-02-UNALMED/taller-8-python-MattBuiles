class Deportista:
  def __init__(self, deporte: str, añosPracticando: int):
    self._deporte = deporte
    self._añosPracticando = añosPracticando

  def getDeporte(self) -> str:
    return self._deporte

  def setDeporte(self, deporte: str):
    self._deporte = deporte

  def getAñosPracticando(self) -> int:
    return self._añosPracticando

  def setAñosPracticando(self, añosPracticando: int):
    self._añosPracticando = añosPracticando
