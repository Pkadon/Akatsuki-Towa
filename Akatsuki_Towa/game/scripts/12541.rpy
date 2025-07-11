label avg12541:

play music "ED6200.ogg"
scene avg_bg_010
window show
with fade_in
c0 '[textdict[1152919]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1152920]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch19.ogg"
c23 '[textdict[1152921]]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1152922]]'
return