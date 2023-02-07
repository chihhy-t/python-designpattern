# 配車が確定したらユーザーへ通知
# Observer: LINEメッセージ通知
# Subject: 車両の確定

from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
  @abstractmethod
  def update(self, generator):
    raise NotImplementedError()

class Subject(metaclass=ABCMeta):
  def __init__(self):
    self.__observers = []

  def addObserver(self, observer):
    self.__observers.append(observer)

  def deleteObserver(self, observer):
    self.__observers.remove(observer)

  def notifyObserver(self):
    for o in self.__observers:
      o.update(self)

  @abstractmethod
  def getTime(self):
    raise NotImplementedError()

class DispatchTaxiSubject(Subject):
  def __init__(self):
    self.__time = ""
    super(DispatchTaxiSubject, self).__init__()

  def getTime(self):
    return self.__time

  def execute(self):
    self.__time = "12:20"
    self.notifyObserver()

class ChatMessagingObserver(Observer):
  def update(self, generator):
    print("ChatMessagingObserver: {0}".format(generator.getTime()))

class main():
  dispatchTaxi = DispatchTaxiSubject()
  chatMessagingObserver = ChatMessagingObserver()
  dispatchTaxi.addObserver(chatMessagingObserver)
  dispatchTaxi.execute()

if __name__ == '__main__':
  main()