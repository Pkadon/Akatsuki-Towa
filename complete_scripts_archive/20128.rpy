label avg20128:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1006630)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1006631)]'
hide p2
$ update_portrait('sc044_01 1', 'p51', [mid(-7), light], 6)
c513 '[convertstrid(1006632)]'
return