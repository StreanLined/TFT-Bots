from pyautogui import *
from tkinter import *
from PIL import ImageTk
import pyautogui, keyboard


#Store Size: (region=(480, 928, 997, 143))
#Store 1: (region=(480,928,192,143))
#Store 2: (region=(681,928,192,143))
#Store 3: (region=(882,928,192,143))
#Store 4: (region=(1084,928,192,143))
#Store 5: (region=(1285,928,192,143))
#################################################################################################################################################
# Cost
#1 Cost
cost_1 = ["Ashe", "Blitzcrank", "Galio", "Gangplank", "Kayle", "Lulu", "Lux", "Nasus", "Poppy", "Renekton", "Sylas", "Talon", "Wukong"]

#2 Cost
cost_2 = ["Annie", "Camille", "Draven", "Ezreal", "Fiora", "Jinx", "Lee Sin", "Malphite", "Rell", "Sivir", "Vi", "Yasuo", "Yuumi"]

#3 Cost
cost_3 = ["Alistar", "Cho'Gath", "Jax", "Kai'sa", "LeBlanc", "Nilah", "Rammus", "Riven", "Senna", "Sona", "Vayne", "Vel'Koz", "Zoe"]

#4 Cost
cost_4 = ["Aurelion Sol", "Bel'Veth", "Ekko", "Miss Fortune", "Samira", "Sejuani", "Sett", "Soraka", "Taliyah", "Viego", "Zac", "Zed"]

#5 Cost
cost_5 = ["Aphelios", "Fiddlesticks", "Janna", "Leona", "Mordekaiser", "Nunu", "Syndra", "Urgot"]

#################################################################################################################################################
# Comps
#Ox Force
Ox_Force_trait = ["Alistar", "Annie", "Aphelios", "Fiora", "Talon", "Viego"]

#Mascot
Mascot_trait = ["Alistar", "Galio", "Malphite", "Nunu", "Yuumi", "Nasus"]

#Aegis
Aegies_trait = ["Alistar", "Ekko", "Leona", "Vi"]

#Gadgeteen
Gadgeteen_trait = ["Annie", "Lulu", "Nunu", "Poppy", "Zoe"]

#Spellslinger
Spellslinger_trait = ["Annie", "Janna", "LeBlanc", "Lux", "Sona", "Taliyah"]

#Sureshot
Sureshot_trait = ["Aphelios", "Samira", "Senna", "Sivir"]

#Arsenal
Arsenal_trait = ["Aphelios"]

#LaserCorps
Lasercorps_trait = ["Ashe", "Mordekaiser", "Renekton", "Sejuani", "Senna", "Yasuo", "Zed"]

#Recon
Recon_trait = ["Ashe", "Ezreal", "Kai'Sa", "Vayne"]

#Threat
Threat_trait = ["Aurelion Sol", "Bel'Veth", "Cho'Gath", "Fiddlesticks", "Rammus", "Urgot", "Vel'koz", "Zac"]

#A.D.M.I.N
Admin_trait = ["Blitzcrank", "Camille", "LeBlanc", "Soraka"]

#Brawler
Brawler_trait = ["Blitzcrank", "Jax", "Lee Sin", "Renekton", "Riven", "Sejuani", "Vi"]

#Renegade
Renegade_trait = ["Camille", "Leona", "Sylas", "Talon", "Viego"]

#Mecha:Prime
Mecha_trait = ["Draven", "Jax", "Leona", "Sett", "Wukong"]

#Ace
Ace_trait = ["Draven", "Miss Fortune", "Mordekaiser", "Samira"]

#Star Guardian
Starguardian_trait = ["Ekko", "Kai'Sa", "Lux", "Nilah", "Rell", "Syndra", "Taliyah", "Yuumi"]

#Prankster
Prankster_trait = ["Ekko", "Jinx", "Zoe"]

#The Underground
Underground_trait = ["Ezreal", "Kayle", "Samira", "Sona", "Vi"]

#Corrupted
Corrupted_trait = ["Fiddlesticks"]

#Duelist
Duelist_trait = ["Fiora", "Gangplank", "Kayle", "Nilah", "Vayne", "Yasuo", "Zed"]

#Civilian
Civilian_trait = ["Galio", "Sivir", "Janna"]

#Supers
Supers_trait = ["Gangplank", "Lee Sin", "Malphite"]

#Forecaster
Forecaster_trait = ["Janna"]

#Anima Squad
Animasquad_trait = ["Jinx", "Miss Fortune", "Nasus", "Riven", "Sylas", "Vayne"]

#Hacker
Hacker_trait = ["LeBlanc", "Zed", "Zoe"]

#Heart
Heart_trait = ["Lee Sin", "Lulu", "Sona", "Soraka", "Syndra", "Yuumi"]

#Defender
Defender_trait = ["Poppy", "Rell", "Riven", "Sett", "Wukong"]

