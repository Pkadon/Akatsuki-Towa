label avg25203:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[convertstrid(1210692)]'
hide p2
play sfx2 "other_7068.ogg"
c0 '[convertstrid(1210693)]'
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_na07.ogg"
c13 '[convertstrid(1210694)]'
return