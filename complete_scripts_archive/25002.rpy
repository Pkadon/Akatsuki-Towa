label avg25002:
stop music

scene placeholderbackground
show oc002_01 1 as p2 at mid(-3), light, zorder 5
window show
with fade_in
play sfx2 "common_select.ogg"
c23 '[textdict[1210002]]'
hide p2
show oc001_01 7 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210003]]'
return