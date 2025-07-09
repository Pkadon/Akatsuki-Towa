label avg10565:
stop music

play music "ED6303.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1154337]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6009.ogg"
play sfxvoice "avg_vocal_ch20.ogg"
c21 '[textdict[1154338]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1154339]]'
hide p3
hide p1
$ update_portrait('st056_01 4', 'p1212', [l(-6), light, flip], 6)
with fade
c12121 '[textdict[1154340]]'
$ update_portrait('st056_01 4', 'p1212', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r_entrance(-3), light], 5)
play sfx2 "other_7085.ogg"
c23 '[textdict[1154341]]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st056_01 2', 'p1212', [l(-6), l_shake, light, flip], 6)
c12121 '[textdict[1154342]]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st056_01 4', 'p1212', [l(-6), light, flip], 6)
c12121 '[textdict[1154343]]'
$ update_portrait('st056_01 4', 'p1212', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1154344]]'
$ update_portrait('st056_01 4', 'p1212', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 5)
c23 '[textdict[1154345]]'
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('st056_01 4', 'p1212', [l(-6), light, flip], 6)
c12121 '[textdict[1154346]]'
$ update_portrait('st056_01 4', 'p1212', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch24.ogg"
c23 '[textdict[1154347]]'
hide p1212
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1154348]]'
hide p4
hide p2
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
with fade
c13 '[textdict[1154349]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1154350]]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1154351]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1154352]]'
hide p1
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
with fade
c13 '[textdict[1154353]]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1154354]]'
hide p3
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1154355]]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1154356]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1154357]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[textdict[1154358]]'
return