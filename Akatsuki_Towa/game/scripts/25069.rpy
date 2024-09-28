label avg25069:
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210220]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210221]]'
menu:
    "[textdict[1214997]]":
        call avg25070
    "[textdict[1215000]]":
        call avg25026
return