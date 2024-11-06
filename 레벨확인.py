current_count = float(input("현재 횟수를 입력해주세요: "))
current_level = float(input("현재 레벨을 입력해주세요: "))
discord_levelup = 100.0 / float(input("100분의 몇 인가요? :"))

test = current_count / current_level
up = 0

while test >= discord_levelup:
    current_count += 1
    current_level += 1
    up += 1
    test = current_count / current_level
L = discord_levelup - test


print(f" 정상값인 {discord_levelup:.0f}보다 작을려면 {up}번 증가해야하고 {discord_levelup:.0f}보다 {L:.2f}만큼 작아.")
