label avg29011:

scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1007043]]'
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
c13 '[textdict[1007044]]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[textdict[1007045]]'
return