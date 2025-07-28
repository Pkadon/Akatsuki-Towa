label avg10428:

play music "ed7526.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1141284)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[convertstrid(1141285)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1141286)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1141287)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1141288)]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1141289)]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1141290)]'
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
c31 '[convertstrid(1141291)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1141292)]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1141293)]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1141294)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1141295)]'
hide p4
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1141296)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1141297)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1141298)]'
menu:
    extend ""
    "[textdict[1141299]]":
        call avg10431
    "[textdict[1141300]]":
        call avg10429
    "[textdict[1141301]]":
        call avg10430
return