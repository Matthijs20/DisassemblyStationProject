from DRCF import *

#snelheden voor normale omstandigheden
velocity = 200
acceleration = 200

#home poses
home_pos_j = posj(0, 22.5, 67.5, 0, 90, 0.0)
home_pos_t = posx(523.4, -0.0, 406.1, 0.0, -180.0, 0.0)


##############################################
##Tool change deel
#############################################

m = 18
def grab_tool(tool):
    vx = 100
    ax = 100
    if tool == 1:
        pos_boven_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5 - 180)
        x = posx(687.4, 69.8, 191.9, 5.8, 179.9, -172.5)
        pos_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, -172.5)
        pos_rotated_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, 7.5 + 45 - 180)
        pos_boven_rotated_t = posx(687.3, 69.8, 251.9, 5.8, 180.0, -127.6)
    elif tool == 2:
        pos_boven_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -90.0)
        pos_t = posx(687.1, -20.4, 168.6, 1.2, -180.0, -87.1)
        pos_rotated_j = posj(-1.7, 54.6, 50.7, -0.0, 74.7, -45)
        pos_boven_rotated_t = posx(687.1, -20.4, 247.0, 0.2, -180.0, -43.1)

    movej(pos_boven_j, a=acceleration, v=velocity)
    movel(pos_t, a=ax, v=vx)
    # Cilinder
    movej(pos_rotated_j, a=ax, v=vx)
    movel(pos_boven_rotated_t, a=ax, v=vx)
    movej(home_pos_j,v=velocity, a=acceleration)


def dump_tool(tool):
    vx = 100
    ax = 100
    if tool == 1:
        pos_boven_t = posx(687.3, 69.8, 251.9, 5.8, 179.9, -172.5)
        pos_j = posj(5.8, 55.2, 49.6, 0.0, 75.2, -180)
        pos_rotated_t = posx(687.3, 69.8, 168.2, 5.8, 180.0, -127.6)
        pos_boven_rotated_j = posj(5.8, 52.5, 41.5, 0.0, 85.9, 7.5 + 45 - 180)
    elif tool == 2:
        pos_boven_t = posx(687.0, -20.4, 247.0, 1.2, -180.0, -87.1)
        pos_j = posj(-1.7, 54.6, 50.7, -0.0, 74.7, -90.0)
        pos_rotated_t = posx(687.1, -20.4, 168.6, 0.2, -180.0, -43.1)
        pos_boven_rotated_j = posj(-1.7, 51.9, 43.4, -0.0, 84.7, -45.0)

    movej(pos_boven_rotated_j, a = acceleration, v = velocity)
    movel(pos_rotated_t, a = ax, v = vx)
    # Cilinder
    movej(pos_j, a = ax, v = vx)
    movel(pos_boven_t, a=ax,v=vx)


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
    vx = 80
    ax = 60
    movej(traytelefoon_bovenj, v=velocity, a=acceleration)
    set_digital_output(1, 1)
    movel(traytelefoon, v=vx, a=ax)

    movel(traytelefoon_bovenl, v=vx, a=ax)
    movel(omdraaistation_telefoon_boven, v=velocity, a=acceleration)
    movel(omdraaistation_telefoon_schuif, v=vx, a=ax)
    movel(omdraaistation_telefoon, v=vx, a=ax)
    set_digital_output(1, 0)
    movel(omdraaistation_telefoon_boven, v=vx, a=ax)
    movej(home_pos_j,v=velocity, a=acceleration)
    #tool changen


vork_S1 = posx(488.1, -149.8, 88.3, 20.2, -179.3, (-27.2+90.0))
vork_S2 = posx(488.1, -177.2, 88.4, 20.9, -179.3, (-26.6+90.0))
vork_S3 = posx(488.1, -177.2, 102.1, 20.9, -179.3, (-26.6+90.0))
vork_S4 = posx(488.1, -177.2, 93.2, 20.9, -179.3, (-26.6+90.0))
vork_S5 = posx(488.1, -177.0, 101.5, 19.9, -179.3, (-27.6+90.0))
vork_S6 = posx(488.1, -190.3, 109.1, 19.9, -179.3, (-27.6+90.0))
vork_S7 = posx(488.1, -144.9, 96.4, 19.8, -179.3, (-27.7+90.0))
vork_S8 = posx(431.0, -246.0, 127.0, 112.7, -179.3, (-27.8+90.0))

