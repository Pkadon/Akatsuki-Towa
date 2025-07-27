label avg25045:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[convertstrid(1210114)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na04.ogg"
c13 '[convertstrid(1210115)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210116)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210117)]'
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210118)]'
return