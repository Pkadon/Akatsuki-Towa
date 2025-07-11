label avg20127:

scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1006627]]'
menu:
    extend ""
    "[textdict[1006628]]":
        call avg20128
    "[textdict[1006629]]":
        call avg20129
return