vork_S9 = posx(460.8, -232.0, 92.4, 4.0, -169.1, -46.1)
vork_S91 = posx(463.4, -219.5, 91.5, 5.3, -167.4, -42.1)
vork_S92 = posx(470.8, -209.4, 88.8, 5.3, -167.4, -42.1)
vork_S93 = posx(470.7, -222.2, 89.0, 5.2, -167.4, -42.2)
vork_S94 = posx(470.7, -222.2, 97.3, 5.2, -167.4, -42.2)
#naar 93
vork_S95 = posx(470.7, -222.2, 103.4, 5.2, -167.4, -42.2)
vork_S96 = posx(449.0, -222.2, 95.8, 5.2, -167.4, -42.2)


vork_S10 = posx(472.0, -222.7, 87.8, 2.9, -166.6, (-137.0+90.0))
vork_S11 = posx(473.1, -222.7, 92.3, 2.9, -166.6, (-137.0+90.0))

def achterklep2():
    vx = 100
    ax = 60
    set_digital_output(2, 1)
    movel(vork_S1, v=velocity, a=acceleration)
    movel(vork_S2, v=vx, a=ax)
    movel(vork_S3, v=vx, a=ax)
    movel(vork_S4, v=vx, a=ax)
    set_digital_output(2, 0)
    movel(vork_S5, v=vx, a=ax)
    movel(vork_S6, v=vx, a=ax)
    movel(vork_S7, v=vx, a=ax)
    movel(vork_S8, v=vx, a=ax)
    movel(vork_S9, v=vx, a=ax)
    movel(vork_S91, v=vx, a=ax)
    movel(vork_S92, v=vx, a=ax)
    movel(vork_S93, v=vx, a=ax)
    set_digital_output(2, 1)
    movel(vork_S94, v=vx, a=ax)
    set_digital_output(2, 0)
    movel(vork_S93, v=vx, a=ax)
    movel(vork_S95, v=vx, a=ax)
    movel(vork_S96, v=vx, a=ax)
    movej(home_pos_j, v=velocity, a=acceleration)



test2 = posx(484.9, -262.0, 134.4, 14.1, -179.9, 13.5)
achterklep_oppakken_boven = posx(486.1, -236.5, 171.5, 153.1, 180.0, 153.2)
achterklep_oppakken_laag = posx(486.1, -236.5, 136.1, 153.2, 180.0, 153.3)
achterklep_basestation_hoog = posx(250.7, -193.6, 164.0, 65.6, -180.0, -26.8)
achterklep_basestation_laag = posx(250.7, -193.6, 145.3, 65.2, -180.0, -27.2)

def achterklep3():
    vx = velocity
    ax = acceleration
    set_digital_output(1, 1)
    movel(achterklep_oppakken_boven, v=velocity, a=acceleration)
    movel(achterklep_oppakken_laag, v=vx, a=ax) #
    #wait(3)
    movel(achterklep_oppakken_boven, v=vx/2, a=ax/2) #
    movel(achterklep_basestation_hoog, v=velocity, a=acceleration) #
    movel(achterklep_basestation_laag, v=velocity, a=acceleration) #
    set_digital_output(1, 0)
    movel(achterklep_basestation_hoog, v=velocity, a=acceleration)




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
    vx = velocity/2
    ax = acceleration/2
    movel(achterklep_omdraai_hoog, v=velocity, a=acceleration)
    #vacuum aan
    set_digital_output(1, 1)
    movel(achterklep_omdraai, v=vx, a=ax)
    movel(achterklep_opzij, v=vx, a=ax)
    movel(achterklep_omdraai_hoog, v=vx, a=ax)

    movej(home_pos_j,v=velocity, a=acceleration)

    movej(omdraaistation_p1,v=velocity, a=acceleration)
    movej(omdraaistation_p2,v=velocity, a=acceleration)
    movel(omdraaistation_p4,v=vx, a=ax)
    set_digital_output(1,0)
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
    vx = velocity
    ax = acceleration
    set_digital_output(1, 1)
    movel(batterij_boven, v=velocity, a=acceleration)
    movel(batterij_pos, v=vx, a=ax)
    #wait(1)
    movel(batterij_eruit, v=vx, a=ax)
    movel(batterij_eruit2, v=vx, a=ax)
    movel(batterij_erin2, v=velocity, a=acceleration)
    movel(batterij_erin, v=vx, a=ax)
    set_digital_output(1, 0)
    #wait(1)
    movel(batterij_erin2, v=vx, a=ax)