#################################################################################################################################################
#Image Association
Alistar_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Alistar.png"
Annie_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Annie.png"
Aphelios_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Aphelios.png"
Ashe_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Ashe.png"
Aurelion_Sol_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Aurelion Sol.png"
Bel_Veth_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Bel'Veth.png"
Blitzcrank_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Blitzcrank.png"
Camille_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Camille.png"
Cho_Gath_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Cho'Gath.png"
Draven_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Draven.png"
Ekko_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Ekko.png"
Ezreal_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Ezreal.png"
Fiddlesticks_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Fiddlesticks.png"
Fiora_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Fiora.png"
Galio_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Galio.png"
Gangplank_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Gangplank.png"
Janna_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Janna.png"
Jax_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Jax.png"
Jinx_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Jinx.png"
Kai_Sa_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Kai'Sa.png"
Kayle_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Kayle.png"
LeBlanc_png = "C:\Python\TFT Bot Intermediate Image\Set 8\LeBlanc.png"
Lee_Sin_png = "C:\Python\TFT Bot Intermediate Image\Set 8\LeeSin.png"
Leona_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Leona.png"
Lulu_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Lulu.png"
Lux_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Lux.png"
Malphite_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Malphite.png"
Miss_Fortune_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Miss Fortune.png"
Mordekaiser_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Mordekaiser.png"
Nasus_png = "C:\Python\TFT Bot Intermediate Image\Set 8\\Nasus.png"
Nilah_png = "C:\Python\TFT Bot Intermediate Image\Set 8\\Nilah.png"
Nunu_png = "C:\Python\TFT Bot Intermediate Image\Set 8\\Nunu.png"
Poppy_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Poppy.png"
Rammus_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Rammus.png"
Rell_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Rell.png"
Renekton_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Renekton.png"
Riven_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Riven.png"
Samira_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Samira.png"
Sejuani_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Sejuani.png"
Senna_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Senna.png"
Sett_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Sett.png"
Sivir_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Sivir.png"
Sona_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Sona.png"
Soraka_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Soraka.png"
Sylas_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Sylas.png"
Syndra_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Syndra.png"
Taliyah_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Taliyah.png"
Talon_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Talon.png"
Urgot_png = "C:\Python\TFT Bot Intermediate Image\Set 8\\Urgot.png"
Vayne_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Vayne.png"
Vel_Koz_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Vel'Koz.png"
Vi_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Vi.png"
Viego_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Viego.png"
Wukong_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Wukong.png"
Yasuo_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Yasuo.png"
Yuumi_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Yuumi.png"
Zac_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Zac.png"
Zed_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Zed.png"
Zoe_png = "C:\Python\TFT Bot Intermediate Image\Set 8\Zoe.png"
#################################################################################################################################################
#Association
Alistar = Alistar_png, cost_3[0], Ox_Force_trait[0], Mascot_trait[0], Aegies_trait[0]
Annie = Annie_png, cost_2[0], Ox_Force_trait[1], Gadgeteen_trait[0], Spellslinger_trait[0]
Aphelios = Aphelios_png, cost_5[0], Sureshot_trait[0], Arsenal_trait[0]
Ashe = Ashe_png, cost_1[0], Lasercorps_trait[0], Recon_trait[0]
Aurelion_Sol = Aurelion_Sol_png, cost_4[0]
Bel_Veth = Bel_Veth_png, cost_4[1]
Blitzcrank = Blitzcrank_png, cost_1[1], Admin_trait[0], Brawler_trait[0]
Camille = Camille_png, cost_2[1], Admin_trait[1], Renegade_trait[0]
Cho_Gath = Cho_Gath_png, cost_3[1]
Draven = Draven_png, cost_2[2], Mecha_trait[0], Ace_trait[0]
Ekko = Ekko_png, cost_4[2], Starguardian_trait[0], Aegies_trait[1], Prankster_trait[0]
Ezreal = Ezreal_png, cost_2[3], Recon_trait[1], Underground_trait[0]
Fiddlesticks = Fiddlesticks_png, cost_5[1], Threat_trait[3], Corrupted_trait[0]
Fiora = Fiora_png, cost_2[4], Ox_Force_trait[3], Duelist_trait[0]
Galio = Galio_png, cost_1[2], Mascot_trait[1], Civilian_trait[0]
Gangplank = Gangplank_png, cost_1[3], Duelist_trait[1], Supers_trait[0]
Janna = Janna_png, cost_5[2], Spellslinger_trait[1], Civilian_trait[2], Forecaster_trait[0]
Jax = Jax_png, cost_3[2], Brawler_trait[1], Mecha_trait[1]
Jinx = Jinx_png, cost_2[5], Prankster_trait[1], Animasquad_trait[0]
Kai_Sa = Kai_Sa_png, cost_3[3], Recon_trait[2], Starguardian_trait[1]
Kayle = Kayle_png, cost_1[4], Underground_trait[1], Duelist_trait[2]
LeBlanc = LeBlanc_png, cost_3[4], Hacker_trait[0], Spellslinger_trait[2], Admin_trait[2]
Lee_Sin = Lee_Sin_png, cost_2[6], Brawler_trait[2], Supers_trait[1], Heart_trait[0]
Leona = Leona_png, cost_5[3], Renegade_trait[1], Aegies_trait[2], Mecha_trait[2]
Lulu = Lulu_png, cost_1[5], Gadgeteen_trait[1], Heart_trait[1]
Lux = Lux_png, cost_1[6], Spellslinger_trait[3], Starguardian_trait[2]
Malphite = Malphite_png, cost_2[7], Mascot_trait[2], Supers_trait[2]
Miss_Fortune = Miss_Fortune_png, cost_4[3], Ace_trait[1], Animasquad_trait[1]
Mordekaiser = Mordekaiser_png, cost_5[4], Lasercorps_trait[1], Ace_trait[2]
Nasus = Nasus_png, cost_1[7], Mascot_trait[5], Animasquad_trait[2]
Nilah = Nilah_png, cost_3[5], Starguardian_trait[3], Duelist_trait[3]
Nunu = Nunu_png, cost_5[5], Mascot_trait[3], Gadgeteen_trait[2]
Poppy = Poppy_png, cost_1[8], Gadgeteen_trait[3], Defender_trait[0]
Rammus = Rammus_png, cost_3[6]
Rell = Rell_png, cost_2[8], Starguardian_trait[4], Defender_trait[1]
Renekton = Renekton_png, cost_1[9], Lasercorps_trait[2], Brawler_trait[3]
Riven = Riven_png, cost_3[7], Animasquad_trait[3], Brawler_trait[4], Defender_trait[2]
Samira = Samira_png, cost_4[4], Sureshot_trait[1], Underground_trait[2], Ace_trait[3]
Sejuani = Sejuani_png, cost_4[5], Lasercorps_trait[3], Brawler_trait[5]
Senna = Senna_png, cost_3[8], Lasercorps_trait[4], Sureshot_trait[2]
Sett = Sett_png, cost_4[6], Defender_trait[3], Mecha_trait[3]
Sivir = Sivir_png, cost_2[9], Sureshot_trait[3], Civilian_trait[1]
Sona = Sona_png, cost_3[9], Underground_trait[3], Spellslinger_trait[4], Heart_trait[2]
Soraka = Soraka_png, cost_4[7], Admin_trait[3], Heart_trait[3]
Sylas = Sylas_png, cost_1[10], Renegade_trait[2], Animasquad_trait[4]
Syndra = Syndra_png, cost_5[6], Starguardian_trait[5], Heart_trait[4]
Taliyah = Taliyah_png, cost_4[8], Starguardian_trait[6], Spellslinger_trait[5]
Talon = Talon_png, cost_1[11], Renegade_trait[3], Ox_Force_trait[4]
Urgot = Urgot_png, cost_5[7], Threat_trait[5]
Vayne = Vayne_png, cost_3[10], Animasquad_trait[5], Recon_trait[3], Duelist_trait[4]
Vel_Koz = Vel_Koz_png, cost_3[11], Threat_trait[6]
Vi = Vi_png, cost_2[10], Underground_trait[4], Brawler_trait[6]
Viego = Viego_png, cost_4[9], Renegade_trait[4], Ox_Force_trait[5]
Wukong = Wukong_png, cost_1[12], Mecha_trait[4], Defender_trait[4]
Yasuo = Yasuo_png, cost_2[11], Lasercorps_trait[5], Duelist_trait[5]
Yuumi = Yuumi_png, cost_2[12], Starguardian_trait[7], Mascot_trait[4], Heart_trait[5]
Zac = Zac_png, cost_4[10], Threat_trait[7]
Zed = Zed_png, cost_4[11], Lasercorps_trait[6], Duelist_trait[6], Hacker_trait[1]
Zoe = Zoe_png, cost_3[12], Gadgeteen_trait[4], Prankster_trait[2], Hacker_trait[2]
#################################################################################################################################################
Slot_1 = ("-")
Slot_2 = ("-")
Slot_3 = ("-")
Slot_4 = ("-")
Slot_5 = ("-")
Slot_6 = ("-")
Slot_7 = ("-")
Slot_8 = ("-")
Slot_9 = ("-")

Slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#################################################################################################################################################
main = Tk()
main.title("Set 8 TFT")

def select_units1():
    global Dropdown1_Value
    global Slot_1, Slot_2, Slot_3, Slot_4, Slot_5, Slot_6, Slot_7, Slot_8, Slot_9
    Dropdown1_Value = Dropdown1.get()
    if Slot_1 == "-":
        Slot_1 = Dropdown1_Value
        Slot_1_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=0, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_1 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_1 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_1 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_1 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_1 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_1 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_1 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_1 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_1 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_1 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_1 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_1 = Talon[0]
        else:
            Slot_1 = Wukong[0]
    elif Slot_2 == "-":
        Slot_2 = Dropdown1_Value
        Slot_2_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=1, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_2 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_2 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_2 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_2 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_2 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_2 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_2 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_2 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_2 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_2 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_2 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_2 = Talon[0]
        else:
            Slot_9 = Wukong[0]
    elif Slot_3 == "-":
        Slot_3 = Dropdown1_Value
        Slot_3_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=2, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_3 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_3 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_3 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_3 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_3 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_3 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_3 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_3 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_3 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_3 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_3 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_3 = Talon[0]
        else:
            Slot_3 = Wukong[0]
    elif Slot_4 == "-":
        Slot_4 = Dropdown1_Value
        Slot_4_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=3, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_4 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_4 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_4 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_4 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_4 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_4 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_4 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_4 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_4 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_4 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_4 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_4 = Talon[0]
        else:
            Slot_4 = Wukong[0]
    elif Slot_5 == "-":
        Slot_5 = Dropdown1_Value
        Slot_5_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=4, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_5 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_5 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_5 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_5 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_5 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_5 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_5 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_5 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_5 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_5 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_5 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_5 = Talon[0]
        else:
            Slot_5 = Wukong[0]
    elif Slot_6 == "-":
        Slot_6 = Dropdown1_Value
        Slot_6_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=5, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_6 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_6 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_6 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_6 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_6 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_6 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_6 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_6 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_6 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_6 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_6 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_6 = Talon[0]
        else:
            Slot_6 = Wukong[0]
    elif Slot_7 == "-":
        Slot_7 = Dropdown1_Value
        Slot_7_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=6, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_7 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_7 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_7 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_7 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_7 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_7 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_7 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_7 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_7 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_7 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_7 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_7 = Talon[0]
        else:
            Slot_7 = Wukong[0]
    elif Slot_8 == "-":
        Slot_8 = Dropdown1_Value
        Slot_8_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=7, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_8 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_8 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_8 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_8 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_8 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_8 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_8 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_8 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_8 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_8 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_8 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_8 = Talon[0]
        else:
            Slot_8 = Wukong[0]
    elif Slot_9 == "-":
        Slot_9 = Dropdown1_Value
        Slot_9_Label = Label(main, text=Dropdown1_Value, width=10).grid(row=8, column=0, columnspan=2)
        if Dropdown1_Value == "Ashe":
            Slot_9 = Ashe[0]
        elif Dropdown1_Value == "Blitzcrank":
            Slot_9 = Blitzcrank[0]
        elif Dropdown1_Value == "Galio":
            Slot_9 = Galio[0]
        elif Dropdown1_Value == "Gangplank":
            Slot_9 = Gangplank[0]
        elif Dropdown1_Value == "Kayle":
            Slot_9 = Kayle[0]
        elif Dropdown1_Value == "Lulu":
            Slot_9 = Lulu[0]
        elif Dropdown1_Value == "Lux":
            Slot_9 = Lux[0]
        elif Dropdown1_Value == "Nasus":
            Slot_9 = Nasus[0]
        elif Dropdown1_Value == "Poppy":
            Slot_9 = Poppy[0]
        elif Dropdown1_Value == "Renekton":
            Slot_9 = Renekton[0]
        elif Dropdown1_Value == "Sylas":
            Slot_9 = Sylas[0]
        elif Dropdown1_Value == "Talon":
            Slot_9 = Talon[0]
        else:
            Slot_9 = Wukong[0]


