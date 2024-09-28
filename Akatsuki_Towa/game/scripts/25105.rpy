label avg25105:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7050.ogg"
play sfxvoice "avg_vocal_ch20.ogg"
show oc002_01 17 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210297]]'
play sfxvoice "avg_vocal_na05.ogg"
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210298]]'
hide c1portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210299]]'
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
hide c1portrait
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210300]]'
return