######################################################################################
##Voorrand demonteren station
######################################################################################
toolchanger_afstand = posj(-0.8, 28.3, 110.7, 76.5, 77.9, 0.0)
toolchanger_telefoon1 = posx(432.1, 132.9, 193.3, 91.2, 107.8, 137.8)
toolchanger_telefoon21 = posx(432.3, 133.0, 201.4, 91.1, 107.7, 137.9) #zet pos goed
toolchanger_telefoon22 = posx(441.0, 133.0, 201.4, 91.1, 107.7, 137.9)
#vacuum af
toolchanger_telefoon3 = posx(441.3, 120.3, 196.5, 91.2, 107.7, 138.0)

toolchanger_eraf1 = posx(441.4, 140.5, 244.0, 91.2, 107.7, 138.0)
toolchanger_eraf2= posx(441.4, 71.5, 244.0, 91.2, 107.7, 138.0)
voorrand_boven = posx(474.1, -0.4, 154.2, 70.8, -179.9, -64.1)
voorrand_eraf = posx(474.1, -0.4, 134.0, 70.8, -179.9, -64.1)


def voorrand_demonteren():
    vx = 80
    ax = 50
    movej(home_pos_j, v=velocity, a=acceleration)
    movej(toolchanger_afstand, v=velocity, a=acceleration)
    set_digital_output(1, 1)
    movel(toolchanger_telefoon1,v=vx,a=ax)
    movel(toolchanger_telefoon21, v=vx, a=ax)
    movel(toolchanger_telefoon22, v=vx, a=ax)
    set_digital_output(1, 0)
    movel(toolchanger_telefoon3, v=vx, a=ax)
    set_digital_output(1, 1)
    movel(toolchanger_telefoon22, v=vx, a=ax)

    movel(toolchanger_eraf1, v=vx, a=ax)
    movel(toolchanger_eraf2, v=vx, a=ax)
    movej(home_pos_j, v=velocity, a=acceleration)
    movel(voorrand_boven, v=velocity, a=acceleration)
    movel(voorrand_eraf, v=vx/5, a=ax/5)
    set_digital_output(1, 0)
    movel(voorrand_boven, v=velocity, a=acceleration)
    movej(home_pos_j, v=velocity, a=acceleration)

######################################################################################
##Voorrand verwijderen
######################################################################################

boven = posx(491.6, 0.5, 124.9, 138.0, 180.0, 178.5)
onder = posx(491.6, 0.5, 99.5, 136.9, 180.0, 177.4)
rotated = posx(491.6, -14.4, 97.9, 89.8, -167.4, 130.3)
opgepakt_1 = posx(491.5, -26.8, 96.1, 89.5, -167.4, 129.9)
opgepakt_2 = posx(491.5, -65.8, 99.4, 89.7, -160.6, 130.1)
opgepakt_3 = posx(491.5, -65.8, 89.9, 89.7, -160.6, 130.1)
opgepakt_4 = posx(491.5, -89.6, 89.9, 89.7, -160.6, 130.1)
opgepakt_5 = posx(491.5, -89.6, 245.4, 89.9, -124.4, 130.3)
opgepakt_6 = posx(491.5, -89.6, 245.4, 107.1, -141.9, 160.2)
opgepakt_7 = posj(-16.4, -8.5, 130.7, -46.8, 45.0, 67.1)
opgepakt_8 = posj(-36.2, -1.2, 122.9, 34.4, 35.6, -111.4)
opgepakt_9 = posx(288.4, -178.5, 217.4, 0.4, 126.2, -50.5)
opgepakt_10 =posx(264.2, -182.3, 217.3, 0.4, 126.3, -50.5)
opgepakt_11 = posx(231.5, -182.3, 207.8, 0.4, 126.2, -50.5)
opgepakt_12 = posx(174.5, -182.3, 160.5, 0.6, 126.2, -50.4)
opgepakt_13 = posx(152.5, -182.3, 105.9, 0.6, 126.2, -50.4)
opgepakt_14 = posx(194.3, -182.3, 105.9, 2.2, 167.7, -48.6)
opgepakt_15 = posx(194.3, -182.3, 99.3, 2.2, 167.7, -48.6)
opgepakt_16 = posx(157.3, -182.3, 99.3, 2.2, 167.7, -48.6)
opgepakt_17 = posx(157.3, -182.3, 110.3, 2.2, 167.7, -48.6)

