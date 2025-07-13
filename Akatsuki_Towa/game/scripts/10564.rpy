label avg10564:

play music "ED6303.ogg"
scene placeholderbackground
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 5)
$ update_narrator('c43')
window show
with fade_in
c43 '[textdict[1154316]]'
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l_entrance(-18), light, flip], 6)
play sfx2 "other_7088.ogg"
c161 '[textdict[1154317]]'
hide p4
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1154318]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1154319]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1154320]]'
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro10.ogg"
c33 '[textdict[1154321]]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1154322]]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1154323]]'
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 5)
c43 '[textdict[1154324]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1154325]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1154326]]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1154327]]'
hide p4
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch24.ogg"
c23 '[textdict[1154328]]'
hide p16
hide p2
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
with fade
c161 '[textdict[1154329]]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1154330]]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1154331]]'
$ update_portrait('sc008_01 4', 'p16', [l_exit(-18), light, flip], 6)
c161 '[textdict[1154332]]'
hide p16
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[textdict[1154333]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 5)
c43 '[textdict[1154334]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
c31 '[textdict[1154335]]'
return