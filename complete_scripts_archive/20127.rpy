label avg20127:

play music "ed7103.ogg"
scene avg_bg_019
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1006627)]'
menu:
    extend ""
    "[textdict[1006628]]":
        call avg20128
    "[textdict[1006629]]":
        call avg20129
return