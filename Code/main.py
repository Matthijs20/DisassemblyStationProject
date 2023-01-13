from DRCF import *

#snelheden voor normale omstandigheden
velocity = 100
acceleration = 100

#home poses
home_pos_j = posj(0, 22.5, 67.5, 0, 90, 0.0)
home_pos_t = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)


##############################################
##Tool change deel
#############################################

m = 5
def grab_tool(tool):
    if tool == 1:
        pos_boven_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5 - 180)
        pos_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, -172.5)
        pos_rotated_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, 7.5 + 45 - 180)
        pos_boven_rotated_t = posx(687.3, 69.8, 251.9, 5.8, 180.0, -127.6)
    elif tool == 2:
        pos_boven_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -180.0)
        pos_t = posx(687.1, -20.4, 168.6, 177.9, -180.0, -0.3)
        pos_rotated_j = posj(-1.7, 54.6, 50.7, 0.0, 74.7, -180.0 + 45)
        pos_boven_rotated_t = posx(687.1, -20.4, 247.0, 178.5, 180.0, 44.0)

    movej(pos_boven_j,v=velocity, a=acceleration)
    movel(pos_t, a=10, v=10 * m)
    # Cilinder
    movej(pos_rotated_j, a=10, v=10 * m)
    movel(pos_boven_rotated_t, a=10, v=10 * m)
    movej(home_pos_j, v=velocity, a=acceleration)


def dump_tool(tool):
    if tool == 1:
        pos_boven_t = posx(687.3, 69.8, 251.9, 5.8, 179.9, -172.5)
        pos_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, -180)
        pos_rotated_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, -127.6)
        pos_boven_rotated_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5 + 45 - 180)
    elif tool == 2:
        pos_boven_t = posx(687.0, -20.4, 247.0, 1.2, -180.0, -178)
        pos_j = posj(-1.7, 54.6, 50.7, 0.0, 74.7, -180.0)
        pos_rotated_t = posx(687.1, -20.4, 168.5, 177.3, 180.0, 44.0)
        pos_boven_rotated_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -180.0 + 45)

    movej(pos_boven_rotated_j,v=velocity, a=acceleration)
    movel(pos_rotated_t, a = 10, v = 10 * m)
    # Cilinder
    movej(pos_j, a = 10, v = 10 * m)
    movel(pos_boven_t, a=10,v=10*m)



######################################################################################
##achterklep demonteer station
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
    #tool changen


vork_S1 = posx(488.1, -149.8, 88.3, 20.2, -179.3, -27.2)
vork_S2 = posx(488.1, -177.2, 88.4, 20.9, -179.3, -26.6)
vork_S3 = posx(488.1, -177.2, 102.1, 20.9, -179.3, -26.6)
vork_S4 = posx(488.1, -177.2, 93.2, 20.9, -179.3, -26.6)
vork_S5 = posx(488.1, -177.0, 101.5, 19.9, -179.3, -27.6)
vork_S6 = posx(488.1, -190.3, 109.1, 19.9, -179.3, -27.6)
vork_S7 = posx(488.1, -144.9, 96.4, 19.8, -179.3, -27.7)
vork_S8 = posx(431.0, -246.0, 127.0, 112.7, -179.3, -27.8)
vork_S9 = posx(458.5, -232.5, 95.2, 3.5, -169.0, -136.4)
vork_S10 = posx(472.0, -222.7, 87.8, 2.9, -166.6, -137.0)
vork_S11 = posx(473.1, -222.7, 92.3, 2.9, -166.6, -137.0)

