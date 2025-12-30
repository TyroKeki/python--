from typing import Union

my_list: list[Union[int, str]] = [1,2,"itheima","itcast"]

num_and_char = int | str
def we_want_float(flt: num_and_char):
    return flt
we_want_float(2.2)