def select_units2():
    global Dropdown2_Value
    global Slot_1, Slot_2, Slot_3, Slot_4, Slot_5, Slot_6, Slot_7, Slot_8, Slot_9
    Dropdown2_Value = Dropdown2.get()
    if Slot_1 == "-":
        Slot_1 = Dropdown2_Value
        Slot_1_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=0, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_1 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_1 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_1 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_1 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_1 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_1 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_1 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_1 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_1 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_1 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_1 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_1 = Yasuo[0]
        else:
            Slot_1 = Yuumi[0]
    elif Slot_2 == "-":
        Slot_2 = Dropdown2_Value
        Slot_2_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=1, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_2 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_2 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_2 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_2 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_2 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_2 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_2 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_2 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_2 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_2 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_2 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_2 = Yasuo[0]
        else:
            Slot_2 = Yuumi[0]
    elif Slot_3 == "-":
        Slot_3 = Dropdown2_Value
        Slot_3_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=2, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_3 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_3 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_3 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_3 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_3 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_3 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_3 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_3 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_3 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_3 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_3 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_3 = Yasuo[0]
        else:
            Slot_3 = Yuumi[0]
    elif Slot_4 == "-":
        Slot_4 = Dropdown2_Value
        Slot_4_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=3, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_4 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_4 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_4 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_4 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_4 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_4 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_4 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_4 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_4 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_4 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_4 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_4 = Yasuo[0]
        else:
            Slot_4 = Yuumi[0]
    elif Slot_5 == "-":
        Slot_5 = Dropdown2_Value
        Slot_5_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=4, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_5 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_5 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_5 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_5 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_5 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_5 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_5 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_5 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_5 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_5 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_5 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_5 = Yasuo[0]
        else:
            Slot_5 = Yuumi[0]
    elif Slot_6 == "-":
        Slot_6 = Dropdown2_Value
        Slot_6_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=5, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_6 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_6 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_6 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_6 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_6 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_6 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_6 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_6 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_6 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_6 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_6 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_6 = Yasuo[0]
        else:
            Slot_6 = Yuumi[0]
    elif Slot_7 == "-":
        Slot_7 = Dropdown2_Value
        Slot_7_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=6, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_7 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_7 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_7 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_7 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_7 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_7 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_7 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_7 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_7 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_7 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_7 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_7 = Yasuo[0]
        else:
            Slot_7 = Yuumi[0]
    elif Slot_8 == "-":
        Slot_8 = Dropdown2_Value
        Slot_8_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=7, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_8 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_8 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_8 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_8 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_8 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_8 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_8 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_8 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_8 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_8 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_8 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_8 = Yasuo[0]
        else:
            Slot_8 = Yuumi[0]
    elif Slot_9 == "-":
        Slot_9 = Dropdown2_Value
        Slot_9_Label = Label(main, text=Dropdown2_Value, width=10).grid(row=8, column=0, columnspan=2)
        if Dropdown2_Value == "Annie":
            Slot_9 = Annie[0]
        elif Dropdown2_Value == "Camille":
            Slot_9 = Camille[0]
        elif Dropdown2_Value == "Draven":
            Slot_9 = Draven[0]
        elif Dropdown2_Value == "Ezreal":
            Slot_9 = Ezreal[0]
        elif Dropdown2_Value == "Fiora":
            Slot_9 = Fiora[0]
        elif Dropdown2_Value == "Jinx":
            Slot_9 = Jinx[0]
        elif Dropdown2_Value == "Lee_Sin":
            Slot_9 = Lee_Sin[0]
        elif Dropdown2_Value == "Malphite":
            Slot_9 = Malphite[0]
        elif Dropdown2_Value == "Rell":
            Slot_9 = Rell[0]
        elif Dropdown2_Value == "Sivir":
            Slot_9 = Sivir[0]
        elif Dropdown2_Value == "Vi":
            Slot_9 = Vi[0]
        elif Dropdown2_Value == "Yasuo":
            Slot_9 = Yasuo[0]
        else:
            Slot_9 = Yuumi[0]


