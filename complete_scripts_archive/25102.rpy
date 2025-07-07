label avg25102:
stop music

scene placeholderbackground
show oc002_01 2 as p2 at mid(-3), light, zorder 5
window show
with fade_out
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210286]]'
hide p2
play sfx2 "other_7051.ogg"
c20073 '[textdict[1210287]]'
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210288]]'
hide p1
c20073 '[textdict[1210289]]'
menu:
    extend ""
    "[textdict[1214995]]":
        call avg25103
    "[textdict[1215000]]":
        call avg25000
return