label avg25040:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 3', 'p2001', [mid(6), light], 6)
$ update_narrator('c20013')
window show
with fade_in
c20013 '[convertstrid(1210102)]'
hide p2001
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210103)]'
hide p1
$ update_portrait('uc001_02 2', 'p2001', [mid(6), light], 6)
c20013 '[convertstrid(1210104)]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25041
    "[textdict[1215000]]":
        call avg25000
return