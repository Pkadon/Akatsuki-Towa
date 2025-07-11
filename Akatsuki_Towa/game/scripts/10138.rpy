label avg10138:

play music "ED6505.ogg"
scene avg_bg_028
window show
with fade_in
play sfx2 "other_7033.ogg"
c0 '[textdict[1007688]]'
c5691 '[textdict[1002313]]'
c5691 '[textdict[1002314]]'
c5691 '[textdict[1002315]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c21 '[textdict[1002316]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1002317]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfx2 "other_7021.ogg"
c13 '[textdict[1007413]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1007414]]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1007415]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1007416]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1007417]]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1007418]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1007419]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1007420]]'
return