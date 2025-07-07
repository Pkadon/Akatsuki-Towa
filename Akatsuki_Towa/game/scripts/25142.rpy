label avg25142:
stop music

scene placeholderbackground
window show
with fade_out
play sfx2 "other_7092.ogg"
c0 '[textdict[1210444]]'
show oc002_01 14 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210445]]'
hide p2
show oc001_01 8 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210446]]'
hide p1
show oc002_01 5 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210447]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na10.ogg"
c13 '[textdict[1210448]]'
hide p1
show oc002_01 14 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1210449]]'
hide p2
show oc001_01 17 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210450]]'
menu:
    extend ""
    "[textdict[1210451]]":
        call avg25144
    "[textdict[1210452]]":
        call avg25145
    "[textdict[1210453]]":
        call avg25143
return