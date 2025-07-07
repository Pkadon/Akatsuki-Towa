label avg20032:
stop music

play music "ed7104.ogg"
scene avg_bg_001
show oc001_01 7 as p1 at mid(-2), light, zorder 5
window show
with fade_out
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1002165]]'
hide p1
show oc002_01 12 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1002166]]'
hide p2
show oc002_01 4 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1002167]]'
return