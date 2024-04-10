#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    flag = 0
    
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            flag = 1
        except TypeError:
            print("wrong type")
            flag = 1
        except IndexError:
            print("out of range")
            flag = 0
        finally:
            if flag:
                flag = 0
                result_list.append(0)
            else:
                result_list.append(div_result)
    return result_list
