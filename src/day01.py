
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

def fuel_required_p2(mass):
    total_so_far = 0
    fuel = fuel_required(mass)
    while fuel > 0:
        total_so_far += fuel
        fuel = fuel_required(fuel)
    return total_so_far

def solve_part_2(filename):
    modules = fetch_data(filename)
    return total_fuel_p2(modules)

def total_fuel_p2(modules):
    requirements = (fuel_required_p2(m) for m in modules)
    return sum(requirements)
 



# ---- tests ---- #

def test_fuel_required():
    assert fuel_required(12) == 2
    assert fuel_required(1969) == 654

def test_total_fuel():
    assert total_fuel([12, 1969]) == 656

def test_solve_part_1():
    assert solve_part_1("input/day01.test.input.txt") == 656

def test_fuel_required_p2() :
    assert fuel_required_p2(14) == 2
    assert fuel_required_p2(1969) == 966
    assert fuel_required_p2(100756) == 50346

def test_total_fuel_p2():
    assert total_fuel_p2([100756, 1969]) == (50346 + 966)

if __name__ == "__main__":
    print(solve_part_2("input/day01.input.txt"))