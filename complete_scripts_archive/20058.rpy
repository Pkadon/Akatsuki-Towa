label avg20058:

play music "ed7151.ogg"
scene avg_bg_001
$ update_narrator('c4971')
window show
with fade_in
play sfx2 "other_7071.ogg"
c4971 '[convertstrid(1002982)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002983)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7073.ogg"
c13 '[convertstrid(1002984)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002985)]'
return