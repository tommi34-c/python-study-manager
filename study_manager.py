print("=== Python Study Manager ===")

student_name = input("Mikä on  nimesi? ")

programming_language = input("Mitä ohjelmointi kieltä opiskelet? ")

study_hours = int(input("Kuinka tuntia opiskelit tänään? "))

weekly_hours = study_hours * 7

print(f"Opiskelija: {student_name}")

print(f"Ohjelmointi kieli: {programming_language}")

print(f"Opiskeluaika: {study_hours} tuntia")

print(f"Viikoittainen opiskeluaika: {weekly_hours} tuntia")

if study_hours >= 4:
    print("Erinomainen opiskelupäivä!")

elif study_hours >= 2:
    print("Hyvää edistymistä!")

else:
    print("Jatka harjoittelua!")

total_hours = 0

for day in range(1, 8):
    daily_hours = int(input(f"Kuinka monta tuntia opiskelit päivässä {day}? "))

    print(f"Opiskelupäivä {day}: {daily_hours} tuntia")

    total_hours += daily_hours

print(f"Viikon opiskelutunnit yhteensä: {total_hours} tuntia  ")

average_hours = total_hours / 7

print(f"Päivittäinen keskiarvo: {average_hours} tuntia")