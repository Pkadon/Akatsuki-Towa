label avg22367:

play music "ed7202.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1133821)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133822)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_exit(-2), light], 6)
c13 '[convertstrid(1133823)]'
hide p1
scene avg_bg_070
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfx2 "other_7050.ogg"
c21 '[convertstrid(1133824)]'
scene placeholderbackground
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1133825)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c21 '[convertstrid(1133826)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133827)]'
hide p2
hide p1
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1133828)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133829)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133830)]'
return