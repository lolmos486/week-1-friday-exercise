from sum_list import addition


def test_addition_1():
    assert addition(2, 10, 30.5, 5.5) == 48
    print(test_addition_1)


def test_addition_2():
    assert addition(2, 10, 5.5) == 17.5
    print(test_addition_2)



def test_addition_3():
    assert addition(2, 2, 3) == 7
    print(test_addition_3)



def test_addition_4():
    assert addition(2, 30.5) == 32.5
    print(test_addition_4)

