label avg22130:

stop music
scene avg_bg_036
$ update_portrait('oc003_01 9', 'p3', [mid(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
play sfxvoice "avg_vocal_ro15.ogg"
c33 '[convertstrid(1128262)]'
hide p3
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1128263)]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1128264)]'
hide p1
$ update_portrait('oc003_01 10', 'p3', [mid(-6), light], 6)
c33 '[convertstrid(1128265)]'
hide p3
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1128266)]'
return