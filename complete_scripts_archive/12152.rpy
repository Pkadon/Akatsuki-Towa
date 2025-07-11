label avg12152:

play music "ed7104.ogg"
scene avg_bg_027
$ update_portrait('uc004_02 1', 'p960', [l(-9), light, flip], 6)
window show
with fade_in
play sfx2 "other_7060.ogg"
c9601 '[textdict[1128367]]'
$ update_portrait('uc004_02 1', 'p960', [l(-9), dark, flip], 6)
$ update_portrait('uc004_02 2', 'p961', [r(-9), light], 5)
c9613 '[textdict[1128368]]'
hide p961
$ update_portrait('uc004_02 1', 'p960', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1128369]]'
hide p1
$ update_portrait('uc004_02 1', 'p960', [l(-9), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1128370]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('uc004_02 1', 'p960', [l(-9), light, flip], 6)
c9601 '[textdict[1128371]]'
scene avg_bg_070
with fade
play sfx2 "other_7021.ogg"
c0 '[textdict[1128373]]'
scene avg_bg_029
with fade
c9621 '[textdict[1128374]]'
c9621 '[textdict[1128375]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1128376]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c9621 '[textdict[1128377]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c9621 '[textdict[1128378]]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12155
    "[textdict[1100002]]":
        call avg12153
return