def achterklep2():
    vx = 40
    ax = 20
    set_digital_output(2, 1)
    movel(vork_S1, v=velocity, a=acceleration)
    wait(2)
    movel(vork_S2, v=vx, a=ax)
    movel(vork_S3, v=vx, a=ax)
    movel(vork_S4, v=vx, a=ax)
    set_digital_output(2, 0)
    movel(vork_S5, v=vx, a=ax)
    movel(vork_S6, v=vx, a=ax)
    movel(vork_S7, v=vx, a=ax)
    movel(vork_S8, v=vx, a=ax)
    movel(vork_S9, v=vx, a=ax)
    movel(vork_S10, v=vx, a=ax)
    set_digital_output(2, 1)
    movel(vork_S11, v=vx, a=ax)
    set_digital_output(2, 0)
    movel(vork_S10, v=vx, a=ax)
    movel(vork_S9, v=vx, a=ax)
    movel(vork_S8, v=vx, a=ax)

    movej(home_pos_j, v=velocity, a=acceleration)
    #tool changen
    #wait(10)

achterklep_oppakken_S1 = posx(486.6, -262.1, 151.0, 177.1, 180.0, 177.1)
achterklep_oppakken_S2 = posx(486.6, -262.1, 139.3, 174.8, 180.0, 174.8)
achterklep_oppakken_S3 = posx(486.6, -262.1, 164.5, 176.3, 180.0, 176.3)
achterklep_oppakken_S4 = posx(277.0, -191.8, 179.5, 179.6, 180.0, 88.5)
achterklep_oppakken_S5 = posx(277.0, -191.8, 145.2, 179.6, 180.0, 88.5)

def achterklep3():
    vx = 40
    ax = 20
    movel(achterklep_oppakken_S1, v=velocity, a=acceleration)
    set_digital_output(1, 1)
    movel(achterklep_oppakken_S2, v=vx, a=ax)
    movel(achterklep_oppakken_S3, v=vx, a=ax)
    movel(achterklep_oppakken_S4, v=vx, a=ax)
    movel(achterklep_oppakken_S5, v=vx, a=ax)
    set_digital_output(1, 0)
    movel(achterklep_oppakken_S4, v=vx, a=ax)




######################################################################################
##Omdraai station
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
######################################################################################

batterij_boven = posx(488.9, -262.9, 156.0, 151.8, 180.0, 137.0)
batterij_pos = posx(490.6, -268.3, 134.1, 146.9, -179.9, 132.1)
batterij_eruit = posx(488.9, -270.6, 144.8, 110.4, -179.1, 95.7)
batterij_eruit2 = posx(488.5, -269.6, 204.1, 110.4, -179.1, 95.7)
batterij_erin = posx(145.2, -204.0, 140.6, 89.5, -179.3, 74.9)
batterij_erin2 = posx(145.2, -204.0, 187.6, 89.5, -179.3, 74.9)


def batterij():
    vx = 50
    ax = 20
    movel(batterij_boven, v=velocity, a=acceleration)
    movel(batterij_pos, v=vx, a=ax)
    set_digital_output(1, 1)
    wait(1)
    movel(batterij_eruit, v=vx, a=ax)
    movel(batterij_eruit2, v=vx, a=ax)
    movel(batterij_erin2, v=vx, a=ax)
    movel(batterij_erin, v=vx, a=ax)
    set_digital_output(1, 0)
    wait(1)
    movel(batterij_erin2, v=vx, a=ax)


######################################################################################
##Voorrand demonteren station
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

######################################################################################
##Voorrand verwijderen
######################################################################################

#staat nog op de planning

######################################################################################
##de rest van de telefoon naar tray verplaatsen
######################################################################################

#staat nog op de planning


######################################################################################
##Main loop
######################################################################################

set_digital_output(1,0)
movej(home_pos_j,v=velocity, a=acceleration)
grab_tool(1) #vacuum opppakken
achterklep() #Oppakken vanaf de tray
dump_tool(1) #vacuum wegzetten
grab_tool(2) #spatel oppakken
achterklep2() #deel met de spatel
dump_tool(2) #spatel wegzetten
grab_tool(1) #vacuum oppakken
achterklep3() #achterklep weghalen
batterij() #batterij weghalen
omdraaistation() #omdraaien
voorrand_demonteren() #voorrand wegdrukken
dump_tool(1) #vacuum wegzetten
