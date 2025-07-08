label avg25073:
stop music

scene placeholderbackground
show oc002_01 9 as p2 at mid(-3), light, zorder 5
window show
with fade_in
c23 '[textdict[1210227]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na10.ogg"
c13 '[textdict[1210228]]'
menu:
    extend ""
    "[textdict[1210240]]":
        call avg25074
    "[textdict[1210241]]":
        call avg25075
return