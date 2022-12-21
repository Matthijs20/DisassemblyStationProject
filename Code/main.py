from DRCF import *

velocity = 150
acceleration = 100
#home poses
home_pos_j = posj(0, 22.5, 67.5, 0, 90, 0.0)
home_pos_t = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)

#achterklep demonteren
achterklepstation_hoogj = posj(-18.4, 30.7, 90.2, -6.5, 59.4, -0.0)
achterklepstation_hoogl = posx(492.7, -176.5, 192.0, 69.3, -174.4, 84.4)
achterklepstation = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)
achterklep_vorkS1 = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)
achterklep_vorkS2 = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)
achterklep_vorkS3 = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)
achterklep_vorkS4 = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)

#plek op de plaat voor achterklep
plaat_achterklep = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)


def achterklep_demonteren():
    #Stap 1: Telefoon naar demonteercel brengen
    movej(achterklepstation_hoogj,v=velocity, a=acceleration)
    movel(achterklepstation,v=velocity, a=acceleration)
    #vacuum uitschakelen
    wait(2)

    #Stap 2: tool changen
    movel(achterklepstation_hoogl,v=velocity, a=acceleration)
    #cilinder uitschuiven
    movej(home_pos_j,v=velocity, a=acceleration)
    #insert tool change code

    #stap 3: vork gebruiken
    movej(achterklepstation_hoogj,v=velocity, a=acceleration)
    movel(achterklep_vorkS1,v=velocity, a=acceleration)
    movel(achterklep_vorkS2,v=velocity, a=acceleration)
    movel(achterklep_vorkS3,v=velocity, a=acceleration)
    movel(achterklep_vorkS4,v=velocity, a=acceleration)

    # Stap 4: tool changen
    movel(achterklepstation_hoogl,v=velocity, a=acceleration)
    movej(home_pos_j,v=velocity, a=acceleration)
    #insert tool change code

    #Stap 5: oppakken achterklep
    # cilinder inschuiven
    movej(achterklepstation_hoogj,v=velocity, a=acceleration)
    #vacuum inschakelen
    movel(achterklepstation,v=velocity, a=acceleration)
    wait(2)
    movel(achterklepstation_hoogl,v=velocity, a=acceleration)
    movej(home_pos_j,v=velocity, a=acceleration)

    #stap 6: achterklep op plaat plaatsen
    movel(plaat_achterklep,v=velocity, a=acceleration)
    #vacuum uitschakelen
    movej(home_pos_j,v=velocity, a=acceleration)



##############################################
##Tool change deel
#############################################
vacuum_bovenj_gedraaid = posj(5.8, 52.2, 38.5, 0.0, 89.3, 48.9)
vacuum_bovenl_gedraaid = posx(686.6, 69.2, 274.7, 82.8, 180.0, 125.9)
vacuum_bovenj_los = posj(5.7, 52.6, 31.4, -0.2, 96.2, 3.4)
vacuum_bovenl_los = posx(686.3, 68.5, 314.9, 53.8, -179.7, 51.5)
vacuum_cel_los = posx(687.6, 70.1, 171.0, 74.0, -179.5, 74.3)
vacuum_cel_gedraaid = posx(686.6, 69.2, 168.5, 150.1, 180.0, -166.8)

def get_vacuum():
    vx = 5
    ax = 10

    movej(vacuum_bovenj_los,v=velocity, a=acceleration)
    movel(vacuum_cel_los, v=vx, a=ax)
    movel(vacuum_cel_gedraaid, v=vx, a=ax)
    movel(vacuum_bovenl_gedraaid, v=vx, a=ax)
    movej(home_pos_j,v=velocity, a=acceleration)
#movej(home_pos_j,v=velocity, a=acceleration)
#get_vacuum()

######################################################################################
##achterklep demonteer station
##status:
######################################################################################
traytelefoon_bovenj = posj(-36.2, 9.5, 125.3, -0.0, 45.1, -33.0)
traytelefoon_bovenl = posx(264.4, -193.7, 190.3, 144.1, 180.0, 147.3)
traytelefoon = posx(264.4, -193.7, 147.1, 143.2, -180.0, 146.4)
omdraaistation_telefoon_boven = posx(485.0, -236.0, 164.8, 119.8, -180.0, -145.5)
omdraaistation_telefoon_schuif = posx(485.0, -236.0, 137.4, 100.7, -180.0, -164.6)
omdraaistation_telefoon = posx(485.0, -254.1, 137.4, 109.8, -180.0, -155.6)

def achterklep():
    vx = 40
    ax = 20
    movej(traytelefoon_bovenj, v=velocity, a=acceleration)
    movel(traytelefoon, v=vx, a=ax)
    set_digital_output(1, 1)
    wait(2)
    movel(traytelefoon_bovenl, v=vx, a=ax)
    movel(omdraaistation_telefoon_boven, v=velocity, a=acceleration)
    movel(omdraaistation_telefoon_schuif, v=vx, a=ax)
    movel(omdraaistation_telefoon, v=vx, a=ax)
    set_digital_output(1, 0)
    movel(omdraaistation_telefoon_boven, v=vx, a=ax)
    movej(home_pos_j,v=velocity, a=acceleration)



