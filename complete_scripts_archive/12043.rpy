label avg12043:

play music "ed7117.ogg"
scene avg_bg_017
$ update_portrait('uc002_01 3', 'p5001', [r(2), light], 6)
$ update_narrator('c50013')
window show
with fade_in
play sfx2 "other_7057.ogg"
c50013 '[convertstrid(1121378)]'
$ update_portrait('uc002_01 3', 'p5001', [r(2), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
c11 '[convertstrid(1121379)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc002_01 4', 'p5001', [r_exit(2), light], 6)
play sfx2 "other_7086.ogg"
c50013 '[convertstrid(1121380)]'
hide p5001
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1121381)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1121382)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1121383)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1121384)]'
hide p2
$ update_portrait('sc068_01 6', 'p72', [l(-17), light, flip], 6)
play sfx2 "other_7020.ogg"
c721 '[convertstrid(1120383)]'
$ update_portrait('sc068_01 6', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1120384)]'
hide p72
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120385)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120386)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1120387)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c21 '[convertstrid(1120388)]'
hide p2
hide p1
c0 '[convertstrid(1121537)]'
return