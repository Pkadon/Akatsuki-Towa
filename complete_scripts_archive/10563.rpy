label avg10563:

play music "ed7151.ogg"
scene avg_bg_108
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1154311]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1154312]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1154313]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1154314]]'
return