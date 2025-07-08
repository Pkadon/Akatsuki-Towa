label avg100908:
stop music

scene placeholderbackground
show oc001_01 2 as p1 at r(-2), light, zorder 5
window show
with fade_out
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1218033]]'
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218034]]'
hide p1
hide p9
show sc001_01 1 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 12 as p1 at r(-2), light, zorder 5
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1218035]]'
hide p9
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc001_01 1 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218036]]'
hide p9
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc001_01 5 as p9 at l(-11), light, flip, zorder 6
c91 '[textdict[1218037]]'
hide p1
hide p9
show sc001_01 5 as p9 at l(-11), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1218038]]'
menu:
    extend ""
    "[textdict[1218039]]":
        call avg100909
    "[textdict[1218040]]":
        call avg100910
    "[textdict[1218041]]":
        call avg100911
return