label avg25102:
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210286]]'
play sfx2 "other_7051.ogg"
hide c2portrait
c20073 '[textdict[1210287]]'
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210288]]'
hide c1portrait
c20073 '[textdict[1210289]]'
menu:
    "[textdict[1214995]]":
        call avg25103
    "[textdict[1215000]]":
        call avg25000
return