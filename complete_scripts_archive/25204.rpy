label avg25204:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[convertstrid(1210695)]'
hide p2
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210696)]'
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c23 '[convertstrid(1210697)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfx2 "common_sephi2.ogg"
c13 '[convertstrid(1210698)]'
return