label avg25045:

scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[textdict[1210114]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1210115]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210116]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210117]]'
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210118]]'
return