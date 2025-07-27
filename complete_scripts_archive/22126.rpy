label avg22126:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1128251)]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1128252)]'
return