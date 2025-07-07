label avg20029:
stop music

play music "ed7150.ogg"
scene placeholderbackground
show oc001_01 1 as p1 at mid(-2), light, zorder 5
window show
with fade_out
play sfxvoice "avg_vocal_na17.ogg"
c13 '[textdict[1002135]]'
menu:
    extend ""
    "[textdict[1002136]]":
        call avg20030
    "[textdict[1002137]]":
        call avg20031
return