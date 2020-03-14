from typing import NamedTuple, List

Contendent = NamedTuple("Contendent", [("name", str), ("price", int)])

def create_crew(hire_list: List[Contendent], given_money: int) -> List[Contendent]:
    """
    Create the biggest crew of the cheapest contendents with the given 
    budget.
    
    :param hire_list: the list of the contendents. 
    :type hire_list: List[Contendent]
    :param given_money: the budget.
    :type given_money: int
    :return: the biggest crew of the cheapest contendents with the given 
             budget.
    :rtype: List[Contendent]
    """
    # Your code here:
    sorted_list = sorted(hire_list, key=lambda contendent: contendent.price)

    count = 0
    current_price = 0
    for contendent in sorted_list:
        current_price += contendent.price
        if current_price <= given_money:
            count += 1
    
    return sorted_list[:count]