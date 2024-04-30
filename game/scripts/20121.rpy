label avg20121:
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na15.ogg"
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1006222)]]'
menu:
    "[textdict[str(1006223)]]":
        call avg10111
    "[textdict[str(1006224)]]":
        call avg10112
    "[textdict[str(1006225)]]":
        call avg10111
return