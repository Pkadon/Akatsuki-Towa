label avg12832:

$ play_music("ed7511.ogg")
scene avg_bg_004
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
c33 '[convertstrid(1185412)]'
$ update_portrait('oc003_01 21', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185413)]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185414)]'
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1185415)]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185416)]'
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1185417)]'
hide p2
$ update_portrait('st061_01 4', 'p1304', [r(-2), r_shake, light], 6)
c13043 '[convertstrid(1185418)]'
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185419)]' with shake
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185420)]'
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185421)]'
hide p16
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1185422)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1185423)]'
$ update_portrait('oc001_01 17', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1185424)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1185425)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185426)]'
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185427)]'
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185428)]'
hide p1
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185429)]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185430)]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185431)]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185432)]'
hide p16
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1185433)]'
hide p1304
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1185434)]'
hide p3
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_exit(-3), light, flip], 6)
c21 '[convertstrid(1185435)]'
hide p2
hide p4
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185436)]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185437)]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l_entrance(-18), light, flip], 6)
c161 '[convertstrid(1185438)]'
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1185439)]'
$ update_portrait('sc008_01 1', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1185440)]'
hide p16
hide p1304
c0 '[convertstrid(1185441)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1185442)]'
hide p1
play sfx2 "other_7085.ogg"
c0 '[convertstrid(1185443)]'
return