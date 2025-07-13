label avg10027:

play music "ED6104.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1002326]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 11', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch18.ogg"
c21 '[textdict[1002327]]'
$ update_portrait('oc002_01 11', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1002328]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1002329]]'
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1002330]]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1002331]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1002332]]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[textdict[1002333]]'
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1002334]]'
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1002335]]'
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c21 '[textdict[1002336]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1002337]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1002338]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro04.ogg"
c31 '[textdict[1002339]]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1002340]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1002341]]'
return