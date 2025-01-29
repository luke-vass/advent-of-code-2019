
def fuel_required(mass):
    return mass // 3 - 2

def total_fuel(modules):
    requirements = (fuel_required(m) for m in modules)
    return sum(requirements)

def fetch_data(filename):
    with open(filename, 'r') as f:
       for line in f:
           yield int(line)

def solve_part_1(filename):
    modules = fetch_data(filename)
    return total_fuel(modules)


# ---- tests ---- #

def test_fuel_required():
    assert fuel_required(12) == 2
    assert fuel_required(1969) == 654

def test_total_fuel():
    assert total_fuel([12, 1969]) == 656

def test_solve_part_1():
    assert solve_part_1("input/day01.input.txt") == 656
