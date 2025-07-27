label avg22129:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1128262)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1128263)]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na07.ogg"
c13 '[convertstrid(1128264)]'
hide p1
$ update_portrait('oc003_01 10', 'p3', [mid(-6), light], 5)
c33 '[convertstrid(1128265)]'
hide p3
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_sc01_01.ogg"
c13 '[convertstrid(1128266)]'
return