label avg25190:

scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7079.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1210635]]'
hide p1
$ update_portrait('uc003_01 1', 'p2018', [mid(-26), light], 5)
play sfx2 "other_7091.ogg"
c20183 '[textdict[1210636]]'
hide p2018
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_atk_03.ogg"
c23 '[textdict[1210637]]'
return