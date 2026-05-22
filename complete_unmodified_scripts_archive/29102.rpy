label avg29102:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1218014)]'
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218015)]'
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218016)]'
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218017)]'
hide p9
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[convertstrid(1218018)]'
return