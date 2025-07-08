label avg12374:
stop music

play music "ed9999.ogg"
scene avg_bg_058
show oc001_01 4 as p1 at r(-2), light, zorder 5
window show
with fade_in
play sfxvoice "avg_vocal_na10.ogg"
c13 '[textdict[1134071]]'
menu:
    extend ""
    "[textdict[1134072]]":
        call avg12375
    "[textdict[1134073]]":
        call avg12376
return