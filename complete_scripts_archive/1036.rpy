label avg1036:

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
window show
with fade_in
c571 '[textdict[2100593]]'
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[2100594]]'
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[2100595]]'
hide p2
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100596]]'
hide p57
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[2100597]]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[2100598]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l_entrance(-19), light, flip], 6)
c571 '[textdict[2100599]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 5', 'p57', [l(-19), light, flip], 6)
c571 '[textdict[2100600]]'
hide p1
$ update_portrait('sc050_01 5', 'p57', [l(-19), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[2100601]]'
return