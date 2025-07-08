label avg12175:
stop music

play music "ED6505.ogg"
scene avg_bg_027
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na04_b.ogg"
c13 '[textdict[1120523]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1120524]]'
hide p1
hide p3
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1120525]]'
hide p3
hide p2
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1120526]]'
hide p2
hide p3
$ update_portrait('oc003_01 14', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 5)
c23 '[textdict[1120527]]'
hide p3
hide p2
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[textdict[1120528]]'
return