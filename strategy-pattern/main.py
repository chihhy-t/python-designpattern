from abc import ABCMeta, abstractmethod

class Customer(metaclass=ABCMeta):
	__normal_taxi_fare = 400
	def __init__(self):
		self.taxi_fare = self.__normal_taxi_fare

	@abstractmethod
	def getTaxiFare(self) -> int:
		raise NotImplementedError

class NormalCustomer(Customer):
	def getTaxiFare(self) -> int:
		return int(self.taxi_fare)

class SeniorCustomer(Customer):
	__senior_discount_rate = 10
	def getTaxiFare(self) -> int:
		return int(self.taxi_fare * (1 - (self.__senior_discount_rate / 100)))

class FamiliyCustomer(Customer):
	__family_discount_rate = 20
	def getTaxiFare(self) -> int:
		return int(self.taxi_fare * (1 - (self.__family_discount_rate / 100)))

class main():
	normal_customer = NormalCustomer()
	senior_customer = SeniorCustomer()
	family_customer = FamiliyCustomer()
	print(f"一般会員タクシー料金：¥{normal_customer.getTaxiFare()}")
	print(f"シニア会員タクシー料金：¥{senior_customer.getTaxiFare()}")
	print(f"家族会員タクシー料金：¥{family_customer.getTaxiFare()}")

if __name__ == '__main__':
	main()