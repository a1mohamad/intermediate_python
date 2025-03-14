averages_A, averages_B, averages = dict(), dict(), dict()
class A:
    def __init__(self):
        number = int(input())
        self.number = number
    def get_info(self):
        age_list = [int(x) for x in input().split()]
        height_list = [int(x) for x in input().split()]
        weight_list = [int(x) for x in input().split()]
        return age_list, height_list, weight_list
    def average(self, age_list, height_list, weight_list):
        average_age = sum(age_list) / self.number
        average_height = sum(height_list) / self.number
        averages_A['average_height'] = average_height
        average_weight = sum(weight_list) / self.number
        averages_A['average_weight'] = average_weight
        averages['A'] = averages_A
        return print(f'{average_age}\n{average_height}\n{average_weight}')
        
class B:
    def __init__(self):
        number = int(input())
        self.number = number
    def get_info(self):
        age_list = [int(x) for x in input().split()]
        height_list = [int(x) for x in input().split()]
        weight_list = [int(x) for x in input().split()]
        return age_list, height_list, weight_list
    def average(self, age_list, height_list, weight_list):
        average_age = sum(age_list) / self.number
        average_height = sum(height_list) / self.number
        averages_B['average_height'] = average_height
        average_weight = sum(weight_list) / self.number
        averages_B['average_weight'] = average_weight
        averages['B'] = averages_B
        return print(f'{average_age}\n{average_height}\n{average_weight}')

students_A = A()
ageA, heightA, weightA = students_A.get_info()
students_B = B()
ageB, heightB, weightB = students_B.get_info()
students_A.average(ageA, heightA, weightA)
students_B.average(ageB, heightB, weightB)
sorted_averages = sorted(averages, key=lambda k:(-averages[k]['average_height'], averages[k]['average_weight']))
if averages['A'] == averages['B']:
    result = 'Same'
else:
    result = sorted_averages[0]
print(result)