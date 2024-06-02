import math

############### Question 1 ###############
def f1score(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * ((precision * recall) / (precision + recall))
    return f1

print("Question 1:", round(f1score(tp=2, fp=3, fn=5), 2))

############### Question 2 ###############
def is_number(param):
    try:
        float(param)
        return True
    except ValueError:
        return False

print("Question 2:", is_number(1), is_number('n'))

############### Question 4 ###############
def calc_sig(x):
    return 1 / (1 + math.exp(-x))

print("Question 3:",round(calc_sig(2), 2))

############### Question 5 ###############
def calc_elu(x, alpha=0.01):
    return x if x > 0 else alpha * (math.exp(x) - 1)

print("Question 4:",round(calc_elu(-1), 2))

############### Question 6 ###############
def calc_relu(x):
    return x if x > 0 else 0

def calc_activation_func(x, act_name):
    if act_name == "sigmoid":
        return calc_sig(x)
    elif act_name == "relu":
        return calc_relu(x)

print("Question 5:",round(calc_activation_func(x=3, act_name='sigmoid'), 2))

############### Question 7-8 ###############
def calc_ae(y, y_hat):
    return abs(y - y_hat)

def calc_se(y, y_hat):
    return (y - y_hat) ** 2

print("Question 7:",calc_ae(2, 9))
print("Question 8:",calc_se(2, 1))

############### Question 9 ###############
def approx_cos(x, n):
    sum_cos = 0
    for i in range(n):
        sum_cos += ((x ** (2 * i)) / (math.factorial(2 * i))) * ((-1) ** i)
    return sum_cos

print("Question 9:",round(approx_cos(x=3.14, n=10), 2))

############### Question 10 ###############
def approx_sin(x, n):
    sum_sin = 0
    for i in range(n):
        sum_sin += ((x ** (2 * i + 1)) / (math.factorial(2 * i + 1))) * ((-1) ** i)
    return sum_sin

print("Question 10:",round(approx_sin(x=3.14, n=10), 4))

############### Question 11 ###############
def approx_sinh(x, n):
    sum_sinh = 0
    for i in range(n):
        sum_sinh += ((x ** (2 * i + 1)) / (math.factorial(2 * i + 1)))
    return sum_sinh

print("Question 11:",round(approx_sinh(x=3.14, n=10), 2))

############### Question 12 ###############
def approx_cosh(x, n):
    sum_cosh = 0
    for i in range(n):
        sum_cosh += ((x ** (2 * i)) / (math.factorial(2 * i)))
    return sum_cosh

print("Question 12:",round(approx_cosh(x=3.14, n=10), 2))

############### Question 13 ###############
def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

print("Example Answer 13:", md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))
