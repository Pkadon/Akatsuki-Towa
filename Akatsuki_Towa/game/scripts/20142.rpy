label avg20142:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch04_b.ogg"
c23 '[textdict[1007519]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfx2 "other_7004.ogg"
c13 '[textdict[1007520]]'
return