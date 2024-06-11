label avg25032:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210078]]'
play sfx2 "fight_6025.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210079]]'
play sfx2 "other_7034.ogg"
hide c2portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210080]]'
play sfxvoice "avg_vocal_ch07.ogg"
hide c2portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210081]]'
hide c2portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210082]]'
return