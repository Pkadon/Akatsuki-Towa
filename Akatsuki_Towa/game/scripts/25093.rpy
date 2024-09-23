label avg25093:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
show oc002_01 21 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210263]]'
play sfxvoice "avg_vocal_na07.ogg"
hide c2portrait
show oc001_01 3 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210264]]'
play sfx2 "fight_6024.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210265]]'
menu:
    "[textdict[1214998]]":
        call avg25094
    "[textdict[1215000]]":
        call avg25026
return