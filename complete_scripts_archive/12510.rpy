label avg12510:

play music "ed7516.ogg"
scene avg_bg_014
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
c31 '[textdict[1150946]]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1150947]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1150948]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1150949]]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1150950]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1150951]]'
return