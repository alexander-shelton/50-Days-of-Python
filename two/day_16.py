#!/usr/bin/env python3
#
# Day 16: Sum the List

def sum_list(nested_list: list) -> int:
    return sum([nested_list[i][j] for i in range(len(nested_list)) for j in range(len(nested_list[i]))])
    #
    # Visualize the list comprehension:
    # return sum(
    #     [
    #         nested_list[i][j] 
    #         for i in range(
    #             len(nested_list)
    #         ) 
    #         for j in range(
    #             len(nested_list[i])
    #         )
    #     ]
    # )


## Extra Challenge: Unpack A Nest
def reversed_list(nested_list: list) -> list:
    return list(set([nested_list[i][j] for i in range(len(nested_list)) for j in range(len(nested_list[i])) if nested_list[i][j] in (34, 67, 78)]))
    #
    # Visualize the list comprehension:
    # return list(
    #     set(
    #         [
    #             nested_list[i][j] 
    #             for i in range(
    #                 len(nested_list)
    #             ) 
    #             for j in range(
    #                 len(nested_list[i])
    #             ) 
    #             if nested_list[i][j] in (34, 67, 78)
    #         ]
    #     )
    # )
