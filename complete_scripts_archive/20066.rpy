label avg20066:

play music "ED6104.ogg"
scene placeholderbackground
window show
with fade_in
c0 '[textdict[1003452]]'
c0 '[textdict[1003453]]'
c0 '[textdict[1003454]]'
c0 '[textdict[1003455]]'
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1003456]]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [mid(-6), light], 5)
c33 '[textdict[1003457]]'
$ update_portrait('oc003_01 1', 'p3', [mid(-6), light], 5)
c33 '[textdict[1003458]]'
hide p3
$ update_portrait('oc004_01 8', 'p4', [mid(-5), light], 5)
c43 '[textdict[1003459]]'
$ update_portrait('oc004_01 1', 'p4', [mid(-5), light], 5)
c43 '[textdict[1003460]]'
hide p4
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
c13 '[textdict[1003461]]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
c23 '[textdict[1003462]]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
c23 '[textdict[1003463]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfx2 "other_7085.ogg"
c13 '[textdict[1003464]]'
return