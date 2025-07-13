label avg12424:

play music "ed7350.ogg"
scene avg_bg_052
$ update_narrator('c43')
window show
with fade_in
$ update_portrait('oc004_01 11', 'p4', [r_entrance(-5), light], 5)
c43 '[textdict[1142945]]'
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro18.ogg"
c31 '[textdict[1142946]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1142947]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1142948]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1142949]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1142950]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1142951]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li15.ogg"
c43 '[textdict[1142952]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1142953]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1142954]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 5)
c23 '[textdict[1142955]]'
return