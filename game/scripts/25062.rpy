label avg25062:
stop music

scene placeholderbackground
with fade
play sfx2 "common_select.ogg"
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210181)]]'
play sfxvoice "avg_vocal_na05.ogg"
hide c1portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210182)]]'
hide c1portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210183)]]'
return