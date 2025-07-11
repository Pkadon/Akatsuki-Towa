label avg20121:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1006222]]'
menu:
    extend ""
    "[textdict[1006223]]":
        call avg10111
    "[textdict[1006224]]":
        call avg10112
    "[textdict[1006225]]":
        call avg10111
return