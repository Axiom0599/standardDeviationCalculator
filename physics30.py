def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    standard_deviation = variance ** 0.5
    return standard_deviation



n = 5
data_list = []
for i in range(n):
    acc = input("Enter acceleration ". format(i+1))
    data_list. append(float(acc))
print(data_list)

std_deviation = calculate_standard_deviation(data_list)
mean = calculate_mean(data_list)
print("Standard Deviation:", std_deviation)
print("Mean: ", mean)

