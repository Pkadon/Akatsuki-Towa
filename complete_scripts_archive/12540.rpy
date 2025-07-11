label avg12540:

play music "ED6105.ogg"
scene avg_bg_010
window show
with fade_in
c0 '[textdict[1152912]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1152913]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1152914]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1152915]]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1152916]]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1152917]]'
return