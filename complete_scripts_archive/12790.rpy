label avg12790:

play music "ed6323.ogg"
scene avg_bg_214
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1176764)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1176765)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1176766)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1176767)]'
return