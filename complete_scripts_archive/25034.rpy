label avg25034:
stop music

scene placeholderbackground
with fade
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210087]]'
hide p1
show oc002_01 2 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210088]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210089]]'
hide p1
show oc002_01 12 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210090]]'
hide p2
show oc001_01 18 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210091]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25035
    "[textdict[1215000]]":
        call avg25026
return