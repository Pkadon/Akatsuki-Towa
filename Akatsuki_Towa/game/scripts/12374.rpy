label avg12374:

$ play_music("ed9999.ogg")
scene avg_bg_058
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na10.ogg"
c13 '[convertstrid(1134071)]'
menu:
    extend ""
    "[textdict[1134072]]":
        call avg12375
    "[textdict[1134073]]":
        call avg12376
return