def select_units3():
    global Dropdown3_Value
    global Slot_1, Slot_2, Slot_3, Slot_4, Slot_5, Slot_6, Slot_7, Slot_8, Slot_9
    Dropdown3_Value = Dropdown3.get()
    if Slot_1 == "-":
        Slot_1 = Dropdown3_Value
        Slot_1_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=0, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_1 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_1 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_1 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_1 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_1 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_1 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_1 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_1 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_1 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_1 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_1 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_1 = Vel_Koz[0]
        else:
            Slot_1 = Zoe[0]
    elif Slot_2 == "-":
        Slot_2 = Dropdown3_Value
        Slot_2_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=1, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_2 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_2 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_2 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_2 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_2 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_2 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_2 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_2 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_2 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_2 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_2 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_2 = Vel_Koz[0]
        else:
            Slot_2 = Zoe[0]
    elif Slot_3 == "-":
        Slot_3 = Dropdown3_Value
        Slot_3_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=2, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_3 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_3 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_3 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_3 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_3 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_3 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_3 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_3 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_3 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_3 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_3 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_3 = Vel_Koz[0]
        else:
            Slot_3 = Zoe[0]
    elif Slot_4 == "-":
        Slot_4 = Dropdown3_Value
        Slot_4_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=3, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_4 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_4 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_4 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_4 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_4 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_4 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_4 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_4 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_4 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_4 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_4 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_4 = Vel_Koz[0]
        else:
            Slot_4 = Zoe[0]
    elif Slot_5 == "-":
        Slot_5 = Dropdown3_Value
        Slot_5_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=4, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_5 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_5 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_5 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_5 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_5 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_5 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_5 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_5 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_5 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_5 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_5 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_5 = Vel_Koz[0]
        else:
            Slot_5 = Zoe[0]
    elif Slot_6 == "-":
        Slot_6 = Dropdown3_Value
        Slot_6_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=5, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_6 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_6 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_6 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_6 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_6 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_6 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_6 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_6 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_6 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_6 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_6 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_6 = Vel_Koz[0]
        else:
            Slot_6 = Zoe[0]
    elif Slot_7 == "-":
        Slot_7 = Dropdown3_Value
        Slot_7_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=6, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_7 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_7 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_7 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_7 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_7 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_7 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_7 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_7 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_7 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_7 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_7 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_7 = Vel_Koz[0]
        else:
            Slot_7 = Zoe[0]
    elif Slot_8 == "-":
        Slot_8 = Dropdown3_Value
        Slot_8_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=7, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_8 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_8 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_8 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_8 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_8 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_8 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_8 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_8 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_8 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_8 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_8 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_8 = Vel_Koz[0]
        else:
            Slot_8 = Zoe[0]
    elif Slot_9 == "-":
        Slot_9 = Dropdown3_Value
        Slot_9_Label = Label(main, text=Dropdown3_Value, width=10).grid(row=8, column=0, columnspan=2)
        if Dropdown3_Value == "Alistar":
            Slot_9 = Alistar[0]
        elif Dropdown3_Value == "Cho'Gath":
            Slot_9 = Cho_Gath[0]
        elif Dropdown3_Value == "Jax":
            Slot_9 = Jax[0]
        elif Dropdown3_Value == "Kai'Sa":
            Slot_9 = Kai_Sa[0]
        elif Dropdown3_Value == "LeBlanc":
            Slot_9 = LeBlanc[0]
        elif Dropdown3_Value == "Nilah":
            Slot_9 = Nilah[0]
        elif Dropdown3_Value == "Rammus":
            Slot_9 = Rammus[0]
        elif Dropdown3_Value == "Riven":
            Slot_9 = Riven[0]
        elif Dropdown3_Value == "Senna":
            Slot_9 = Senna[0]
        elif Dropdown3_Value == "Sona":
            Slot_9 = Sona[0]
        elif Dropdown3_Value == "Vayne":
            Slot_9 = Vayne[0]
        elif Dropdown3_Value == "Vel'Koz":
            Slot_9 = Vel_Koz[0]
        else:
            Slot_9 = Zoe[0]


