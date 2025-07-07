label avg25093:
stop music

scene placeholderbackground
with fade
show oc002_01 21 as p2 at mid(-3), light, zorder 5
play sfx2 "other_7079.ogg"
c23 '[textdict[1210263]]'
hide p2
show oc001_01 3 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na07.ogg"
c13 '[textdict[1210264]]'
hide p1
show oc002_01 9 as p2 at mid(-3), light, zorder 5
play sfx2 "fight_6024.ogg"
c23 '[textdict[1210265]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25094
    "[textdict[1215000]]":
        call avg25026
return