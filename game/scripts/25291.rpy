label avg25291:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 3 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211106]]'
play sfxvoice "avg_vocal_ch22.ogg"
hide c1portrait
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1211107]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1211108]]'
return