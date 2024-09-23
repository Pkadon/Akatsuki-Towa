label avg25019:
stop music

scene placeholderbackground
with fade
c20080 '[textdict[1210042]]'
c20090 '[textdict[1210043]]'
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210044]]'
hide c2portrait
c20080 '[textdict[1210045]]'
c20090 '[textdict[1210046]]'
menu:
    "[textdict[1214999]]":
        call avg25020
    "[textdict[1215000]]":
        call avg25026
return