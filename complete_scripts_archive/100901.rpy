label avg100901:
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na19.ogg"
show oc001_01 1 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1218002]]' with shake
hide p1
show sc001_01 6 as p9 at mid(-11), light, zorder 5
c93 '[textdict[1218003]]'
hide p9
show sc001_01 2 as p9 at mid(-11), light, zorder 5
c93 '[textdict[1218004]]'
hide p9
show sc001_01 1 as p9 at mid(-11), light, zorder 5
c93 '[textdict[1218005]]'
play sfxvoice "avg_vocal_na15.ogg"
hide p9
show oc001_01 11 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1218006]]'
return