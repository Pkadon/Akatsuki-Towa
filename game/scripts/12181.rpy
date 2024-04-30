label avg12181:
stop music

play music "ED6104.ogg"
scene avg_bg_010
with fade
c00 '[textdict[str(1007707)]]'
show oc001_01 1 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1120600)]]'
hide c1portrait
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(1120601)]]'
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show oc002_01 2 as c2portrait at leftside(-3), shakeleft, zorder 5
c21 '[textdict[str(1120602)]]'
hide c2portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show oc002_01 6 as c2portrait at leftside(-3), zorder 5
c21 '[textdict[str(1120603)]]'
hide c2portrait
hide c1portrait
show sc022_01 2 as c500portrait at leftside(-9), zorder 5
with fade
c5001 '[textdict[str(1120604)]]'
play sfxvoice "avg_vocal_ch05.ogg"
hide c500portrait
show sc022_01 2 as c500portrait at darkleft(-9), zorder 6
show oc002_01 6 as c2portrait at rightsideentrance(-3), zorder 5
c23 '[textdict[str(1120605)]]'
hide c2portrait
hide c500portrait
show sc022_01 2 as c500portrait at darkleft(-9), zorder 6
show oc002_01 12 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1120606)]]'
hide c500portrait
hide c2portrait
show oc002_01 12 as c2portrait at darkright(-3), zorder 5
show sc022_01 1 as c30portrait at leftside(-9), shakeleft, zorder 5
c301 '[textdict[str(1120607)]]'
hide c2portrait
hide c30portrait
show sc022_01 1 as c30portrait at darkleft(-9), zorder 6
show oc002_01 12 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1120608)]]'
hide c30portrait
hide c2portrait
c00 '[textdict[str(1120609)]]'
show sc022_01 1 as c30portrait at leftside(-9), zorder 5
c301 '[textdict[str(1120610)]]'
hide c30portrait
show sc022_01 1 as c30portrait at darkleft(-9), zorder 6
show oc001_01 1 as c1portrait at rightsideexit(-2), zorder 5
c13 '[textdict[str(1120611)]]'
hide c1portrait
hide c30portrait
show sc022_01 4 as c30portrait at leftside(-9), zorder 5
c301 '[textdict[str(1120612)]]'
play sfx2 "other_7004.ogg"
hide c30portrait
c00 '[textdict[str(1120613)]]'
show sc022_01 4 as c30portrait at leftside(-9), zorder 5
c301 '[textdict[str(1120614)]]'
hide c30portrait
show sc022_01 4 as c30portrait at leftside(-9), zorder 5
c301 '[textdict[str(1120615)]]'
hide c30portrait
show sc022_01 1 as c30portrait at leftside(-9), zorder 5
c301 '[textdict[str(1120616)]]'
return