num1, num2 = map(int, input().split())


def get_hcf(x, y):
    while y:
        x, y = y, x%y
    return x


hcf_value = get_hcf(num1, num2)


print("HCF of num1: {} and num2: {} is => {}".format(num1, num2, hcf_value))