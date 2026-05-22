label avg25190:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[convertstrid(1210635)]'
hide p1
$ update_portrait('uc003_01 1', 'p2018', [mid(-26), light], 6)
play sfx2 "other_7091.ogg"
c20183 '[convertstrid(1210636)]'
hide p2018
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_atk_03.ogg"
c23 '[convertstrid(1210637)]'
return