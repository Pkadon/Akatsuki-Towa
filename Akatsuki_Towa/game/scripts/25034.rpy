label avg25034:
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210087]]'
play sfxvoice "avg_vocal_ch12.ogg"
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210088]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210089]]'
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210090]]'
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210091]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25035
    "[textdict[1215000]]":
        call avg25026
return