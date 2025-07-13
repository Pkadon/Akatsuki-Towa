label avg25175:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1210561]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210562]]'
hide p2
play sfx2 "elc_5002.ogg"
c0 '[textdict[1210563]]'
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na08.ogg"
c13 '[textdict[1210564]]'
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch20.ogg"
c23 '[textdict[1210565]]'
hide p2
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210566]]'
return