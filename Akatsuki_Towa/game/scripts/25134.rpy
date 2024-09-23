label avg25134:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na18.ogg"
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210405]]'
play sfxvoice "avg_vocal_ch08.ogg"
hide c1portrait
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210406]]'
play sfx2 "other_7088.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210407]]'
play sfxvoice "avg_vocal_ch06.ogg"
hide c1portrait
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210408]]'
return