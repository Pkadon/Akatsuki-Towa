label avg12545:
stop music

play music "ED6105.ogg"
scene avg_bg_010
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[textdict[1152953]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 5)
c43 '[textdict[1152954]]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1152955]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152956]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152957]]'
return