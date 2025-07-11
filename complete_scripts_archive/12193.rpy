label avg12193:

play music "ED6200.ogg"
scene avg_bg_039
window show
with fade_in
c9853 '[textdict[1120754]]'
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c21 '[textdict[1120755]]'
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 6)
c9853 '[textdict[1120756]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120757]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 6)
c9853 '[textdict[1120758]]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120759]]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 6)
c9853 '[textdict[1120760]]'
c9853 '[textdict[1120761]]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[textdict[1120762]]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 6)
c9853 '[textdict[1120763]]'
c9853 '[textdict[1120764]]'
c9853 '[textdict[1120765]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120766]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120767]]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
c9853 '[textdict[1120768]]'
return