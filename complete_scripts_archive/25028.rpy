label avg25028:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 3', 'p2000', [mid(-2), light], 5)
$ update_narrator('c20003')
window show
with fade_in
c20003 '[convertstrid(1210068)]'
hide p2000
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210069)]'
hide p1
$ update_portrait('uc001_01 1', 'p2000', [mid(-2), light], 5)
c20003 '[convertstrid(1210070)]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25029
    "[textdict[1215000]]":
        call avg25000
return