label avg25291:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 3 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211106]]'
play sfxvoice "avg_vocal_ch22.ogg"
hide p1
show oc002_01 3 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1211107]]'
play sfxvoice "avg_vocal_na03.ogg"
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1211108]]'
return