import random #ok 2
def two_dice_roll():
    dice1 = random.randrange(6) + 1
    dice2 = random.randrange(6) + 1
    return dice1 + dice2
result_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for turn in range(1000):
    result = two_dice_roll()
    result_dict[result] += 1
print("Total".rjust(16), "|", "Simulated".rjust(16), "|", "Expected".rjust(16))
for n in range(2, 13):
    sim_result = str("%.2f" % (result_dict[n] / 1000 * 100))
    if n <= 7:
        exp_result = str("%.2f" % ((n - 1) / 36 * 100))
    else:
        exp_result = str("%.2f" % ((12 - n + 1) / 36 * 100))
    print(str(n).rjust(16), "|", sim_result.rjust(16), "|", exp_result.rjust(16))