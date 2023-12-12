#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = {"Phython", "C", "Javascript"}
set_2 = {"Bash", "C", "Perl", "Ruby"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
