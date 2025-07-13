label avg12035:

play music "ed7101.ogg"
scene avg_bg_020
$ update_narrator('c0')
window show
with fade_in
c0 '[textdict[1121557]]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1121558]]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1121559]]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st033_01 3', 'p537', [r(-7), light], 5)
c5373 '[textdict[1121560]]'
$ update_portrait('st033_01 3', 'p537', [r(-7), dark], 5)
$ update_portrait('oc002_01 20', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6003.ogg"
c21 '[textdict[1121561]]'
hide p537
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1120215]]'
hide p1
$ update_portrait('st033_01 3', 'p537', [r(-7), light], 5)
c5373 '[textdict[1120216]]'
$ update_portrait('st033_01 3', 'p537', [r(-7), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120217]]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st033_01 2', 'p537', [r(-7), light], 5)
c5373 '[textdict[1120218]]'
hide p2
hide p537
play sfx2 "other_7067.ogg"
c0 '[textdict[1120219]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120220]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1120221]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120222]]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1120223]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c21 '[textdict[1120224]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st033_01 2', 'p537', [r(-7), light], 5)
c5373 '[textdict[1120225]]'
$ update_portrait('st033_01 2', 'p537', [r(-7), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120226]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st033_01 4', 'p537', [r_exit(-7), light], 5)
c5373 '[textdict[1120227]]'
hide p537
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1120228]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120229]]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch09.ogg"
c21 '[textdict[1120230]]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1120231]]'
return