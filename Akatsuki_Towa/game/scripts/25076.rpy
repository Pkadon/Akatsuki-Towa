label avg25076:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[convertstrid(1210231)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfx2 "elc_5005.ogg"
c13 '[convertstrid(1210232)]'
return