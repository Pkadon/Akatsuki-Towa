label avg20013:

play music "ed7150.ogg"
scene avg_bg_014
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1000935]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch04_b.ogg"
c23 '[textdict[1000936]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
c13 '[textdict[1000937]]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
c13 '[textdict[1000938]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1000939]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1000940]]'
return