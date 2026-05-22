label avg25018:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1210039)]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210040)]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
play sfx2 "common_36rewardsp.ogg"
c23 '[convertstrid(1210041)]'
return