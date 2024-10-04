label avg25019:
stop music

scene placeholderbackground
with fade
c20083 '[textdict[1210042]]'
c20093 '[textdict[1210043]]'
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210044]]'
hide c2portrait
c20083 '[textdict[1210045]]'
c20093 '[textdict[1210046]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25020
    "[textdict[1215000]]":
        call avg25026
return