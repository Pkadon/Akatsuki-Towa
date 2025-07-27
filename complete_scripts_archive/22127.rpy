label avg22127:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1128253)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1128254)]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1128255)]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1128256)]'
hide p1
$ update_portrait('oc003_01 13', 'p3', [mid(-6), light], 5)
play sfxvoice "bcv_oc003_com_01.ogg"
c33 '[convertstrid(1128257)]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1128258)]'
hide p1
$ update_portrait('oc003_01 6', 'p3', [mid(-6), light], 5)
c33 '[convertstrid(1128259)]'
$ update_portrait('oc003_01 10', 'p3', [mid(-6), light], 5)
c33 '[convertstrid(1128260)]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
play sfx2 "other_7079.ogg"
c13 '[convertstrid(1128261)]'
return