label avg25099:
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210276]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210277]]'
play sfx2 "fight_6025.ogg"
hide c1portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210278]]'
hide c1portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210279]]'
return