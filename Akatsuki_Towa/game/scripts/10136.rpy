label avg10136:
stop music

play music "ED6505.ogg"
scene avg_bg_027
window show
with fade_in
c0 '[textdict[1007379]]'
show oc002_01 6 as p2 at l_entrance(-3), light, flip, zorder 6
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[textdict[1007380]]'
hide p2
show oc001_01 2 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1007381]]'
hide p1
show oc001_01 2 as p1 at l(-2), dark, flip, zorder 6
show uc004_02 5 as p570 at r_entrance(-9), light, zorder 5
play sfx2 "other_7021.ogg"
c5703 '[textdict[1007382]]'
hide p1
hide p570
show uc004_02 5 as p570 at r(-9), dark, zorder 5
show oc002_01 4 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1007383]]'
hide p570
hide p2
show oc002_01 4 as p2 at l(-3), dark, flip, zorder 6
show uc004_02 2 as p961 at r(-9), light, zorder 5
c9613 '[textdict[1007384]]'
hide p2
hide p961
show uc004_02 2 as p961 at r(-9), dark, zorder 5
show oc001_01 22 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1007385]]'
hide p961
hide p1
show oc001_01 22 as p1 at l(-2), dark, flip, zorder 6
show uc004_02 1 as p961 at r(-9), light, zorder 5
c9613 '[textdict[1007386]]'
hide p1
hide p961
show uc004_02 1 as p961 at r(-9), dark, zorder 5
show oc001_01 23 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1007387]]'
hide p961
hide p1
show oc001_01 23 as p1 at l(-2), dark, flip, zorder 6
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1007682]]'
hide p1
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
show oc001_01 10 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1007683]]'
return