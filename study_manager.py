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
 
choice = input("Valintasi (1/2): ")

if choice  ==  "1":

    for day in range(1, 8):

        daily_hours = int(input(f"Kuinka monta tuntia opiskelit päivässä {day}? "))

        print(f"Opiskelupäivä {day}: {daily_hours} tuntia")

        total_hours += daily_hours

    average_hours = total_hours / 7

    print(f"Viikon opiskelutunnit yhteensä: {total_hours} tuntia")

    print(f"Päivittäinen keskiarvo: {average_hours:.2f} tuntia")

elif  choice == "2":

    day_count = 0

    answer = "k"

    while answer == "k":

        daily_hours = int(input("Anna opiskelutunnit: "))

        total_hours += daily_hours

        day_count += 1

        answer = input("Haluatko lisätä uuden päivän? (k/e): ")

    average_hours = total_hours / day_count


    print(f"Viikon opiskelutunnit yhteensä: {total_hours} tuntia  ")

    print(f"Opiskelupäiviä: {day_count}")

    print(f"Päivittäinen keskiarvo: {average_hours:.2f} tuntia")