def select_units4():
    global Dropdown4_Value
    global Slot_1, Slot_2, Slot_3, Slot_4, Slot_5, Slot_6, Slot_7, Slot_8, Slot_9
    Dropdown4_Value = Dropdown4.get()
    if Slot_1 == "-":
        Slot_1 = Dropdown4_Value
        Slot_1_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=0, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_1 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_1 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_1 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_1 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_1 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_1 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_1 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_1 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_1 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_1 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_1 = Zac[0]
        else:
            Slot_1 = Zed[0]
    elif Slot_2 == "-":
        Slot_2 = Dropdown4_Value
        Slot_2_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=1, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_2 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_2 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_2 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_2 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_2 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_2 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_2 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_2 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_2 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_2 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_2 = Zac[0]
        else:
            Slot_2 = Zed[0]
    elif Slot_3 == "-":
        Slot_3 = Dropdown4_Value
        Slot_3_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=2, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_3 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_3 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_3 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_3 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_3 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_3 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_3 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_3 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_3 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_3 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_3 = Zac[0]
        else:
            Slot_3 = Zed[0]
    elif Slot_4 == "-":
        Slot_4 = Dropdown4_Value
        Slot_4_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=3, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_4 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_4 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_4 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_4 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_4 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_4 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_4 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_4 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_4 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_4 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_4 = Zac[0]
        else:
            Slot_4 = Zed[0]
    elif Slot_5 == "-":
        Slot_5 = Dropdown4_Value
        Slot_5_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=4, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_5 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_5 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_5 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_5 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_5 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_5 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_5 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_5 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_5 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_5 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_5 = Zac[0]
        else:
            Slot_5 = Zed[0]
    elif Slot_6 == "-":
        Slot_6 = Dropdown4_Value
        Slot_6_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=5, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_6 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_6 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_6 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_6 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_6 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_6 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_6 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_6 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_6 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_6 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_6 = Zac[0]
        else:
            Slot_6 = Zed[0]
    elif Slot_7 == "-":
        Slot_7 = Dropdown4_Value
        Slot_7_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=6, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_7 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_7 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_7 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_7 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_7 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_7 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_7 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_7 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_7 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_7 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_7 = Zac[0]
        else:
            Slot_7 = Zed[0]
    elif Slot_8 == "-":
        Slot_8 = Dropdown4_Value
        Slot_8_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=7, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_8 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_8 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_8 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_8 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_8 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_8 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_8 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_8 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_8 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_8 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_8 = Zac[0]
        else:
            Slot_8 = Zed[0]
    elif Slot_9 == "-":
        Slot_9 = Dropdown4_Value
        Slot_9_Label = Label(main, text=Dropdown4_Value, width=10).grid(row=8, column=0, columnspan=2)
        if Dropdown4_Value == "Aurelion Sol":
            Slot_9 = Aurelion_Sol[0]
        elif Dropdown4_Value == "Bel'Veth":
            Slot_9 = Bel_Veth[0]
        elif Dropdown4_Value == "Ekko":
            Slot_9 = Ekko[0]
        elif Dropdown4_Value == "Miss Fortune":
            Slot_9 = Miss_Fortune[0]
        elif Dropdown4_Value == "Samira":
            Slot_9 = Samira[0]
        elif Dropdown4_Value == "Sejuani":
            Slot_9 = Sejuani[0]
        elif Dropdown4_Value == "Sett":
            Slot_9 = Sett[0]
        elif Dropdown4_Value == "Soraka":
            Slot_9 = Soraka[0]
        elif Dropdown4_Value == "Taliyah":
            Slot_9 = Taliyah[0]
        elif Dropdown4_Value == "Viego":
            Slot_9 = Viego[0]
        elif Dropdown4_Value == "Zac":
            Slot_9 = Zac[0]
        else:
            Slot_9 = Zed[0]


