label avg10671:
stop music

play music "ed6324.ogg"
scene avg_bg_041
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
window show
with fade_in
c13041 '[textdict[1165936]]'
hide p1304
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1165937]]'
hide p1304
hide p1
c0 '[textdict[1165938]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
c23 '[textdict[1165939]]'
hide p2
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1165940]]'
hide p2
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1165941]]'
stop music
hide p3
hide p4
with fade
c13621 '[textdict[1165942]]'
c13633 '[textdict[1165943]]'
play music "ed7511.ogg"
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
with fade
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1165944]]'
hide p1
c0 '[textdict[1165945]]'
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 5)
c43 '[textdict[1165946]]'
hide p4
$ update_portrait('oc004_01 13', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1165947]]'
hide p4
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1165948]]'
hide p2
hide p1
c0 '[textdict[1165949]]'
play sfx2 "other_7079.ogg"
c13621 '[textdict[1165950]]'
play sfx2 "other_7080.ogg"
c13633 '[textdict[1165951]]'
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 5)
c33 '[textdict[1165952]]'
hide p3
$ update_portrait('oc003_01 21', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1165953]]'
hide p3
hide p4
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1165954]]'
return