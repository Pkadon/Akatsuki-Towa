label avg12459:

play music "ed7300.ogg"
scene avg_bg_071
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1143735]]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 5)
c23 '[textdict[1143736]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1143737]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1143738]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1143739]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1143740]]'
hide p2
play sfx2 "other_7074.ogg"
c0 '[textdict[1143741]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
play sfx2 "other_7073.ogg"
c23 '[textdict[1143742]]'
return