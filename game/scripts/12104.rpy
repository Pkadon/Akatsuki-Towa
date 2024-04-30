label avg12104:
stop music

play music "ed7111.ogg"
scene avg_bg_047
with fade
play sfx2 "common_select.ogg"
show oc001_01 4 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1128019)]]'
play sfxvoice "avg_vocal_ji11.ogg"
hide c1portrait
show oc001_01 4 as c1portrait at darkleft(-2), zorder 6
show oc005_01 5 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[str(1128020)]]'
hide c5portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkleft(-2), zorder 6
show oc005_01 4 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[str(1128021)]]'
hide c5portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkleft(-2), zorder 6
show oc005_01 10 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[str(1128022)]]'
hide c1portrait
hide c5portrait
show oc005_01 10 as c5portrait at darkright(-6), zorder 5
show oc001_01 18 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1128023)]]'
play sfx2 "common_quest.ogg"
hide c5portrait
hide c1portrait
show oc001_01 18 as c1portrait at darkleft(-2), zorder 6
show oc005_01 1 as c5portrait at rightside(-6), zorder 5
c53 '[textdict[str(1128024)]]'
return