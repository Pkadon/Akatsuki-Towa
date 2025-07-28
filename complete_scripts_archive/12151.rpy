label avg12151:

play music "ED6505.ogg"
scene avg_bg_027
$ update_portrait('uc004_02 1', 'p960', [l(-9), light, flip], 6)
$ update_narrator('c9601')
window show
with fade_in
play sfx2 "other_7060.ogg"
c9601 '[convertstrid(1128367)]'
$ update_portrait('uc004_02 1', 'p960', [l(-9), dark, flip], 5)
$ update_portrait('uc004_02 2', 'p961', [r(-9), light], 6)
c9613 '[convertstrid(1128368)]'
hide p961
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1128369)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1128370)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('uc004_02 1', 'p960', [l(-9), light, flip], 6)
c9601 '[convertstrid(1128371)]'
play music "ED6107.ogg"
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7021.ogg"
c0 '[convertstrid(1128373)]'
scene avg_bg_038
$ update_narrator('c9621')
with fade
c9621 '[convertstrid(1128374)]'
c9621 '[convertstrid(1128375)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1128376)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c9621 '[convertstrid(1128377)]'
c9621 '[convertstrid(1128378)]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12154
    "[textdict[1100002]]":
        call avg12153
return