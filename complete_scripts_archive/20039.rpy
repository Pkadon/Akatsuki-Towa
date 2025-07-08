label avg20039:
stop music

play music "ED6200.ogg"
scene avg_bg_010
show oc002_01 12 as p2 at r(-3), light, zorder 5
window show
with fade_out
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1002318]]'
hide p2
show uc004_02 1 as p570 at r(-9), light, zorder 5
c5703 '[textdict[1002319]]'
hide p570
show uc004_02 1 as p570 at r(-9), dark, zorder 5
show sc017_01 1 as p571 at l(-7), light, flip, zorder 6
c5711 '[textdict[1002320]]'
hide p571
hide p570
show uc004_02 1 as p570 at r(-9), dark, zorder 5
show sc017_01 1 as p571 at l(-7), light, flip, zorder 6
c5711 '[textdict[1002321]]'
hide p570
hide p571
show sc017_01 1 as p571 at l(-7), dark, flip, zorder 6
show uc004_02 1 as p570 at r(-9), light, zorder 5
c5703 '[textdict[1002322]]'
hide p571
hide p570
show oc002_01 17 as p2 at r(-3), light, zorder 5
with fade
play sfxvoice "avg_vocal_ch21.ogg"
c23 '[textdict[1002323]]'
hide p2
show oc002_01 17 as p2 at r(-3), dark, zorder 5
show oc001_01 2 as p1 at l(-2), light, flip, zorder 6
play sfxvoice "avg_vocal_na02.ogg"
c11 '[textdict[1002324]]'
hide p1
hide p2
show oc002_01 17 as p2 at r(-3), dark, zorder 5
show oc001_01 4 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1002325]]'
return