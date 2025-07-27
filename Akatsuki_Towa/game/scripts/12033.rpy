label avg12033:

play music "ed7150.ogg"
scene avg_bg_014
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7046.ogg"
c0 '[convertstrid(1120184)]'
c9691 '[convertstrid(1120185)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1120186)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c9691 '[convertstrid(1120187)]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1120188)]'
hide p2
play sfx2 "other_7081.ogg"
c9733 '[convertstrid(1120189)]'
c9691 '[convertstrid(1120190)]'
c9691 '[convertstrid(1120191)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1120192)]'
hide p2
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1120193)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
c9691 '[convertstrid(1120194)]'
hide p1
play sfx2 "other_7081.ogg"
c9733 '[convertstrid(1120195)]'
return