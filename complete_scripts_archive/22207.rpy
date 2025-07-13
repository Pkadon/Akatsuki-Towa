label avg22207:

play music "ed7102.ogg"
scene avg_bg_008
$ update_narrator('c7211')
window show
with fade_in
play sfx2 "other_7064.ogg"
c7211 '[textdict[1128623]]'
$ update_portrait('oc002_01 1', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1128624]]'
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
c7211 '[textdict[1128625]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1128626]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1128627]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c7211 '[textdict[1128628]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1128629]]'
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 5)
c23 '[textdict[1128630]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1128631]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c7211 '[textdict[1128632]]'
c7211 '[textdict[1128633]]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1128634]]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1128635]]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1128636]]'
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
c7213 '[textdict[1128637]]'
c7213 '[textdict[1128638]]'
hide p4
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128639]]'
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1128640]]'
hide p2
c7213 '[textdict[1128641]]'
c7213 '[textdict[1128642]]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128643]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na10_b.ogg"
c11 '[textdict[1128644]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1128645]]'
return