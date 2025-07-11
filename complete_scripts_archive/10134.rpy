label avg10134:

play music "ed7104.ogg"
scene avg_bg_014
window show
with fade_in
c0 '[textdict[1007359]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
play sfx2 "other_7064.ogg"
c23 '[textdict[1007360]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7072.ogg"
c11 '[textdict[1007361]]'
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 19', 'p2', [r_exit(-3), light], 5)
play sfx2 "other_7085.ogg"
c23 '[textdict[1007362]]'
hide p2
scene avg_bg_030
$ update_portrait('st004_01 2', 'p204', [l(4), light, flip], 6)
with fade
play sfx2 "other_7088.ogg"
c2041 '[textdict[1001637]]'
$ update_portrait('st004_01 2', 'p204', [l(4), dark, flip], 6)
$ update_portrait('sc043_01 1', 'p50', [r_entrance(-20), light], 5)
play sfx2 "other_7079.ogg"
c503 '[textdict[1001638]]'
$ update_portrait('sc043_01 1', 'p50', [r(-20), dark], 5)
$ update_portrait('st004_01 1', 'p204', [l(4), light, flip], 6)
c2041 '[textdict[1001639]]'
$ update_portrait('st004_01 1', 'p204', [l(4), dark, flip], 6)
$ update_portrait('sc043_01 4', 'p50', [r(-20), light], 5)
play sfx2 "other_7079.ogg"
c503 '[textdict[1001640]]'
$ update_portrait('sc043_01 4', 'p50', [r(-20), dark], 5)
$ update_portrait('st004_01 2', 'p204', [l(4), light, flip], 6)
c2041 '[textdict[1001641]]'
$ update_portrait('st004_01 5', 'p204', [l(4), light, flip], 6)
c2041 '[textdict[1001642]]'
$ update_portrait('st004_01 1', 'p204', [l(4), light, flip], 6)
play sfx2 "other_7088.ogg"
c2041 '[textdict[1001643]]'
hide p204
hide p50
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
with fade
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1001644]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1001645]]'
return