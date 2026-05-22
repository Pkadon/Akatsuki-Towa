label avg20101:

$ play_music("ED6103.ogg")
scene avg_bg_035
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1123038)]'
$ update_portrait('st025_01 2', 'p224', [l(-17), light, flip], 6)
play sfx2 "other_7022.ogg"
c2241 '[convertstrid(1004904)]'
$ update_portrait('st025_01 2', 'p224', [l(-17), dark, flip], 5)
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
c6923 '[convertstrid(1004905)]'
hide p692
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
c153 '[convertstrid(1004906)]'
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
$ update_portrait('st025_01 4', 'p224', [l(-17), light, flip], 6)
c2241 '[convertstrid(1004907)]'
$ update_portrait('st025_01 2', 'p224', [l(-17), light, flip], 6)
play sfx2 "other_7071.ogg"
c2241 '[convertstrid(1004908)]'
$ update_portrait('st025_01 5', 'p224', [l(-17), light, flip], 6)
play sfx2 "other_7072.ogg"
c2241 '[convertstrid(1004909)]'
$ update_portrait('st025_01 2', 'p224', [l(-17), light, flip], 6)
c2241 '[convertstrid(1004910)]'
$ update_portrait('st025_01 3', 'p224', [l(-17), l_shake, light, flip], 6)
c2241 '[convertstrid(1004911)]'
$ update_portrait('st025_01 3', 'p224', [l(-17), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), r_shake, light], 6)
c153 '[convertstrid(1004912)]'
hide p15
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
play sfx2 "other_7073.ogg"
c6923 '[convertstrid(1004913)]'
$ update_portrait('st044_01 4', 'p692', [r(10), dark], 5)
$ update_portrait('st025_01 4', 'p224', [l(-17), light, flip], 6)
c2241 '[convertstrid(1004914)]'
return