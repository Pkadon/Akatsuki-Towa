label avg25073:
stop music

scene placeholderbackground
with fade
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210227]]'
play sfxvoice "avg_vocal_na10.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210228]]'
menu:
    "[textdict[1210240]]":
        call avg25074
    "[textdict[1210241]]":
        call avg25075
return