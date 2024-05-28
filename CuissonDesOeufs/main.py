

import time

TIME_CUISSON=180


def lancement_timer(tps_cuisson):
   # print("Cuisson en cours", end="", flush=True)
    tps_cuisson_encours=tps_cuisson
    while not tps_cuisson_encours==0:


        if tps_cuisson==tps_cuisson_encours:
            tps_cuisson_encours = tps_cuisson_encours - 10
            print(f"\nCuisson en cours", end="", flush=True)
            for i in range(10):
                time.sleep(1)
                print(".", end="", flush=True)

        min = tps_cuisson_encours // 60  # division entière (pas de virgules)
        sec = tps_cuisson_encours - min * 60
        print(f"\nDurée restante :{min:02d}:{sec:02d}", end="", flush=True)
        tps_cuisson_encours = tps_cuisson_encours - 10
        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)

    return True


#Demander le choix du type de timer
while True:
    print("Quel type de cuisson pour les oeufs voulez vous ? \n 1 - Oeufs à la coque : 3 minutes \n 2 - Oeufs mollets : 6 minutes \n 3 - Oeufs durs : 9 minutes")
    choix_str = input("Faite votre choix : ")
    try:
        choix_int=int(choix_str)
        if choix_str == "1" or choix_str == "2" or choix_str == "3":
            break
        print(" Veuillez entrer 1, 2 ou 3 pour votre choix de cuisson \n")

    except:
        print("ERREUR !!! Veuillez une valuer demandé pour votre choix de cuisson \n")
        continue

time_cuisson_sec=TIME_CUISSON*choix_int

if lancement_timer(time_cuisson_sec):
    print("\nFini")







