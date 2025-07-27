label avg25228:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6003.ogg"
play sfxvoice "bcv_oc002_win_02.ogg"
c23 '[convertstrid(1210811)]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210812)]'
return