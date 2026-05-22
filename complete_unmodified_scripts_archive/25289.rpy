label avg25289:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6019.ogg"
c13 '[convertstrid(1211102)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[convertstrid(1211103)]'
return