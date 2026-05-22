label avg12368:

$ play_music("ed7121.ogg")
scene avg_bg_045
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7047.ogg"
c13 '[convertstrid(1133832)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c6601 '[convertstrid(1133833)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133834)]'
hide p2
hide p1
play sfx2 "other_7021.ogg"
c0 '[convertstrid(1133835)]'
c6601 '[convertstrid(1133836)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133837)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1133838)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133839)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
c6601 '[convertstrid(1133840)]'
c6601 '[convertstrid(1133841)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1133842)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c6601 '[convertstrid(1133843)]'
return