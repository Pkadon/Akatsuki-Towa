label avg20098:
stop music

play music "ed7104.ogg"
scene avg_bg_027
window show
with fade_in
show oc001_01 2 as p1 at l_entrance(-2), light, flip, zorder 6
play sfx2 "other_7043.ogg"
c11 '[textdict[1004834]]'
hide p1
show oc001_01 2 as p1 at l(-2), dark, flip, zorder 6
show oc002_01 10 as p2 at r(-3), light, zorder 5
c23 '[textdict[1004835]]'
hide p1
hide p2
show oc002_01 10 as p2 at r(-3), dark, zorder 5
show oc001_01 8 as p1 at l(-2), light, flip, zorder 6
play sfxvoice "avg_vocal_na06.ogg"
c11 '[textdict[1004836]]'
return