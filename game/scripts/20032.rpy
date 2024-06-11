label avg20032:
stop music

play music "ed7104.ogg"
scene avg_bg_001
with fade
play sfxvoice "avg_vocal_na02.ogg"
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1002165]]'
play sfxvoice "avg_vocal_ch11.ogg"
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1002166]]'
hide c2portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1002167]]'
return