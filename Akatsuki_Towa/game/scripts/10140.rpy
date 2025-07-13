label avg10140:

play music "ED6505.ogg"
scene avg_bg_027
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1007442]]'
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('uc004_02 4', 'p961', [l(-9), light, flip], 6)
c9611 '[textdict[1007443]]'
hide p961
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007444]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 5)
c33 '[textdict[1007445]]'
hide p1
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('uc004_02 4', 'p961', [l(-9), light, flip], 6)
c9611 '[textdict[1007446]]'
hide p3
$ update_portrait('uc004_02 4', 'p961', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1007447]]'
return