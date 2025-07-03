label avg25029:
stop music

scene placeholderbackground
with fade
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
show oc002_01 4 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210071]]'
play sfxvoice "avg_vocal_na02.ogg"
hide p2
show oc001_01 7 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210072]]'
hide p1
show uc001_01 1 as p2000 at mid(-2), light, zorder 5
c20003 '[textdict[1210073]]'
return