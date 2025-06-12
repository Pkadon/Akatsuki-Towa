label avg25123:
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210367]]'
play sfxvoice "avg_vocal_ch12.ogg"
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210368]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210369]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25124
    "[textdict[1214996]]":
        call avg25026
return