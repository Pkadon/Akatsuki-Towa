label avg25051:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 3', 'p2006', [mid(6), light], 6)
$ update_narrator('c20063')
window show
with fade_in
c20063 '[convertstrid(1210140)]'
hide p2006
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210141)]'
hide p1
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
c20063 '[convertstrid(1210142)]'
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 6)
c20063 '[convertstrid(1210143)]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25052
    "[textdict[1215000]]":
        call avg25000
return