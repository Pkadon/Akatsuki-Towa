label avg25037:
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210095]]'
hide c2portrait
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210096]]'
play sfx2 "fight_6024.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210097]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25038
    "[textdict[1215000]]":
        call avg25026
return