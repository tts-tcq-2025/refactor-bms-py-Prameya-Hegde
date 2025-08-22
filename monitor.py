from time import sleep
import sys


def check_vitals(temperature, pulseRate, spo2):
    issues = []
    if temperature > 102 or temperature < 95:
        issues.append('Temperature critical!')
    if pulseRate < 60 or pulseRate > 100:
        issues.append('Pulse Rate is out of range!')
    if spo2 < 90:
        issues.append('Oxygen Saturation out of range!')
    return issues


def show_alert(message):
    print(message)
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)
    print()  # Move to next line after animation


# Main_function
def vitals_ok(temperature, pulseRate, spo2):
    issues = check_vitals(temperature, pulseRate, spo2)
    for issue in issues:
        show_alert(issue)
    return len(issues) == 0

