from monitor import vitals_ok


# Tests
def test_vitals_ok():
    assert vitals_ok(98.6, 80, 95) == True
    assert vitals_ok(103, 80, 95) == False
    assert vitals_ok(98.6, 50, 95) == False
    assert vitals_ok(98.6, 80, 85) == False
    assert vitals_ok(94, 50, 85) == False
    assert vitals_ok(105, 110, 88) == False
    print("All tests passed.")


if __name__ == "__main__":
    test_vitals_ok()
