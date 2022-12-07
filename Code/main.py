from DRCF import *

pose1 = posx(-312.6, -305.2, 132.4, 93.3, -147.4, 145.2)
pose2 = posx(155.9, -597.1, 743.5, 105.3, -63.7, 149.3)
pose3 = posx(344.3, -512.0, 259.1, 114.5, -120.3, 120.7)
while(1):
    movel(pose1, v=130, a=30)
    movel(pose2, v=130, a=30)
    movel(pose3, v=130, a=30)