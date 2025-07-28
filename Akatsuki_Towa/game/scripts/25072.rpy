label avg25072:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "elc_5005.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210225)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfx2 "other_7034.ogg"
c13 '[convertstrid(1210226)]'
return