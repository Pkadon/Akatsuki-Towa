label avg20018:

$ play_music("ed7561.ogg")
scene avg_bg_064
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7088.ogg"
c13 '[convertstrid(1001032)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1001033)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[convertstrid(1001034)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r_exit(-2), light], 6)
play sfx2 "other_7020.ogg"
c13 '[convertstrid(1001035)]'
hide p1
return