label avg12194:
stop music

play music "ED6200.ogg"
scene avg_bg_023
$ update_portrait('st018_01 3', 'p217', [r(-16), light], 5)
window show
with fade_in
c2173 '[textdict[1120770]]'
hide p217
c0 '[textdict[1120771]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1120772]]'
hide p2
$ update_portrait('st017_01 2', 'p216', [r(-18), light], 5)
c2163 '[textdict[1120773]]'
hide p216
$ update_portrait('st019_01 5', 'p218', [r(-17), light], 5)
c2183 '[textdict[1120774]]'
hide p218
$ update_portrait('oc002_01 19', 'p2', [r(-3), light], 5)
c23 '[textdict[1120775]]'
$ update_portrait('oc002_01 19', 'p2', [r(-3), dark], 5)
$ update_portrait('st009_01 2', 'p209', [l(-22), light, flip], 6)
c2091 '[textdict[1120776]]'
$ update_portrait('st009_01 2', 'p209', [l(-22), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1120777]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st009_01 4', 'p209', [l(-22), light, flip], 6)
c2091 '[textdict[1120778]]'
hide p2
$ update_portrait('st009_01 4', 'p209', [l(-22), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1120779]]'
hide p209
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120780]]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1120781]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st009_01 1', 'p209', [l(-22), light, flip], 6)
c2091 '[textdict[1120782]]'
hide p1
$ update_portrait('st009_01 1', 'p209', [l(-22), dark, flip], 6)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 5)
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[1120783]]'
return