######################################################################################
##Omdraai station
##status: Getest, werkend
######################################################################################
achterklep_omdraai = posx(491.9, -258.8, 129.3, 152.3, 180.0, 136.1)
achterklep_opzij = posx(490.9, -255.4, 130.6, 152.6, 180.0, 136.3)
achterklep_omdraai_hoog = posx(490.9, -255.4, 205.2, 152.6, 180.0, 136.4)
omdraaistation_p1 = posj(42.1, 23.1, 71.7, 71.7, -87.8, -5.7)
omdraaistation_p2 = posj(50.9, 58.7, 64.3, 81.5, -145.5, -5.7)
omdraaistation_p3 = posx(416.3, 402.6, 243.1, 93.2, -66.2, -105.2)
omdraaistation_p4 = posx(418.8, 352.5, 111.5, 91.6, -65.6, -107.2)
omdraaistation_p5 = posx(417.2, 410.9, 85.0, 91.6, -65.6, -107.2)
omdraaistation_p6 = posx(417.2, 410.9, 564.5, 91.6, -65.6, -107.2)

def omdraaistation():
    vx = 50
    ax = 20
    movel(achterklep_omdraai_hoog, v=velocity, a=acceleration)
    #vacuum aan
    set_digital_output(1, 1)
    wait(2)
    movel(achterklep_omdraai, v=vx, a=ax)
    movel(achterklep_opzij, v=vx, a=ax)
    movel(achterklep_omdraai_hoog, v=vx, a=ax)

    movej(home_pos_j,v=velocity, a=acceleration)

    movej(omdraaistation_p1,v=velocity, a=acceleration)
    movej(omdraaistation_p2,v=velocity, a=acceleration)
    movel(omdraaistation_p4,v=vx, a=ax)
    set_digital_output(1,0)
    wait(2)
    movel(omdraaistation_p5,v=vx, a=ax)
    movel(omdraaistation_p6,v=velocity, a=acceleration)
    movej(home_pos_j,v=velocity, a=acceleration)

######################################################################################
##batterij weghalen
##status:
######################################################################################

batterij_boven = posx(488.9, -262.9, 156.0, 151.8, 180.0, 137.0)
batterij_pos = posx(490.6, -268.3, 134.1, 146.9, -179.9, 132.1)
batterij_eruit = posx(488.9, -270.6, 144.8, 110.4, -179.1, 95.7)
batterij_eruit2 = posx(488.5, -269.6, 204.1, 110.4, -179.1, 95.7)

def batterij():
    vx = 50
    ax = 20
    movel(batterij_boven,v=velocity, a=acceleration)
    movel(batterij_pos,v=vx, a=ax)
    set_digital_output(1,1)
    wait(1)
    movel(batterij_eruit,v=vx, a=ax)
    movel(batterij_eruit2,v=vx, a=ax)

######################################################################################
##Voorrand demonteren station
##status: Getest, werkend
######################################################################################
toolchanger_afstand = posj(-0.8, 28.3, 110.7, 76.5, 77.9, 0.0)
toolchanger_telefoon = posx(431.3, 134.6, 192.5, 89.1, 106.2, 137.5)
toolchanger_eraf1 = posx(434.7, 147.2, 245.9, 91.3, 107.9, 137.9)
toolchanger_eraf2= posx(435.8, 96.5, 262.4, 91.3, 107.9, 137.9)
voorrand_boven = posx(479.8, 4.8, 171.7, 17.6, 179.9, -114.0)
voorrand_eraf = posx(479.8, 4.8, 134.6, 17.6, 179.9, -114.0)


def voorrand_demonteren():
    vx = 60
    ax = 30
    movej(home_pos_j, v=velocity, a=acceleration)
    movej(toolchanger_afstand, v=velocity, a=acceleration)
    set_digital_output(1, 1)
    movel(toolchanger_telefoon,v=vx,a=ax)
    wait(1)
    movel(toolchanger_eraf1, v=vx, a=ax)
    movel(toolchanger_eraf2, v=vx, a=ax)
    movej(home_pos_j, v=velocity, a=acceleration)
    movel(voorrand_boven, v=velocity, a=acceleration)
    movel(voorrand_eraf, v=vx, a=ax)
    set_digital_output(1, 0)
    movel(voorrand_boven, v=velocity, a=acceleration)
    movej(home_pos_j, v=velocity, a=acceleration)



#main

set_digital_output(1,0)
movej(home_pos_j,v=velocity, a=acceleration)
#omdraaistation()
#voorrand_demonteren()
#achterklep()
batterij()