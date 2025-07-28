label avg20047:

play music "ED6505.ogg"
scene avg_bg_027
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1002746)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1002747)]'
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1002748)]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1002749)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1002750)]'
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1002751)]'
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1002752)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1002753)]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1002754)]'
return