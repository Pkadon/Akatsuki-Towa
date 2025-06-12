label avg20029:
stop music

play music "ed7150.ogg"
scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na17.ogg"
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1002135]]'
menu:
    extend ""
    "[textdict[1002136]]":
        call avg20030
    "[textdict[1002137]]":
        call avg20031
return