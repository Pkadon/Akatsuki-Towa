label avg20121:
stop music

scene placeholderbackground
show oc001_01 1 as p1 at mid(-2), light, zorder 5
window show
with fade_out
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