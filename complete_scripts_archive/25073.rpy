label avg25073:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1210227]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[textdict[1210228]]'
menu:
    extend ""
    "[textdict[1210240]]":
        call avg25074
    "[textdict[1210241]]":
        call avg25075
return