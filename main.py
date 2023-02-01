from abc import ABCMeta, abstractmethod

# Interface
class DiscountRule(metaclass=ABCMeta):
  @abstractmethod
  def isOk(customer_data) -> bool:
    raise NotImplementedError()

class SeniorDiscountAgeRule(DiscountRule):
  def __init__(self, customer_data):
    self.customer_data = customer_data

  def isOk(self) -> bool:
    return self.customer_data["age"] >= 65

class SeniorDiscountReturnDriverLicenceRule(DiscountRule):
  def __init__(self, customer_data):
    self.customer_data = customer_data
  
  def isOk(self) -> bool:
    return self.customer_data["have_driver_licence"]

class FrequencyOfUseRule(DiscountRule):
  def __init__(self, customer_data):
    self.customer_data = customer_data
  
  def isOk(self)-> bool:
    return self.customer_data["frequency_of_use"] >= 5

# Policy
class SeniorDiscountPolicy():
  def __init__(self):
    self.rules = set()

  def add(self, rule):
    self.rules.add(rule)

  def complyWithAll(self):
    for rule in self.rules:
      if not rule:
        return False
    return True

class NormalDiscountPolicy():
  def __init__(self):
    self.rules = set()

  def add(self, rule):
    self.rules.add(rule)

  def complyWithAll(self):
    for rule in self.rules:
      if not rule:
        return False
    return True

class main():
  sinior_data = {
    "age": 50,
    "have_driver_licence": True,
    "frequency_of_use": 5
  }
  normal_data = {
    "age": 30,
    "have_driver_licence": False,
    "frequency_of_use": 3
  }

  # シニア割引対象
  senior_discount_policy = SeniorDiscountPolicy()
  senior_discount_policy.add(SeniorDiscountAgeRule(sinior_data).isOk())
  senior_discount_policy.add(SeniorDiscountReturnDriverLicenceRule(sinior_data).isOk())
  senior_discount_policy.add(FrequencyOfUseRule(sinior_data).isOk())
  # 一般割引対象
  normal_discount_policy = NormalDiscountPolicy()
  normal_discount_policy.add(FrequencyOfUseRule(normal_data).isOk())

  print(f'シニア割引対象：{senior_discount_policy.complyWithAll()}')
  print(f'一般割引対象：{normal_discount_policy.complyWithAll()}')

if __name__ == '__main__':
  main()