def select_units5():
    global Dropdown5_Value
    global Slot_1, Slot_2, Slot_3, Slot_4, Slot_5, Slot_6, Slot_7, Slot_8, Slot_9
    Dropdown5_Value = Dropdown5.get()
    if Slot_1 == "-":
        Slot_1 = Dropdown5_Value
        Slot_1_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=0, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_1 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_1 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_1 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_1 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_1 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_1 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_1 = Syndra[0]
        else:
            Slot_1 = Urgot[0]
    elif Slot_2 == "-":
        Slot_2 = Dropdown5_Value
        Slot_2_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=1, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_2 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_2 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_2 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_2 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_2 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_2 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_2 = Syndra[0]
        else:
            Slot_2 = Urgot[0]
    elif Slot_3 == "-":
        Slot_3 = Dropdown5_Value
        Slot_3_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=2, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_3 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_3 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_3 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_3 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_3 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_3 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_3 = Syndra[0]
        else:
            Slot_3 = Urgot[0]
    elif Slot_4 == "-":
        Slot_4 = Dropdown5_Value
        Slot_4_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=3, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_4 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_4 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_4 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_4 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_4 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_4 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_4 = Syndra[0]
        else:
            Slot_4 = Urgot[0]
    elif Slot_5 == "-":
        Slot_5 = Dropdown5_Value
        Slot_5_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=4, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_5 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_5 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_5 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_5 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_5 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_5 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_5 = Syndra[0]
        else:
            Slot_5 = Urgot[0]
    elif Slot_6 == "-":
        Slot_6 = Dropdown5_Value
        Slot_6_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=5, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_6 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_6 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_6 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_6 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_6 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_6 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_6 = Syndra[0]
        else:
            Slot_6 = Urgot[0]
    elif Slot_7 == "-":
        Slot_7 = Dropdown5_Value
        Slot_7_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=6, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_7 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_7 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_7 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_7 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_7 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_7 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_7 = Syndra[0]
        else:
            Slot_7 = Urgot[0]
    elif Slot_8 == "-":
        Slot_8 = Dropdown5_Value
        Slot_8_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=7, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_8 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_8 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_8 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_8 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_8 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_8 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_8 = Syndra[0]
        else:
            Slot_8 = Urgot[0]
    elif Slot_9 == "-":
        Slot_9 = Dropdown5_Value
        Slot_9_Label = Label(main, text=Dropdown5_Value, width=10).grid(row=8, column=0, columnspan=2)
        if Dropdown5_Value == "Aphelios":
            Slot_9 = Aphelios[0]
        elif Dropdown5_Value == "Fiddlesticks":
            Slot_9 = Fiddlesticks[0]
        elif Dropdown5_Value == "Janna":
            Slot_9 = Janna[0]
        elif Dropdown5_Value == "Leona":
            Slot_9 = Leona[0]
        elif Dropdown5_Value == "Mordekaiser":
            Slot_9 = Mordekaiser[0]
        elif Dropdown5_Value == "Nunu":
            Slot_9 = Nunu[0]
        elif Dropdown5_Value == "Syndra":
            Slot_9 = Syndra[0]
        else:
            Slot_9 = Urgot[0]


def reset():
    global Slots_Var
    global Slot_1, Slot_2, Slot_3, Slot_4, Slot_5, Slot_6, Slot_7, Slot_8, Slot_9
    Slots_Value = Slots_Var.get()
    if Slots_Value == str(Slots[0]):
        Slot_1 = "-"
        Slot_1_Label = Label(main, text=Slot_1, width=10).grid(row=0, column=0, columnspan=2)
    elif Slots_Value == str(Slots[1]):
        Slot_2 = "-"
        Slot_2_Label = Label(main, text=Slot_2, width=10).grid(row=1, column=0, columnspan=2)
    elif Slots_Value == str(Slots[2]):
        Slot_3 = "-"
        Slot_3_Label = Label(main, text=Slot_3, width=10).grid(row=2, column=0, columnspan=2)
    elif Slots_Value == str(Slots[3]):
        Slot_4 = "-"
        Slot_4_Label = Label(main, text=Slot_4, width=10).grid(row=3, column=0, columnspan=2)
    elif Slots_Value == str(Slots[4]):
        Slot_5 = "-"
        Slot_5_Label = Label(main, text=Slot_5, width=10).grid(row=4, column=0, columnspan=2)
    elif Slots_Value == str(Slots[5]):
        Slot_6 = "-"
        Slot_6_Label = Label(main, text=Slot_6, width=10).grid(row=5, column=0, columnspan=2)
    elif Slots_Value == str(Slots[6]):
        Slot_7 = "-"
        Slot_7_Label = Label(main, text=Slot_7, width=10).grid(row=6, column=0, columnspan=2)
    elif Slots_Value == str(Slots[7]):
        Slot_8 = "-"
        Slot_8_Label = Label(main, text=Slot_8, width=10).grid(row=7, column=0, columnspan=2)
    elif Slots_Value == str(Slots[8]):
        Slot_9 = "-"
        Slot_9_Label = Label(main, text=Slot_9, width=10).grid(row=8, column=0, columnspan=2)


def toggle():
    global Tog
    if Tog == False:
        Tog = True
        Toggle_label = Label(main, text="  Active  ").grid(row=8, column=3, columnspan=2)
    else:
        Tog = False
        Toggle_label = Label(main, text="Inactive").grid(row=8, column=3, columnspan=2)
    main.destroy()


