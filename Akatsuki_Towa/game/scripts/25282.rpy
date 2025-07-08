label avg25282:
stop music

scene placeholderbackground
show oc001_01 1 as p1 at mid(-2), light, zorder 5
window show
with fade_in
play sfx2 "fight_6025.ogg"
c13 '[textdict[1211068]]'
hide p1
c20153 '[textdict[1211069]]'
show oc002_01 19 as p2 at mid(-3), light, zorder 5
play sfx2 "fight_6010.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1211070]]'
hide p2
play sfx2 "other_7057.ogg"
c20153 '[textdict[1211071]]'
show oc002_01 21 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1211072]]'
hide p2
c20153 '[textdict[1211073]]'
play sfx2 "other_7086.ogg"
c0 '[textdict[1211074]]'
show oc001_01 8 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1211075]]'
return