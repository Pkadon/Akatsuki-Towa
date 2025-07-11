label avg25231:

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[textdict[1210821]]'
c6123 '[textdict[1210822]]'
play sfx2 "other_7080.ogg"
c0 '[textdict[1210823]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210824]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210825]]'
return