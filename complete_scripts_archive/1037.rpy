label avg1037:

play music "ed7201.ogg"
scene avg_bg_010
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
window show
with fade_in
c571 '[textdict[2100603]]'
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[2100604]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
c571 '[textdict[2100605]]'
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[2100606]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[2100607]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[2100608]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[2100609]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 5', 'p57', [l(-19), light, flip], 6)
c571 '[textdict[2100610]]'
hide p1
$ update_portrait('sc050_01 5', 'p57', [l(-19), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[2100611]]'
return