label avg25291:
stop music

scene placeholderbackground
show oc001_01 3 as p1 at mid(-2), light, zorder 5
window show
with fade_out
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1211106]]'
hide p1
show oc002_01 3 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch22.ogg"
c23 '[textdict[1211107]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1211108]]'
return