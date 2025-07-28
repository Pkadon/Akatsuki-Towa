label avg1007:

play music "ed7106.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(2100095)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100096)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7036.ogg"
c561 '[convertstrid(2100097)]'
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100098)]'
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100099)]'
hide p56
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(2100100)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(2100101)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(2100102)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100103)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100104)]'
$ update_portrait('sc049_01 7', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100105)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[convertstrid(2100106)]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100107)]'
return