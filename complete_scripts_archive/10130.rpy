label avg10130:

play music "ed7110.ogg"
scene avg_bg_018
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1007298)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007299)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), light], 6)
c23 '[convertstrid(1007300)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007301)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 13', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1007302)]'
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007303)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1007304)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
c11 '[convertstrid(1007305)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007306)]'
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007307)]'
play music "ed7106.ogg"
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7020.ogg"
c23 '[convertstrid(1007308)]'
hide p1
hide p2
$ update_narrator('c9673')
with fade
play sfx2 "other_7088.ogg"
c9673 '[convertstrid(1007309)]'
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(1007310)]'
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
c9673 '[convertstrid(1007311)]'
hide p2
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
c11 '[convertstrid(1007312)]'
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 5)
c9673 '[convertstrid(1007313)]'
c9673 '[convertstrid(1007314)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
c23 '[convertstrid(1007315)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007316)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[convertstrid(1007317)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1007318)]'
return