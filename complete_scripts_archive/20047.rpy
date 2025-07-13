label avg20047:

play music "ED6505.ogg"
scene avg_bg_027
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1002746]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1002747]]'
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
c23 '[textdict[1002748]]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
c13 '[textdict[1002749]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 5)
c23 '[textdict[1002750]]'
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 5)
c23 '[textdict[1002751]]'
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1002752]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1002753]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1002754]]'
return