def card_search():
    if Slot_1 != "-":
        Slot_1_Var = pyautogui.locateOnScreen(Slot_1, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_1_Var != None:
            Slot_1_Loc = pyautogui.center(Slot_1_Var)
            pyautogui.moveTo(Slot_1_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_1[43:-4])
    if Slot_2 != "-":
        Slot_2_Var = pyautogui.locateOnScreen(Slot_2, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_2_Var != None:
            Slot_2_Loc = pyautogui.center(Slot_2_Var)
            pyautogui.moveTo(Slot_2_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_2[43:-4])
    if Slot_3 != "-":
        Slot_3_Var = pyautogui.locateOnScreen(Slot_3, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_3_Var != None:
            Slot_3_Loc = pyautogui.center(Slot_3_Var)
            pyautogui.moveTo(Slot_3_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_3[43:-4])
    if Slot_4 != "-":
        Slot_4_Var = pyautogui.locateOnScreen(Slot_4, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_4_Var != None:
            Slot_4_Loc = pyautogui.center(Slot_4_Var)
            pyautogui.moveTo(Slot_4_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_4[43:-4])
    if Slot_5 != "-":
        Slot_5_Var = pyautogui.locateOnScreen(Slot_5, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_5_Var != None:
            Slot_5_Loc = pyautogui.center(Slot_5_Var)
            pyautogui.moveTo(Slot_5_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_5[43:-4])
    if Slot_6 != "-":
        Slot_6_Var = pyautogui.locateOnScreen(Slot_6, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_6_Var != None:
            Slot_6_Loc = pyautogui.center(Slot_6_Var)
            pyautogui.moveTo(Slot_6_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_6[43:-4])
    if Slot_7 != "-":
        Slot_7_Var = pyautogui.locateOnScreen(Slot_7, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_7_Var != None:
            Slot_7_Loc = pyautogui.center(Slot_7_Var)
            pyautogui.moveTo(Slot_7_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_7[43:-4])
    if Slot_8 != "-":
        Slot_8_Var = pyautogui.locateOnScreen(Slot_8, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_8_Var != None:
            Slot_8_Loc = pyautogui.center(Slot_8_Var)
            pyautogui.moveTo(Slot_8_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_8[43:-4])
    if Slot_9 != "-":
        Slot_9_Var = pyautogui.locateOnScreen(Slot_9, region=(480, 928, 997, 143), grayscale=True, confidence=0.70)
        if Slot_9_Var != None:
            Slot_9_Loc = pyautogui.center(Slot_9_Var)
            pyautogui.moveTo(Slot_9_Loc)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            print("Found " + Slot_9[43:-4])



Slot_1_Label = Label(main, text=Slot_1, width=10)
Slot_2_Label = Label(main, text=Slot_2, width=10)
Slot_3_Label = Label(main, text=Slot_3, width=10)
Slot_4_Label = Label(main, text=Slot_4, width=10)
Slot_5_Label = Label(main, text=Slot_5, width=10)
Slot_6_Label = Label(main, text=Slot_6, width=10)
Slot_7_Label = Label(main, text=Slot_7, width=10)
Slot_8_Label = Label(main, text=Slot_8, width=10)
Slot_9_Label = Label(main, text=Slot_9, width=10)

Slot_1_Label.grid(row=0, column=0, columnspan=2)
Slot_2_Label.grid(row=1, column=0, columnspan=2)
Slot_3_Label.grid(row=2, column=0, columnspan=2)
Slot_4_Label.grid(row=3, column=0, columnspan=2)
Slot_5_Label.grid(row=4, column=0, columnspan=2)
Slot_6_Label.grid(row=5, column=0, columnspan=2)
Slot_7_Label.grid(row=6, column=0, columnspan=2)
Slot_8_Label.grid(row=7, column=0, columnspan=2)
Slot_9_Label.grid(row=8, column=0, columnspan=2)

Dropdown1 = StringVar()
Dropdown1.set("1 Cost")
Dropdown2 = StringVar()
Dropdown2.set("2 Cost")
Dropdown3 = StringVar()
Dropdown3.set("3 Cost")
Dropdown4 = StringVar()
Dropdown4.set("4 Cost")
Dropdown5 = StringVar()
Dropdown5.set("5 Cost")

Cost_1_dropdown = OptionMenu(main, Dropdown1, *cost_1)
Cost_1_dropdown.grid(row=0, column=3, ipadx=10)
Cost_2_dropdown = OptionMenu(main, Dropdown2, *cost_2)
Cost_2_dropdown.grid(row=1, column=3, ipadx=10)
Cost_3_dropdown = OptionMenu(main, Dropdown3, *cost_3)
Cost_3_dropdown.grid(row=2, column=3, ipadx=10)
Cost_4_dropdown = OptionMenu(main, Dropdown4, *cost_4)
Cost_4_dropdown.grid(row=3, column=3, ipadx=10)
Cost_5_dropdown = OptionMenu(main, Dropdown5, *cost_5)
Cost_5_dropdown.grid(row=4, column=3, ipadx=10)

Select_1_Button = Button(main, text="Select",width=10 , command=select_units1).grid(row=0, column=4)
Select_2_Button = Button(main, text="Select",width=10 , command=select_units2).grid(row=1, column=4)
Select_3_Button = Button(main, text="Select",width=10 , command=select_units3).grid(row=2, column=4)
Select_4_Button = Button(main, text="Select",width=10 , command=select_units4).grid(row=3, column=4)
Select_5_Button = Button(main, text="Select",width=10 , command=select_units5).grid(row=4, column=4)

# Reset Button
Slots_Var = StringVar()
Slots_Var.set(str(Slots[0]))

Reset_button = Button(main, text="Reset",width=12 , command=reset).grid(row=5, column=3)
Reset_slot = OptionMenu(main, Slots_Var, *Slots)
Reset_slot.grid(row=5, column=4, ipadx=16)

# Toggle Button
Tog = False
Toggle_button = Button(main, text="Toggle", width=20, command=toggle).grid(row=7, column=3, columnspan=2)
Toggle_label = Label(main, text="Inactive").grid(row=8, column=3, columnspan=2)

main.mainloop()

while Tog:
    card_search()
    if keyboard.is_pressed("ESC"):
        exec(open("TFT auto-buy Set 8.py").read())


