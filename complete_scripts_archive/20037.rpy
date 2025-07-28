label avg20037:

play music "ED6505.ogg"
scene avg_bg_027
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1007684)]'
play sfx2 "other_7064.ogg"
c5671 '[convertstrid(1002305)]'
c5683 '[convertstrid(1002306)]'
c5683 '[convertstrid(1002307)]'
c5683 '[convertstrid(1002308)]'
c5683 '[convertstrid(1002309)]'
c5671 '[convertstrid(1002310)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002311)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c21 '[convertstrid(1002312)]'
return