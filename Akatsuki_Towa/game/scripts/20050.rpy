label avg20050:

play music "ED6505.ogg"
scene avg_bg_027
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1002777]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 5)
c33 '[textdict[1002778]]'
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 5)
c33 '[textdict[1002779]]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [mid(-5), light], 5)
c43 '[textdict[1002780]]'
$ update_portrait('oc004_01 4', 'p4', [mid(-5), light], 5)
c43 '[textdict[1002781]]'
$ update_portrait('oc004_01 21', 'p4', [mid(-5), light], 5)
c43 '[textdict[1002782]]'
$ update_portrait('oc004_01 4', 'p4', [mid(-5), light], 5)
c43 '[textdict[1002783]]'
hide p4
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch20.ogg"
c23 '[textdict[1002784]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1002785]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1002786]]'
return