def voorrand_verwijderen():
    vx = 100
    ax = 100
    movel(boven, v=vx, a=ax)
    movel(onder, v=vx, a=ax)
    movel(rotated, v=vx, a=ax)
    movel(opgepakt_1, v=vx, a=ax)
    movel(opgepakt_2, v=vx, a=ax)
    movel(opgepakt_3, v=vx, a=ax)
    movel(opgepakt_4, v=vx, a=ax)
    movel(opgepakt_5, v=vx, a=ax)
    movel(opgepakt_6, v=vx, a=ax)
    movej(opgepakt_7, v=vx, a=ax)
    movej(opgepakt_8, v=vx, a=ax)
    movel(opgepakt_9, v=vx, a=ax)
    movel(opgepakt_10, v=vx, a=ax)
    movel(opgepakt_11, v=vx, a=ax)
    movel(opgepakt_12, v=vx, a=ax)
    movel(opgepakt_13, v=vx, a=ax)
    movel(opgepakt_14, v=vx, a=ax)
    movel(opgepakt_15, v=vx, a=ax)
    movel(opgepakt_16, v=vx, a=ax)
    movel(opgepakt_17, v=vx, a=ax)

######################################################################################
##de rest van de telefoon naar tray verplaatsen
######################################################################################

bovenj = posj(3.6, 28.7, 100.2, 0.0, 51.1, 3.6)
schuif1 = posx(480.8, 30.3, 134.4, 179.0, 180.0, 179.0)
schuif2 = posx(492.2, 30.4, 134.9, 3.9, 179.9, 4.0)
schuif3 = posx(492.2, 16.9, 134.9, 3.9, 179.9, 4.0)
schuif4 = posx(492.2, 16.9, 145.1, 3.9, 179.9, 3.9)
pak1 = posx(492.2, 16.9, 203.0, 4.0, 179.9, 4.0)
pak2 = posx(256.7, -108.4, 199.2, 91.4, -179.9, -176.5)
pak3 = posx(256.7, -108.4, 145.0, 91.8, -179.9, -176.1)

def oppakken_laatstedeel():
    vx = 100
    ax = 60
    movej(bovenj, v=velocity, a=acceleration)
    movel(schuif1, v=vx, a=ax)
    set_digital_output(1, 1)
    movel(schuif2, v=vx, a=ax)
    movel(schuif3, v=vx, a=ax)
    set_digital_output(1, 0)
    movel(schuif4, v=vx, a=ax)
    set_digital_output(1, 1)
    movel(schuif3, v=vx, a=ax)
    movel(pak1, v=vx, a=ax)
    movel(pak2, v=vx, a=ax)
    movel(pak3, v=vx, a=ax)
    set_digital_output(1, 0)
    movel(pak2, v=vx, a=ax)
    movej(home_pos_j,v=velocity, a=acceleration)






######################################################################################
##Main loop
######################################################################################
def runall():
    set_digital_output(1,0)
    movej(home_pos_j,v=velocity, a=acceleration)
    grab_tool(1) #vacuum opppakken
    achterklep() #Oppakken vanaf de tray
    dump_tool(1) #vacuum wegzetten
    grab_tool(2) #spatel oppakken
    achterklep2() #achterklep losklikken met spatel
    dump_tool(2) #spatel wegzetten
    grab_tool(1) #vacuum oppakken
    achterklep3() #achterklep weghalen
    batterij() #batterij weghalen
    omdraaistation() #omdraaien
    voorrand_demonteren() #voorrand wegdrukken
    dump_tool(1) #vacuum wegzetten
    grab_tool(2) #spatel oppakken
    voorrand_verwijderen()
    dump_tool(2)  # spatel wegzetten
    grab_tool(1)  # vacuum oppakken
    oppakken_laatstedeel()
    dump_tool(1) #vacuum wegzetten

    movej(home_pos_j,v=velocity, a=acceleration)


runall()

#movej(home_pos_j,v=velocity, a=acceleration)
#grab_tool(2) # opppakken
#voorrand_verwijderen()
#achterklep2()  # deel met de spatel

#oppakken_laatstedeel()
#omdraaistation() #omdraaien
#voorrand_demonteren() #voorrand wegdrukken