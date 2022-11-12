# Tuple = Immutable data
status10 = (2, 5, 10)
player10 = [10, 5, 100]
print(player10)
lvup_player = [player10[i] + status10[i] for i in range(len(status10))]
print(lvup_player)

copy_status10 = list(status10)
del status10
status10 = copy_status10