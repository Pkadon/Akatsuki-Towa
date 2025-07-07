label avg25160:
stop music

scene placeholderbackground
window show
with fade_out
play sfx2 "fight_6022.ogg"
c20153 '[textdict[1210517]]'
play sfx2 "other_7080.ogg"
c20163 '[textdict[1210518]]'
c20153 '[textdict[1210519]]'
show oc002_01 9 as p2 at mid(-3), light, zorder 5
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[1210520]]'
hide p2
show oc001_01 9 as p1 at mid(-2), light, zorder 5
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na24.ogg"
c13 '[textdict[1210521]]'
return