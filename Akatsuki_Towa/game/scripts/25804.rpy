label avg25804:
stop music

scene placeholderbackground
with fade
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1211259]]'
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211260]]'
play sfx2 "fight_6026.ogg"
hide c1portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211261]]'
play sfx2 "other_7034.ogg"
play sfxvoice "bcv_oc001_win_02.ogg"
hide c1portrait
show oc001_01 5 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211262]]'
return