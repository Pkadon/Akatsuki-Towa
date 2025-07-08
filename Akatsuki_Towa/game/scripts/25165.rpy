label avg25165:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210539]]'
hide p1
play sfx2 "other_7082.ogg"
c20173 '[textdict[1210540]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210541]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210542]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210543]]'
return