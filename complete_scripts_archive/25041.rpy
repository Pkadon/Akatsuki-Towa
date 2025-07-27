label avg25041:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[convertstrid(1210105)]'
hide p2
$ update_portrait('uc001_02 1', 'p2001', [mid(6), light], 5)
c20013 '[convertstrid(1210106)]'
return