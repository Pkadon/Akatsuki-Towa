label avg20142:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch04_b.ogg"
c23 '[convertstrid(1007519)]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfx2 "other_7004.ogg"
c13 '[convertstrid(1007520)]'
return